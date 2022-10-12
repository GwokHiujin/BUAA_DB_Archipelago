from django.shortcuts import render

import json
from django.db import connection
# Create your views here.
from django.http import HttpResponse, JsonResponse


# 10.12: 初步实验，注册及登录的部分逻辑
def login(request):
    if request.method == "POST":
        json_str = request.body.decode()
        payload = json.loads(json_str)
        email = payload.get("email")
        password = payload.get("password")
        cur = connection.cursor()
        cur.execute("SELECT PW FROM users WHERE UE=%s", email)
        sql_result = cur.fetchall()
        if len(sql_result) == 1:
            ref_password = sql_result[0][0]
            if ref_password != password:
                return JsonResponse({"success": False, "message": "错误的用户名或密码", "userID": 0})
            return JsonResponse({"success": True, "message": "登录成功", "userID": 0})
        elif len(sql_result) == 0:
            return JsonResponse({"success": False, "message": "错误的用户名或密码", "userID": 0})
        return JsonResponse({"success": False, "message": "未知异常", "userID": 0})
    #             return JsonResponse({"success": True, "message": "登录成功，已为您的密码加密", "userID": user[0].user_id})
    #         elif check_password(password, (user[0]).user_password):
    #             return JsonResponse({"success": True, "message": "登录成功", "userID": user[0].user_id})
    #         else:
    #             return JsonResponse({"success": False, "message": "密码错误", "userID": user[0].user_id})
    # else:
    #     JsonResponse({"success": False, "message": "请求异常"})


# 10.12: 初步实验
def register(request):
    if request.method == "POST":
        json_str = request.body.decode()
        print(json_str)
        payload = json.loads(json_str)
        email = payload.get("email")
        nickname = payload.get("nickname")
        # TODO useravatar = payload.get("useravatar")
        password = payload.get("password")
        type_id = payload.get("type")
        bio = payload.get("bio")
        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE UE=%s", email)
        sql_result = cur.fetchall()
        if len(sql_result) != 0:
            return JsonResponse({"success": False, "message": "邮箱已注册"})
        cur.execute("INSERT INTO users (UE, UN, AVATAR, PW, UTP, UB) VALUES(%s,%s,%s,%s,%s,%s)",
                    (email, nickname, 'NULL', password, type_id, bio))
        return JsonResponse({"success": True, "message": "注册成功"})
