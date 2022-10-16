import json
import re

from django.db import connection
from django.http import JsonResponse


def get_data(sel, table_name, limit):
    cur = connection.cursor()
    cmd_str = "SELECT " + sel + " FROM " + table_name + " WHERE " + limit
    print(cmd_str)
    cur.execute(cmd_str)
    ret = cur.fetchall()
    return ret


def get_user(email):
    cur = connection.cursor()
    cur.execute("SELECT UE, UN, AVATAR, UTP, UB, PW FROM users WHERE UE=%s", (email,))
    sql_result = cur.fetchall()
    sql_result = sql_result[0]
    return {"email": sql_result[0], "username": sql_result[1],
            "avatar": sql_result[2], "usertype": sql_result[3], "profile": sql_result[4],
            "password": sql_result[5]}


# Create your views here.
# 10.12: 初步实验，注册及登录的部分逻辑
def login(request):
    if request.method == "POST":
        # if request.session.get('email') is not None:
        #     return JsonResponse({"errno": 1, "msg": "请勿重复登录！"})
        print(request.body)
        json_str = request.body.decode()
        payload = json.loads(request.body)
        email = payload.get("email")
        password = payload.get("password")
        if email == "":
            return JsonResponse({"errno": 2, "msg": "错误的用户名git或密码"})
        cur = connection.cursor()
        cur.execute("SELECT PW FROM users WHERE UE=%s", (email,))
        sql_result = cur.fetchall()
        if len(sql_result) == 1:
            ref_password = sql_result[0][0]
            if ref_password != password:
                return JsonResponse({"errno": 2,
                                     "msg": "错误的用户名或密码"})  # why need this
            # 由于数据库要求不能使用ORM，使用session完成AUTH + User的功能，session存储在内存Cache中，规避ORM
            request.session['email'] = email
            ret = get_user(email)
            ret['errno'] = 0
            ret['msg'] = "登录成功"
            return JsonResponse(ret)
        elif len(sql_result) == 0:
            return JsonResponse({"errno": 2, "msg": "错误的用户名或密码"})
        return JsonResponse({"errno": 3, "msg": "未知异常"})


# 10.12: 初步实验
def register(request):
    if request.method == "POST":
        print(request.body)
        json_str = request.body.decode()
        payload = json.loads(json_str)
        email = payload.get("email")
        email_re = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        if not re.match(email_re, email):
            return JsonResponse({"errno": 3, "msg": "错误的邮箱格式"})
        nickname = payload.get("username")
        if nickname == '':
            return JsonResponse({"errno": 4, "msg": "用户名不能为空"})
        # TODO useravatar = payload.get("useravatar")
        password = payload.get("password_1")
        if len(password) < 3:
            return JsonResponse({"errno": 5, "msg": "您输入的密码过短，至少为3位"})
        password_c = [False, False]
        for c in password:
            if c.isupper():
                password_c[0] = True
            if c.islower():
                password_c[1] = True
        if not (password_c[0] and password_c[1]):
            return JsonResponse({"errno": 6, "msg": "您输入的密码至少应包含大小写字母"})
        password_check = payload.get("password_2")
        if password_check != password:
            return JsonResponse({"errno": 1, "msg": "两次输入的密码不一致"})
        type_id = payload.get("usertype")
        bio = None
        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE UE=%s", (email,))
        sql_result = cur.fetchall()
        if len(sql_result) != 0:
            return JsonResponse({"errno": 2, "msg": "邮箱已注册"})
        cur.execute("INSERT INTO users (UE, UN, AVATAR, PW, UTP, UB) VALUES(%s,%s,%s,%s,%s,%s)",
                    (email, nickname, 'NULL', password, type_id, bio))
        if type_id == '1':
            cur.execute("INSERT INTO musicians (UE, MN, OC) VALUES(%s,%s,%s)", (email, nickname,
                                                                                'DEFAULT_OC'))  # TODO: ADD INTERFACE IN FRONTEND
        return JsonResponse({"errno": 0, "msg": "注册成功"})


def logoff(request):
    if request.method == "GET":
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        print(email + ": logoff")
        del request.session['email']
        return JsonResponse({"errno": 0, "msg": "已注销"})


def delete_account(request):
    if request.method == "POST":
        email = request.session.get('email')
        cur = connection.cursor()
        cur.execute("DELETE FROM users WHERE UE=%s", (email,))
        return JsonResponse({"errno": 0, "msg": "注销成功"})


def get_user_info(request):
    if request.method == "GET":
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        ret = get_user(email)
        return JsonResponse({
            'email': ret['email'],
            'nickname': ret['username'],
            'useravatar': ret['avatar'],
            'type': ret['usertype'],
            'bio': ret['profile']})


def set_user_info(request):
    if request.method == "POST":
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        check_list = [('nickname', 'UN'), ('useravatar', 'AVATAR'), ('password', 'PW'),
                      ('type', 'UTP'), ('bio', 'UB')]
        json_str = request.body.decode()
        payload = json.loads(json_str)
        print(payload)
        cur = connection.cursor()
        for check_unit in check_list:
            if payload.get(check_unit[0]) is not None:
                ctrl_str = 'UPDATE users SET ' + check_unit[1] + '=' + f"'{payload[check_unit[0]]}' " \
                           + f" WHERE UE='{email}' "
                cur.execute(ctrl_str)
        return JsonResponse({"errno": 0, "msg": "修改成功"})


def get_album(request):
    if request.method == "GET":
        email = request.session.get('email')
        if email is None:
            return JsonResponse(list(), safe=False)
        mid_list = get_data('MID,MN', 'musicians', f"UE='{email}'")
        if len(mid_list) == 0:
            return JsonResponse(list(), safe=False)
        mid = mid_list[0][0]
        mn = mid_list[0][1]
        album_list = get_data('AN,AP,AU,RY,MID,TYP,SRC', 'albums', f"MID={mid}")
        print(album_list)
        var = [{
            'albumName': elem[0],
            'price': elem[1],
            'author': elem[2],
            'releaseYear': elem[3],
            'releaser': mn,
            'type': elem[5],
            'resource': elem[6]
        } for elem in album_list]
        return JsonResponse(var, safe=False)


def set_album(request):
    if request.method == "POST":
        json_str = request.body.decode()
        payload = json.loads(json_str)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        mid_list = get_data('MID', 'musicians', f"UE='{email}'")
        if len(mid_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        mid = mid_list[0][0]
        new_data = payload['NewAlbumData']
        tag = payload['Tag']
        cur = connection.cursor()
        if tag < 0:
            cur.execute('INSERT INTO albums (AN, AP, AU, MID, RY, AC, TYP, SRC) values(%s,%s,%s,%s,%s,%s,%s,%s)',
                        (new_data['albumName'], new_data['price'], new_data['author'], mid,
                         new_data['releaseYear'], new_data['cover'], new_data['type'], new_data['resource']))
            return JsonResponse({"errno": 0, "msg": "新建唱片成功！"})
        cast_list = [
            ('albumName', 'AN'),
            ('price', 'AP'),
            ('author', 'AU'),
            # ('releaser', 'MID'), todo: config it's useless
            ('releaseYear', 'RY'),
            ('cover', 'AC'),
            ('type', 'TYP'),
            ('resource', 'SRC')
        ]
        old_album = get_data('MID', 'albums', f"AID={tag} AND MID={mid}")
        if len(old_album) == 0:
            return JsonResponse({"errno": 3, "msg": "无此唱片，或唱片不属于此用户"})
        for elem in cast_list:
            if new_data.get(elem[0]) is not None:
                ctrl_str = 'UPDATE albums SET ' + elem[1] + '=' + f"'{new_data[elem[0]]}' " \
                           + f" WHERE AID='{tag}' "
                cur.execute(ctrl_str)
        return JsonResponse({"errno": 0, "msg": "修改唱片成功！"})


def get_musician(request):
    if request.method == "GET":
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        mid_list = get_data('MID, MN, PH, OC, LC, LT, FY, INFO', 'musicians', f"UE='{email}'")
        if len(mid_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        mid_list = mid_list[0]
        return JsonResponse({
            'musicianName': mid_list[1],
            'photo': mid_list[2],
            'originCountry': mid_list[3],
            'location': mid_list[4],
            'lyricalThemes': mid_list[5],
            'formedYear': mid_list[6],
            'introduction': mid_list[7]
        })


def set_musician(request):
    if request.method == "POST":
        json_str = request.body.decode()
        payload = json.loads(json_str)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        mid_list = get_data('MID', 'musicians', f"UE='{email}'")
        if len(mid_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        mid = mid_list[0][0]
        cast_list = [
            ('musicianName', 'MN'),
            ('photo', 'PH'),
            ('originCountry', 'OC'),
            ('location', 'LC'),
            ('lyricalThemes', 'LT'),
            ('formedYear', 'FY'),
            ('introduction', 'INFO')
        ]
        cur = connection.cursor()
        for elem in cast_list:
            if payload.get(elem[0]) is not None:
                ctrl_str = 'UPDATE musicians SET ' + elem[1] + '=' + f"'{payload[elem[0]]}' " \
                           + f" WHERE MID='{mid}' "
                cur.execute(ctrl_str)
        return JsonResponse({"errno": 0, "msg": "修改音乐人信息成功！"})
