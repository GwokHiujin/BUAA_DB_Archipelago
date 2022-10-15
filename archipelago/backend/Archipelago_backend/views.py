import json
import re

from django.db import connection
from django.http import JsonResponse


# Create your views here.
# 10.12: 初步实验，注册及登录的部分逻辑
def login(request):
    if request.method == "POST":
        if request.session.get('email') is not None:
            return JsonResponse({"errno": 1, "msg": "请勿重复登录！"})
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
            cur.execute("SELECT UE, UN, AVATAR, UTP, UB, PW FROM users WHERE UE=%s", (email,))
            sql_result = cur.fetchall()
            sql_result = sql_result[0]
            print(sql_result)
            return JsonResponse({"errno": 0, "msg": "登录成功", "email": sql_result[0], "username": sql_result[1],
                                 "avatar": sql_result[2], "usertype": sql_result[3], "profile": sql_result[4],
                                 "password": sql_result[5]})
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
        email = request.session.get('userEmail')
        cur = connection.cursor()
        cur.execute("DELETE FROM users WHERE UE=%s", (email,))
        return JsonResponse({"errno": 0, "msg": "注销成功"})
