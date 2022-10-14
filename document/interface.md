接口文档。

## 10/14

/api/login/:
用于登录验证的接口，传入为一序列化的JSON对象，结构为：

```JSON
{
    "email":"dofingert@gmail.com",   #字符串，表示用户的邮箱
    "password":"u7w$m$oab4WGfDy "    #字符串，表示用户的密码，推荐加密后再传输
}
```

传出也为一JSON对象，当失败时，结构为：

```JSON
{
    "errno": 1/2/3,   #非0整数，表示错误类型，具体分配(TODO)
    "msg":"xxx"    #字符串，表示错误信息
}
```

当成功时，结构为：

```JSON
{
    "errno": 0,
    "msg": "登录成功",
    "email":    , #字符串，表示邮箱
    "username": , #字符串，表示用户名
    "avatar":   , #字符串，表示用户头像相关地址（TODO）
    "usertype": , #整型，表示用户类型
    "profile":  , #字符串，表示用户签名
    "password":   #字符串，表示用户密码
}
```

## 10/14

/api/register/:
用于注册账户的接口
传入为一序列化的JSON对象，结构为：

```JSON
{
    "email":"dofingert@gmail.com", #邮箱
    "username":"xxx",              #注册用户昵称
    "useravatar":"",               #用户头像
    "password_1":"",               #用户密码
    "password_2":"",               #用户确认密码
    "usertype":                    #整型，表示用户类型
}
```

无论失败成功，返回为一JSON对象，包含错误码和错误信息

```JSON
{
    "errno": 0/1/2/3,   #整型，表示错误类型，0表示无异常，具体分配(TODO)
    "msg":"xxx"    #字符串，表示错误信息
}
```