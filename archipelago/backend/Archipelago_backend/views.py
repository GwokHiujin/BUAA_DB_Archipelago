import datetime
import json
import random
import re

from django.db import connection, transaction
from django.db.models import Q
from django.db.models import F
from django.http import JsonResponse
from Archipelago_backend.models import *


def get_payload(request):
    json_str = request.body.decode()
    payload = json.loads(json_str)
    # payload = payload.get("data")
    return payload


def get_user(email):
    user = User.objects.filter(user_id=email)
    user = user[0]
    return {"email": user.user_id, "name": user.user_name,
            "avatar": user.avatar, "type": user.user_type, "bio": user.bio}


# Create your views here.
# 10.12: 初步实验，注册及登录的部分逻辑
def login(request):
    if request.method == "POST":
        print(request.body)
        payload = get_payload(request)
        email = payload.get('email')
        password = payload.get('password')
        if email == "" or email is None:
            return JsonResponse({"errno": 2, "msg": "错误的用户名或密码"})
        user = User.objects.filter(user_id=email)
        if len(user) != 1:
            return JsonResponse({"errno": 3, "msg": "未知异常"})
        user = user[0]
        ref_password = user.password
        if ref_password != password:
            return JsonResponse({"errno": 2,
                                 "msg": "错误的用户名或密码"})
        request.session['email'] = email
        ret = dict()
        ret['data'] = get_user(email)
        musician = Musician.objects.filter(user=user)
        if len(musician) != 0:
            ret['data']['musicianID'] = musician[0].id
        ret['errno'] = 0
        ret['msg'] = "登录成功"
        return JsonResponse(ret)


# 10.12: 初步实验
def register(request):
    if request.method == "POST":
        print(request.body)
        payload = get_payload(request)
        email = payload.get("email")
        # email_re = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        # if not re.match(email_re, email):
        #     return JsonResponse({"errno": 3, "msg": "错误的邮箱格式"})
        nickname = payload.get("name")
        if nickname == '':
            return JsonResponse({"errno": 4, "msg": "用户名不能为空"})
        # TODO useravatar = payload.get("useravatar")
        password = payload.get("password_1")
        # if len(password) < 3:
        #     return JsonResponse({"errno": 5, "msg": "您输入的密码过短，至少为3位"})
        # password_c = [False, False]
        # for c in password:
        #     if c.isupper():
        #         password_c[0] = True
        #     if c.islower():
        #         password_c[1] = True
        # if not (password_c[0] and password_c[1]):
        #     return JsonResponse({"errno": 6, "msg": "您输入的密码至少应包含大小写字母"})
        password_check = payload.get("password_2")
        if password_check != password:
            return JsonResponse({"errno": 1, "msg": "两次输入的密码不一致"})
        type_id = payload.get("type")
        bio = " "
        user = User.objects.filter(user_id=email)
        if len(user) != 0:
            return JsonResponse({"errno": 2, "msg": "邮箱已注册"})
        new_user = User(user_id=email, user_name=nickname, user_type=type_id, password=password, bio=bio)
        new_user.save()
        if type_id == '1':
            new_musician = Musician(user=new_user, musician_name=nickname, user_type=type_id, nationality='Default_OC')
            new_musician.save()
        return JsonResponse({"errno": 0, "msg": "注册成功"})


def logoff(request):
    if request.method == "GET":
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "用户未登录"})
        print(email + ": logoff")
        del request.session['email']
        return JsonResponse({"errno": 0, "msg": "已注销"})


def delete_account(request):
    if request.method == "POST":
        payload = get_payload(request)
        email = payload.get('email')
        passwd = payload.get('password')
        user = User.objects.filter(user_id=email)
        if len(user) == 0:
            return JsonResponse({"errno": 1, "msg": "注销失败！密码不匹配"})
        user = user[0]
        old_password = user.password
        if passwd != old_password:
            return JsonResponse({"errno": 1, "msg": "注销失败！密码不匹配"})
        user.delete()
        return JsonResponse({"errno": 0, "msg": "注销成功"})


def get_user_info(request):
    if request.method == "GET":
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        ret = dict()
        ret["data"] = get_user(email)
        ret["errno"] = 0
        ret["msg"] = "成功"
        return JsonResponse(ret)


def set_user_info(request):
    if request.method == "POST":
        payload = get_payload(request)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.select_for_update().objects.get(user_id=email)
        check_list = [('name', 'user_name'), ('avatar', 'avatar'), ('password', 'password'),
                      ('bio', 'bio')
                      # ,('type', 'user_type')
                      ]
        print(payload)
        cur = connection.cursor()
        if payload.get('password') is not None:
            old_password = user.password
            if payload['oldPassword'] != old_password:
                return JsonResponse({"errno": 2, "msg": "旧密码输入错误"})
        for check_unit in check_list:
            if payload.get(check_unit[0]) is not None:
                update_data = {check_unit[1]: payload.get(check_unit[0])}
                user.update(**update_data)
                user.save()

        return JsonResponse({"errno": 0, "msg": "修改成功"})


def get_album_info(request):
    if request.method == "POST":
        payload = get_payload(request)
        album = Album.objects.filter(id=payload.get('albumID'))
        if len(album) == 0:
            return JsonResponse({"errno": 1, "msg": "成功"})
        album = album[0]
        song_list = Song.objects.filter(album=album)
        return JsonResponse({
            "errno": 0, "msg": "成功",
            "generalInfo": {"albumID": album.id, "albumName": album.album_name, "price": album.album_price,
                            "author": album.album_producer, "releaseYear": album.release_year,
                            "releaser": album.musician.musician_name, "cover": album.cover, "type": album.type,
                            "resource": album.source, "salesVolume": album.sales_volume},
            "songList": [{"name": s.song_name, "songLast": s.song_last, "ADT": s.resource, "albumID": album.id} for s in
                         song_list]
        })


def get_album(request):
    if request.method == "GET":
        email = request.session.get('email')
        if email is None:
            return JsonResponse(list(), safe=False)
        user = User.objects.get(user_id=email)
        mid_list = Musician.objects.filter(user=user)
        if len(mid_list) == 0:
            return JsonResponse(list(), safe=False)
        mn = mid_list[0].musician_name
        album_list = Album.objects.filter(musician=mid_list[0])
        print(album_list)
        var = [{
            'albumID': elem.id,
            'albumName': elem.album_name,
            'price': elem.album_price,
            'author': elem.album_producer,
            'releaseYear': elem.release_year,
            'releaser': mn,
            'type': elem.type,
            'resource': elem.source,
            'salesVolume': elem.sales_volume
        } for elem in album_list]
        return JsonResponse(var, safe=False)
    if request.method == "POST":
        payload = get_payload(request)
        musician_id = payload.get('musicianID')
        mid_list = Musician.objects.filter(id=musician_id)
        if len(mid_list) == 0:
            return JsonResponse(list(), safe=False)
        mn = mid_list[0].musician_name
        album_list = Album.objects.filter(musician=mid_list[0])
        print(album_list)
        var = [{
            'albumID': elem.id,
            'albumName': elem.album_name,
            'price': elem.album_price,
            'author': elem.album_producer,
            'releaseYear': elem.release_year,
            'releaser': mn,
            'type': elem.type,
            'resource': elem.source,
            'salesVolume': elem.sales_volume
        } for elem in album_list]
        return JsonResponse({'errno': 0, 'msg': '成功', 'albumList': var}, safe=False)


def set_album(request):
    if request.method == "POST":
        payload = get_payload(request)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.objects.get(user_id=email)
        musician_list = Musician.objects.filter(user=user)
        if len(musician_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        musician = musician_list[0]
        new_data = payload['NewAlbumData']
        tag = payload['Tag']
        if tag < 0:
            new_album = Album(album_name=new_data['albumName'],
                              album_price=new_data['price'],
                              album_producer=new_data['author'],
                              release_year=new_data['releaseYear'],
                              cover=new_data['cover'],
                              type=new_data['type'],
                              source=new_data['resource'])
            new_album.save()
            if payload.get('songs') is None:
                return JsonResponse({"errno": 0, "msg": "新建唱片成功！"})
            for new_song_json in payload['songs']:
                new_song = Song(song_name=new_song_json.get('name'), song_last=new_song_json.get('songLength'),
                                resource=new_song_json.get('ADT'),
                                album=new_album)
                new_song.save()
            return JsonResponse({"errno": 0, "msg": "新建唱片并添加歌曲成功！"})

        old_album = Album.objects.select_for_update().filter(Q(musician=musician) and Q(id=tag))
        if len(old_album) == 0:
            return JsonResponse({"errno": 3, "msg": "无此唱片，或唱片不属于此用户"})
        cast_list = [
            ('albumName', 'album_name'),
            ('price', 'album_price'),
            ('author', 'album_producer'),
            # ('releaser', 'MID'), config it's useless
            ('releaseYear', 'release_year'),
            ('cover', 'cover'),
            ('type', 'type'),
            ('resource', 'source')
        ]
        for elem in cast_list:
            if new_data.get(elem[0]) is not None:
                update_data = {elem[1]: payload.get(elem[0])}
                old_album.update(**update_data)
                old_album.save()
        return JsonResponse({"errno": 0, "msg": "修改唱片成功！"})


def del_album(request):
    if request.method == "POST":
        payload = get_payload(request)
        sel_album = Album.objects.filter(id=payload['Tag'])
        if len(sel_album) == 0:
            return JsonResponse({"errno": 1, "msg": "唱片不存在"})
        sel_album = sel_album[0]
        user = User.objects.get(user_id=email)
        musician_list = Musician.objects.filter(user=user)
        if len(musician_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        musician = musician_list[0]
        if sel_album.musician != musician:
            return JsonResponse({"errno": 3, "msg": "当前唱片不属于此用户"})
        sel_album.delete()
        return JsonResponse({"errno": 0, "msg": "成功"})


def get_musician(request):
    if request.method == "GET":
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.objects.get(user_id=email)
        musician_list = Musician.objects.filter(user=user)
        if len(musician_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        musician = musician_list[0]
        return JsonResponse({
            'errno': 0,
            'msg': '成功',
            'data': {
                'musicianName': musician.musician_name,
                'photo': musician.photo,
                'originCountry': musician.nationality,
                'location': musician.location,
                'lyricalThemes': musician.theme,
                'formedYear': musician.found_year,
                'introduction': musician.info
            }
        })
    if request.method == "POST":
        payload = get_payload(request)
        musician_list = Musician.objects.filter(id=payload.get('musicianID'))
        if len(musician_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        musician = musician_list[0]
        return JsonResponse({
            'errno': 0,
            'msg': '成功',
            'data': {
                'musicianName': musician.musician_name,
                'photo': musician.photo,
                'originCountry': musician.nationality,
                'location': musician.location,
                'lyricalThemes': musician.theme,
                'formedYear': musician.found_year,
                'introduction': musician.info
            }
        })


def get_all_musician(request):
    if request.method == "GET":
        musician_list = Musician.objects.all
        return JsonResponse({'data': [{
            'musicianName': musician.musician_name,
            'photo': musician.photo,
            'originCountry': musician.nationality,
            'location': musician.location,
            'lyricalThemes': musician.theme,
            'formedYear': musician.found_year,
            'introduction': musician.info} for musician in musician_list]
        })


def set_musician(request):
    if request.method == "POST":
        payload = get_payload(request)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.objects.get(user_id=email)
        musician_list = Musician.objects.select_for_update().filter(user=user)
        if len(musician_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        musician = musician_list[0]
        cast_list = [
            ('musicianName', 'musician_name'),
            ('photo', 'photo'),
            ('originCountry', 'nationality'),
            ('location', 'location'),
            ('lyricalThemes', 'theme'),
            ('formedYear', 'found_year'),
            ('introduction', 'info')
        ]
        for elem in cast_list:
            if payload.get(elem[0]) is not None:
                update_data = {elem[1]: payload.get(elem[0])}
                musician.update(**update_data)
                musician.save()
        return JsonResponse({"errno": 0, "msg": "修改音乐人信息成功！"})


def add_musician_member(request):
    if request.method == "POST":
        payload = get_payload(request)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.objects.get(user_id=email)
        musician_list = Musician.objects.filter(user=user)
        if len(musician_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        musician = musician_list[0]
        if musician.id != payload.get('musicianID'):
            return JsonResponse({"errno": 3, "msg": "错误绑定音乐人信息"})
        old_member = MusicianMember.objects.filter(musician=musician, member_name=payload.get('N'))
        if len(old_member) != 0:
            return JsonResponse({"errno": 4, "msg": "该成员已存在"})
        new_member = MusicianMember(musician=musician,
                                    member_name=payload.get('name'),
                                    birthday=payload.get('birthday'),
                                    role=payload.get('role'),
                                    active_year=payload.get('activeYear'))
        new_member.save()
        all_member = MusicianMember.objects.filter(musician=musician)
        all_member = [{"name": member.member_name,
                       "birthday": member.birthday,
                       "role": member.role,
                       "activeYear": member.active_year} for member in all_member]
        return JsonResponse({"errno": 0, "msg": "成功", "data": all_member})


def set_musician_member(request):
    if request.method == "POST":
        payload = get_payload(request)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.objects.get(user_id=email)
        musician_list = Musician.objects.filter(user=user)
        if len(musician_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        musician = musician_list[0]
        # if musician.id != payload.get('musicianID'):
        #     return JsonResponse({"errno": 3, "msg": "错误绑定音乐人信息"})
        old_member = MusicianMember.objects.select_for_update().filter(musician=musician,
                                                                       member_name=payload.get('name'))
        if len(old_member) != 1:
            return JsonResponse({"errno": 4, "msg": "该成员不存在"})
        old_member = old_member[0]
        cast_list = [
            # ('N', 'member_name'),
            ('birthday', 'birthday'),
            ('role', 'role'),
            ('activeYear', 'active_year')
        ]
        for elem in cast_list:
            if payload.get(elem[0]) is not None:
                update_data = {elem[1]: payload.get(elem[0])}
                old_member.update(**update_data)
                old_member.save()
        all_member = MusicianMember.objects.filter(musician=musician)
        all_member = [{"name": member.member_name,
                       "birthday": member.birthday,
                       "role": member.role,
                       "activeYear": member.active_year} for member in all_member]
        return JsonResponse({"errno": 0, "msg": "成功", "data": all_member})


def get_musician_member(request):
    if request.method == "POST":
        payload = get_payload(request)
        musician_list = Musician.objects.filter(id=payload.get('musicianID'))
        if len(musician_list) == 0:
            return JsonResponse({"errno": 1, "msg": "音乐人不存在"})
        musician = musician_list[0]
        all_member = MusicianMember.objects.filter(musician=musician)
        all_member = [{"name": member.member_name,
                       "birthday": member.birthday,
                       "role": member.role,
                       "activeYear": member.active_year} for member in all_member]
        return JsonResponse({"errno": 0, "msg": "成功", "data": all_member})


def del_musician_member(request):
    if request.method == "POST":
        payload = get_payload(request)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.objects.get(user_id=email)
        musician_list = Musician.objects.filter(user=user)
        if len(musician_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        musician = musician_list[0]
        # if musician.id != payload.get('MID'):
        #     return JsonResponse({"errno": 3, "msg": "错误绑定音乐人信息"})
        old_member = MusicianMember.objects.filter(musician=musician, member_name=payload.get('N'))
        if len(old_member) != 1:
            return JsonResponse({"errno": 4, "msg": "该成员不存在"})
        old_member = old_member[0]
        old_member.delete()
        all_member = MusicianMember.objects.filter(musician=musician)
        all_member = [{"name": member.member_name,
                       "birthday": member.birthday,
                       "role": member.role,
                       "activeYear": member.active_year} for member in all_member]
        return JsonResponse({"errno": 0, "msg": "成功", "data": all_member})


def get_musician_tag(request):
    if request.method == "POST":
        payload = get_payload(request)
        mid = payload.get('MID')
        if mid == None:
            return JsonResponse({"errno": 1, "msg": "该音乐人不存在"})
        musician = Musician.objects.filter(id=mid)
        if len(musician) == 0:
            return JsonResponse({"errno": 1, "msg": "该音乐人不存在"})
        musician = musician[0]
        all_tag = MusicianTag.objects.filter(musician=musician)
        all_tag = [{"tag": tag.tag.tag_name} for tag in all_tag]
        return JsonResponse({"errno": 0, "msg": "成功", "data": all_tag})


@transaction.atomic
def add_del_musician_tag(request):
    if request.method == "POST":
        payload = get_payload(request)
        mid = payload.get('musicianID')
        if mid == None:
            return JsonResponse({"errno": 1, "msg": "该音乐人不存在"})
        musician = Musician.objects.filter(id=mid)
        if len(musician) == 0:
            return JsonResponse({"errno": 1, "msg": "该音乐人不存在"})
        musician = musician[0]
        for tag_json in payload['tagList']:
            tag_sel = Tag.objects.filter(tag_name=tag_json['tag'], tag_type=tag_json['tagType'])
            if len(tag_sel) == 0:
                tag_sel = Tag(tag_name=tag_json['tag'], tag_type=tag_json['tagType'], popularity=0)
                tag_sel.save()
            else:
                tag_sel = tag_sel[0]
            old_musician_tag = MusicianTag.objects.filter(tag=tag_sel, musician=musician)
            if len(old_musician_tag) == 0:
                continue
            new_musician_tag = MusicianTag(tag=tag_sel, musician=musician)
            tag_sel.popularity += 1
            tag_sel.save()
            new_musician_tag.save()
        return JsonResponse({"errno": 0, "msg": "成功"})


def add_song(request):
    if request.method == "POST":
        payload = get_payload(request)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.objects.get(user_id=email)
        musician_list = Musician.objects.filter(user=user)
        if len(musician_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        musician = musician_list[0]
        album_list = Album.objects.filter(id=payload.get('AID'), musician=musician)
        if len(album_list) == 0:
            return JsonResponse({"errno": 3, "msg": "唱片不存在或不归属当前音乐人"})
        album = album_list[0]
        old_song = Song.objects.filter(song_name=payload.get('SN'), album=album)
        if len(old_song) == 1:
            return JsonResponse({"errno": 4, "msg": "歌曲已存在"})
        new_song = Song(song_name=payload.get('name'), song_last=payload.get('songLength'),
                        resource=payload.get('ADT'),
                        album=album)
        new_song.save()
        all_song = Song.objects.filter(album=album)
        all_song = [{"SN": song.song_name,
                     "SL": song.song_last,
                     "ADT": song.resource} for song in all_song]
        return JsonResponse({"errno": 0, "msg": "成功", "data": all_song})


def set_song(request):
    if request.method == "POST":
        payload = get_payload(request)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.objects.get(user_id=email)
        musician_list = Musician.objects.filter(user=user)
        if len(musician_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        musician = musician_list[0]
        album_list = Album.objects.filter(id=payload.get('albumID'), musician=musician)
        if len(album_list) == 0:
            return JsonResponse({"errno": 3, "msg": "唱片不存在或不归属当前音乐人"})
        album = album_list[0]
        old_song = Song.objects.select_for_update().filter(song_name=payload.get('name'), album=album)
        if len(old_song) == 0:
            return JsonResponse({"errno": 4, "msg": "歌曲不存在"})
        old_song = old_song[0]
        cast_list = [
            ('songLast', 'song_last'),
            ('ADT', 'song_name')
        ]
        for elem in cast_list:
            if payload.get(elem[0]) is not None:
                update_data = {elem[1]: payload.get(elem[0])}
                old_song.update(**update_data)
                old_song.save()
        all_song = Song.objects.filter(album=album)
        all_song = [{"name": song.song_name,
                     "songLength": song.song_last,
                     "ADT": song.resource,
                     "albumID": song.album.id} for song in all_song]
        return JsonResponse({"errno": 0, "msg": "成功",
                             "data": all_song})


def del_song(request):
    if request.method == "POST":
        payload = get_payload(request)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.objects.get(user_id=email)
        musician_list = Musician.objects.filter(user=user)
        if len(musician_list) == 0:
            return JsonResponse({"errno": 2, "msg": "未绑定音乐人信息"})
        musician = musician_list[0]
        album_list = Album.objects.filter(id=payload.get('AID'), musician=musician)
        if len(album_list) == 0:
            return JsonResponse({"errno": 3, "msg": "唱片不存在或不归属当前音乐人"})
        album = album_list[0]
        old_song = Song.objects.filter(song_name=payload.get('SN'), album=album)
        if len(old_song) == 0:
            return JsonResponse({"errno": 4, "msg": "歌曲不存在"})
        old_song = old_song[0]
        old_song.delete()
        all_song = Song.objects.filter(album=album)
        all_song = [{"name": song.song_name,
                     "songLength": song.song_last,
                     "ADT": song.resource,
                     "albumID": song.album.id} for song in all_song]
        return JsonResponse({"errno": 0, "msg": "成功", "data": all_song})


def get_album_tag(request):
    if request.method == "POST":
        payload = get_payload(request)
        aid = payload.get('albumID')
        if aid is None:
            return JsonResponse({"errno": 1, "msg": "该唱片不存在"})
        album = Album.objects.filter(id=aid)
        if len(album) == 0:
            return JsonResponse({"errno": 1, "msg": "该唱片不存在"})
        album = album[0]
        all_tag = AlbumTag.objects.filter(album=album)
        all_tag = [{"SN": tag.tag.tag_name} for tag in all_tag]
        return JsonResponse({"errno": 0, "msg": "成功", "data": all_tag})


def add_del_album_tag(request):
    if request.method == "POST":
        payload = get_payload(request)
        aid = payload.get('AID')
        if aid is None:
            return JsonResponse({"errno": 1, "msg": "该唱片不存在"})
        album = Album.objects.filter(id=aid)
        if len(album) == 0:
            return JsonResponse({"errno": 1, "msg": "该唱片不存在"})
        album = album[0]
        for tag_json in payload['tagList']:
            tag_sel = Tag.objects.filter(tag_name=tag_json['tag'], tag_type=tag_json['tagType'])
            if len(tag_sel) == 0:
                tag_sel = Tag(tag_name=tag_json['tag'], tag_type=tag_json['tagType'], popularity=0)
                tag_sel.save()
            else:
                tag_sel = tag_sel[0]
            old_album_tag = AlbumTag.objects.filter(tag=tag_sel, album=album)
            if len(old_album_tag) == 0:
                continue
            new_album_tag = AlbumTag.objects.filter(tag=tag_sel, album=album)
            tag_sel.popularity += 1
            tag_sel.save()
            new_album_tag.save()
        return JsonResponse({"errno": 0, "msg": "成功"})


def gen_order(request):
    if request.method == "POST":
        payload = get_payload(request)
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.objects.get(user_id=email)
        album = Album.objects.filter(id=payload.get('albumID'))
        if len(album) == 0:
            return JsonResponse({"errno": 2, "msg": "不存在此专辑"})
        album = album[0]
        new_order = Order(consumer=user, album=album, time=datetime.date.today())
        new_order.save()
        return JsonResponse({"errno": 0, "msg": "成功"})


def get_order(request):
    if request.method == "GET":
        email = request.session.get('email')
        if email is None:
            return JsonResponse({"errno": 1, "msg": "未登录"})
        user = User.objects.get(user_id=email)
        order_list = Order.objects.filter(consumer=user)
        order_list = [{"orderNum": order.id, "albumID": order.album.id, "setTime": order.time} for order in
                      order_list]
        return JsonResponse({"errno": 0, "msg": "成功", "orderList": order_list})


def search_tag(request):
    if request.method == "POST":
        payload = get_payload(request)
        select_tag = Tag.objects.filter(tag_name__icontains=payload.get("keyWord"))
        select_musicians = MusicianTag.objects.filter(tag__in=select_tag)
        select_albums = AlbumTag.objects.filter(tag__in=select_tag)
        return_dict = {"errno": 0, "msg": "成功"}
        musician_list = [
            {"musicianID": m.musician.id, "musicianName": m.musician.musician_name, "photo": m.musician.photo} for m
            in
            select_musicians]
        album_list = [{"albumID": a.album.id, "albumName": a.album.album_name, "author": a.album.album_producer,
                       "cover": a.album.cover, "salesVolume": a.album.sales_volume} for a in select_albums]
        return_dict['musicianList'] = musician_list
        return_dict['albumList'] = album_list
        return JsonResponse(return_dict)


def search_musician_album(request):
    if request.method == "POST":
        payload = get_payload(request)
        select_musicians = Musician.objects.filter(musician_name__icontains=payload.get('keyWord'))
        select_albums = Album.objects.filter(album_name__icontains=payload.get('keyWord'))
        return_dict = {"errno": 0, "msg": "成功"}
        musician_list = [
            {"musicianID": m.id, "musicianName": m.musician_name, "photo": m.photo} for m in select_musicians]
        album_list = [{"albumID": a.id, "albumName": a.album_name, "author": a.album_producer, "cover": a.cover,
                       "salesVolume": a.sales_volume} for a in select_albums]
        return_dict['musicianList'] = musician_list
        return_dict['albumList'] = album_list
        return JsonResponse(return_dict)


def get_homepage_info(request):
    if request.method == "GET":
        select_musicians = [Musician.objects.all()[i] for i in
                            random.Random().sample(range(0, Musician.objects.count() - 1), 6)]
        select_tags = [Tag.objects.all()[i] for i in
                       random.Random().sample(range(0, Tag.objects.count() - 1), 6)]
        select_albums = Album.objects.filter().order_by('-sales_volume')[:4]
        musician_list = [
            {"musicianID": m.id, "musicianName": m.musician_name, "photo": m.photo} for m in select_musicians]
        album_list = [{"albumID": a.id, "albumName": a.album_name, "author": a.album_producer, "cover": a.cover,
                       "salesVolume": a.sales_volume} for a in select_albums]
        tag_list = [
            {"tag": t.tag_name, "tagType": t.tag_type} for t in select_tags
        ]
        return_dict = {"errno": 0, "msg": "成功"}
        return_dict['musicianList'] = musician_list
        return_dict['albumList'] = album_list
        return_dict['tagList'] = tag_list
        return JsonResponse(return_dict)
