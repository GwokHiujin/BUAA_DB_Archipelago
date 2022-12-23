

[TOC]

# 用户

## 用户基本信息

### 关系模式 

| 属性名 | 中文         | 数据类型 | 备注 |
| ------ | ------------ | -------- | ---- |
| UE     | 用户邮箱     | VARCHAR  | 主码 |
| UN     | 用户昵称     | VARCHAR  |      |
| AVT    | 用户头像     | VARCHAR  |      |
| PW     | 用户密码     | VARCHAR  |      |
| UTP    | 用户类型     | INT      |      |
| UB     | 用户个性签名 | TEXT     |      |

### 接口

#### 注册

##### 描述

* 注册一个新的用户账号

##### 请求URL

* ```
  api/register/
  ```

##### 请求方式

* POST

##### 权限要求

无

##### 请求参数（JSON）

~~~
{
	"data": {
		"email": 	  string 必选, 用户注册邮箱
		"name":       string 必选, 用户指定的用户名
		"password_1": string 必选, 用户指定的密码
		"password_2": string 必选, 第二次输入密码，若两次密码不一致，会返回错误
		"type":  integer 必选, 普通用户：0 音乐人用户：1 当指定为音乐人用户时，会自动创建一个音乐人并绑定到当前用户
	}
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:注册成功 1:输入密码不一致 2:邮箱重复注册
	"msg":    string 必选, 返回信息
}
```



#### 登陆

##### 描述

* 登录到一个用户账号

##### 请求URL

* ```
  api/login/
  ```

##### 请求方式

* POST

##### 权限要求

无

##### 请求参数（JSON）

~~~
{
	"data": {
		"email": 	  string 必选, 用户登录邮箱
		"password":   string 必选, 用户登录密码
	}
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:登录成功 2:用户不存在或者密码错误 3:未知错误
	"msg":    string 必选, 返回信息
	
	/ 可选 /
	"data": {
		"email":     string 登录成功时存在, 用户邮箱
		"name":      string 登录成功时存在, 用户名
		"avatar":    string 登录成功时存在, 用户头像
		"type":     integer 登录成功时存在, 用户类型 同注册时填写的
		"bio":       string 登录成功时存在, 用户个性签名
	}
}
```



#### 登出

##### 描述

* 登出已经登录的用户

##### 请求URL

* ```
  api/logoff/
  ```
  

##### 请求方式

* GET

##### 权限要求

- 已经登录

##### 请求参数

无

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:登出成功 1:用户未登录
	"msg":    string 必选, 返回信息
}
```



#### 删除账户

##### 描述

* 删除一个用户账号

##### 请求URL

* ```
  api/delete_account/
  ```

##### 请求方式

* POST

##### 权限要求

无

##### 请求参数（JSON）

~~~
{
	"data": {
		"email": 	  string 必选, 用户登录邮箱
		"password":   string 必选, 用户登录密码
	}
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:删除账户成功 1:用户不存在或者密码错误
	"msg":    string 必选, 返回信息
}
```



#### 获取用户信息

##### 描述

* 获取当前登录的用户信息

##### 请求URL

* ```
  api/get_user_info/
  ```

##### 请求方式

* GET

##### 权限要求

- 已经登录

##### 请求参数

无

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:获取信息成功 1:用户未登录
	"msg":    string 必选, 返回信息

	/ 可选 /
	"data": {
		"email":      string 获取信息成功时, 用户邮箱
		"name":       string 获取信息成功时, 用户名
		"avatar":     string 获取信息成功时, 用户头像
		"type":      integer 获取信息成功时, 用户类型
		"bio": 	      string 获取信息成功时, 用户个性签名
	}
}
```



#### 修改用户信息

##### 描述

* 修改当前登录的用户信息

##### 请求URL

* ```
  api/set_user_info/
  ```

##### 请求方式

* POST

##### 权限要求

- 已经登录

##### 请求参数（JSON）

~~~
{
	"data": {
		"name":        string 可选, 用户指定的新用户名
		"avatar":      string 可选, 用户指定的新头像
		"oldPassword": string 可选, 用户的旧密码
		"password":    string 可选(存在oldPassword才有效), 用户指定的新密码
		"bio":         string 可选, 用户的新签名
	}
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:修改成功 1: 用户未登录 2:旧密码不正确
	"msg":    string 必选, 返回信息
}
```



# 音乐人

## 音乐人基本信息

### 关系模式

| 属性名 | 中文               | 数据类型     | 备注      |
| ------ | ------------------ | ------------ | --------- |
| MID    | 音乐人ID           | UNSIGNED INT | 主码      |
| UE     | 用户邮箱（用户ID） | VARCHAR      | 外键      |
| MN     | 音乐人名称         | VARCHAR      |           |
| PHVAR  | 音乐人照片         | VARCHAR      |           |
| OC     | 音乐人国籍         | VARCHAR      |           |
| LC     | 音乐人城市         | VARCHAR      |           |
| LT     | 音乐人创作主题     | VARCHAR      |           |
| FY     | 音乐人成立年份     | VARCHAR      |           |
| ITD    | 音乐人简介         | VARCHAR      |           |
| FN     | 关注数             | UNSIGNED INT | 初始化为0 |

### 接口

#### 获取所有音乐人信息

##### 描述

* 获取所有的音乐人信息

##### 请求URL

* ```
  api/get_all_musician/
  ```

##### 请求方式

* GET

##### 权限要求

无

##### 请求参数

无

##### 返回参数（JSON）

```
{
	/ 必选 /
	"data": [
		{
			"musicianName":      string 音乐人名称
			"photo":             string 音乐人头像
			"originCountry":     string 音乐人国籍
			"location":          string 音乐人所在地区
			"lyricalThemes": 	 string 音乐人创作主题
			"formedYear": 	     string 音乐人成立年份
			"introduction": 	 string 音乐人介绍
			"followersNum"		integer 音乐人关注数
		}
	]
}
```



#### 获取当前音乐人信息

##### 描述

* 获取当前登录的音乐人信息

##### 请求URL

* ```
  api/get_musician/
  ```

##### 请求方式

* GET

##### 权限要求

- 已经登录，且登录账户已绑定音乐人

##### 请求参数

无

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:获取信息成功 1:用户未登录 2:用户未绑定音乐人信息
	"msg":    string 必选, 返回信息

	/ 可选 /
	"data": {
		"musicianName":      string 可选 获取信息成功时, 音乐人名称
		"photo":             string 可选 获取信息成功时, 音乐人头像
		"originCountry":     string 可选 获取信息成功时, 音乐人国籍
		"location":          string 可选 获取信息成功时, 音乐人所在地区
		"lyricalThemes": 	 string 可选 获取信息成功时, 音乐人创作主题
		"formedYear": 	     string 可选 获取信息成功时, 音乐人成立年份
		"introduction": 	 string 可选 获取信息成功时, 音乐人介绍
		"followersNum": 	integer 可选 获取信息成功时, 音乐人关注数
	}
}
```



#### 获取某音乐人信息

##### 描述

* 获取指定音乐人信息

##### 请求URL

* ```
  api/get_musician/
  ```

##### 请求方式

* POST

##### 权限要求

- 无

##### 请求参数（JSON）

~~~
{
	data: {
		"musicianID": string 必选, 音乐人ID
	} 对象 必选,
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:获取信息成功 1:音乐人不存在
	"msg":    string 必选, 返回信息

	/ 可选 /
	"data": {
		"musicianName":      string 可选 获取信息成功时, 音乐人名称
		"photo":             string 可选 获取信息成功时, 音乐人头像
		"originCountry":     string 可选 获取信息成功时, 音乐人国籍
		"location":          string 可选 获取信息成功时, 音乐人所在地区
		"lyricalThemes": 	 string 可选 获取信息成功时, 音乐人创作主题
		"formedYear": 	     string 可选 获取信息成功时, 音乐人成立年份
		"introduction": 	 string 可选 获取信息成功时, 音乐人介绍
		"followersNum": 	integer 可选 获取信息成功时, 音乐人关注数
	}
}
```



#### 修改音乐人信息

##### 描述

* 修改当前登录的音乐人信息

##### 请求URL

* ```
  api/set_musician/
  ```

##### 请求方式

* POST

##### 权限要求

- 已经登录，且当前登录账户已绑定音乐人

##### 请求参数（JSON）

~~~
{
	"data": {
		"musicianName":      string 可选, 音乐人名称（修改后）
		"photo":             string 可选, 音乐人头像（修改后）
		"originCountry":     string 可选, 音乐人国籍（修改后）
		"location":          string 可选, 音乐人所在地区（修改后）
		"lyricalThemes": 	 string 可选, 音乐人创作主体（修改后）
		"formedYear": 	     string 可选, 音乐人成立年份（修改后）
		"introduction": 	 string 可选, 音乐人介绍（修改后）
	}
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:修改成功 1: 未登录 2:未绑定音乐人信息
	"msg":    string 必选, 返回信息
}
```



## 音乐人成员

### 关系模式

| **属性名** | **中文**  | **数据类型** | **备注**   |
| ---------- | --------- | ------------ | ---------- |
| N          | 姓名      | VARCHAR      | 主码       |
| BD         | 生日      | VARCHAR      |            |
| RL         | 职务/角色 | VARCHAR      |            |
| AY         | 活动年份  | VARCHAR      |            |
| MID        | 音乐人ID  | UNSIGNED INT | 主码，外码 |

### 接口

#### 获取音乐人成员

##### 描述

* 获取某音乐人的所有音乐人成员

##### 请求URL

* ```
  api/get_musician_member/
  ```

##### 请求方式

* POST

##### 权限要求

- 无

##### 请求参数（JSON）

~~~
{
	data: {
		"musicianID": string 必选, 音乐人ID
	} 对象 必选,
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:成功 1:音乐人不存在
	"msg":    string 必选, 返回信息
	
	/ 可选 /
	"data": [
		{
			"name":  string 必选, 音乐人成员名称
			"birthday": string 必选, 音乐人成员生日
			"role": string 必选, 音乐人成员乐队角色
			"activeYear": string 必选, 音乐人成员活跃年份
		}, 重复n次 可为空
	] 数组对象 可选 成功时存在,  包含当前音乐人的所有成员
}
```



#### 添加音乐人成员

##### 描述

* 添加音乐人成员到音乐人

##### 请求URL

* ```
  api/add_musician_member/
  ```

##### 请求方式

* POST

##### 权限要求

- 已经登录，且当前登录账户已绑定音乐人

##### 请求参数（JSON）

~~~
{
	data: {
		"musicianID": string 必选, 音乐人ID
		"name":   string 必选, 音乐人成员名称
		"birthday":  string 必选, 音乐人生日
		"role":  string 必选, 音乐人乐队角色
		"activeYear":  string 必选, 音乐人活跃年份
	} 对象 必选,
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:成功 1: 未登录 2:未绑定音乐人信息 3:音乐人绑定信息不符 4:成员重复
	"msg":    string 必选, 返回信息
	
	/ 可选 /
	"data": [
		{
			"name":  string 必选, 音乐人成员名称
			"birthday": string 必选, 音乐人成员生日
			"role": string 必选, 音乐人成员乐队角色
			"activeYear": string 必选, 音乐人成员活跃年份
		}, 重复n次 可为空
	] 数组对象 可选 成功时存在,  包含当前音乐人的所有成员
}
```



#### 修改音乐人成员

##### 描述

* 修改当前登录的音乐人的某个音乐人成员信息

##### 请求URL

* ```
  api/set_musician_member/
  ```

##### 请求方式

* POST

##### 权限要求

- 已经登录，且当前登录账户已绑定音乐人

##### 请求参数（JSON）

~~~
{
	data: {
		"name":  string 必选, 待修改信息的音乐人成员名称（名字不可改，改名字相当于删除该成员）
		"birthday": string 可选, 音乐人成员生日（修改后）
		"role": string 可选, 音乐人成员乐队角色（修改后）
		"activeYear": string 可选, 音乐人成员活跃年份（修改后）
	} 对象 必选,
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:成功 1: 未登录 2:未绑定音乐人信息 3:音乐人绑定信息不符 4:成员不存在
	"msg":    string 必选, 返回信息
	
	/ 可选 /
	"data": [
		{
			"name":  string 必选, 音乐人成员名称
			"birthday": string 必选, 音乐人成员生日
			"role": string 必选, 音乐人成员乐队角色
			"activeYear": string 必选, 音乐人成员活跃年份
		}, 重复n次 可为空
	] 数组对象 可选 成功时存在,  包含当前音乐人的所有成员
}
```



#### 删除音乐人成员

##### 描述

* 删除当前登录的音乐人的某个音乐人成员信息

##### 请求URL

* ```
  api/del_musician_member/
  ```

##### 请求方式

* POST

##### 权限要求

- 已经登录，且当前登录账户已绑定音乐人

##### 请求参数（JSON）

~~~
{
	data: {
		"name":  string 必选, 待删除音乐人成员名称
	} 对象 必选,
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:成功 1: 未登录 2:未绑定音乐人信息 3:音乐人绑定信息不符 4:成员不存在
	"msg":    string 必选, 返回信息
	
	/ 可选 /
	"data": [
		{
			"name":  string 必选, 音乐人成员名称
			"birthday": string 必选, 音乐人生日
			"role": string 必选, 音乐人乐队角色
			"activeYear": string 必选, 音乐人活跃年份
		}, 重复n次 可为空
	] 数组对象 可选 成功时存在,  包含当前音乐人的所有成员
}
```



## 音乐人标签

### 关系模式

| **属性名** | **中文** | **数据类型** | **备注** |
| ---------- | -------- | ------------ | -------- |
| SN         | 标签名称 | VARCHAR      | 主码     |
| ST         | 标签类型 | INT          | 主码     |
| SP         | 标签热度 | UNSIGNED INT |          |



## 音乐人-音乐人标签

### 关系模式

| **属性名** | **中文** | **数据类型** | **备注**     |
| ---------- | -------- | ------------ | ------------ |
| MID        | 音乐人ID | UNSIGNED INT | 唯一主码属性 |
| SN         | 标签名称 | VARCHAR      | 外码的属性   |
| ST         | 标签类型 | INT          | 外码的属性   |

### 接口

#### 获取音乐人的TAG

##### 描述

* 获取某音乐人的TAG

##### 请求URL

* ```
  api/get_musician_tag/
  ```

##### 请求方式

* POST

##### 权限要求

无

##### 请求参数（JSON）

~~~
{
	"data": {
		"musicianId":  integer 必选, 音乐人ID
	}
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:获取信息成功 1:该音乐人不存在
	"msg":    string 必选, 返回信息

	/ 可选 /
	"data": [
		{
			"tag":  string 必选, 音乐人标签名
		}, 重复n次 可为空
	] 数组对象 可选 成功时候存在, 音乐人的所有标签信息
}
```



#### 添加或删除音乐人的TAG

##### 描述

* 添加或删除某音乐人的 TAG ，对于某一 TAG 和某一音乐人，若音乐人已拥有此 TAG，使用此方法会删除该TAG，否之，TAG会被添加到音乐人上。
* 此方法的副作用：当 TAG 被添加时，TAG的热度会增加一，被删除时，会减少一。若是未使用过的 TAG，TAG会被自动创建并初始化热度为一；若TAG热度减为0，则TAG会被自动从TAG表中删除。

##### 请求URL

* ```
  api/get_musician_tag/
  ```

##### 请求方式

* POST

##### 权限要求

无

##### 请求参数（JSON）

~~~
{
	data: {
		"musicianID":  integer 必选, 音乐人ID
		"tagList": 
		[
			{
				"tag":    string 必选, TAG名
				"tagType":   integer 必选, TAG类型
			}
		] 重复n次，可为空
		
	} 对象 必选,
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:添加或者删除音乐人标签成功 1:该音乐人不存在 2：2：添加的TAG重复
	"msg":    string 必选, 返回信息
}
```



# 唱片

## 歌曲

### 关系模式

| **属性名** | **中文** | **数据类型** | **备注**   |
| ---------- | -------- | ------------ | ---------- |
| SN         | 歌曲名称 | VARCHAR      | 主码       |
| SL         | 歌曲时长 | INT          |            |
| ADT        | 试听链接 | VARCHAR      |            |
| AID        | 唱片ID   | UNSIGNED INT | 主码，外码 |

### 接口

#### 添加歌曲

##### 描述

* 为某唱片添加歌曲

##### 请求URL

* ```
  api/add_song/
  ```

##### 请求方式

* POST

##### 权限要求

- 已经登录，且当前账户为音乐人账户

##### 请求参数（JSON）

~~~
{
	"data": {
		"albumID": integer 必选, 唱片ID, 歌曲将被添加到此唱片
		"name":   string 必选, 待添加的歌曲名
		"songLast":  integer 必选, 歌曲时长(秒)
		"ADT":  string 必选, 歌曲试听链接 TODO: 全称是？
	} 对象 必选, 当前音乐人拥有的所有歌曲
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:添加成功 1:未登录 2:未绑定音乐人 3:无此唱片或唱片不属于用户 4:歌曲重复
	"msg":    string 必选, 返回信息
	
	/ 可选 /
	"data": [
		{
			"name":  string 必选, 歌曲名
			"songLast": integer 必选, 歌曲时长
			"ADT": string 必选, 歌曲试听链接
			"albumID": integer 必选, 唱片ID
		},
	] 数组对象 可选 成功时存在, 当前唱片拥有的所有歌曲
}
```



#### 修改歌曲信息

##### 描述

* 为某唱片修改歌曲

##### 请求URL

* ```
  api/set_song/
  ```

##### 请求方式

* POST

##### 权限要求

- 已经登录，且当前账户为音乐人账户

##### 请求参数（JSON）

~~~
{
	"data": {
		"albumID": integer 必选, 唱片ID, 待修改的歌曲所在唱片
		"name":   string 必选, 待修改的歌曲名
		"songLast":  integer 可选, 歌曲时长（秒，修改后）
		"ADT":  string 可选, 歌曲试听链接（修改后）
	} 对象 必选, 当前音乐人拥有的所有歌曲
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:添加成功 1:未登录 2:未绑定音乐人 3:无此唱片或唱片不属于用户 4:歌曲不存在
	"msg":    string 必选, 返回信息
	
	/ 可选 /
	"data": [
		{
			"name":   string 必选, 歌曲名
			"songLast":  integer 必选, 歌曲时长
			"ADT":  string 必选, 歌曲试听链接
			"albumID": integer 必选, 唱片ID
		},
	] 数组对象 可选 成功时存在, 当前音乐人拥有的所有歌曲
}
```



#### 删除歌曲

##### 描述

* 删除歌曲

##### 请求URL

* ```
  api/del_song/
  ```

##### 请求方式

* POST

##### 权限要求

- 已经登录，且当前账户为音乐人账户

##### 请求参数（JSON）

~~~
{
	"data": {
		"albumID": integer 必选, 唱片ID, 待删除的歌曲所在唱片
		"name":   string 必选, 待删除的歌曲名
	} 对象 必选, 当前音乐人拥有的所有歌曲
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:添加成功 1:未登录 2:未绑定音乐人 3:无此唱片或唱片不属于用户 4:歌曲不存在
	"msg":    string 必选, 返回信息
	
	/ 可选 /
	"data": [
		{
			"name":   string 必选, 歌曲名
			"songLast":  integer 必选, 歌曲时长
			"ADT":  string 必选, 歌曲试听链接
			"albumID": integer 必选, 唱片ID
		},
	] 数组对象 可选 成功时存在, 当前唱片在修改后拥有的所有歌曲
}
```



## 唱片基本信息

### 关系模式

| 属性名 | 中文       | 数据类型     | 备注           |
| ------ | ---------- | ------------ | -------------- |
| AID    | 唱片ID     | UNSIGNED INT | 系统自增，主码 |
| AN     | 唱片名称   | VARCHAR      |                |
| AP     | 唱片定价   | INT          |                |
| AU     | 唱片创作者 | VARCHAR      |                |
| MID    | 唱片发布者 | VARCHAR      | 外键           |
| RY     | 发行年份   | VARCHAR      |                |
| AC     | 唱片封面   | VARCHAR      |                |
| TYP    | 唱片类型   | INT          |                |
| SRC    | 资源链接   | VARCHAR      |                |
| SV     | 唱片销量   | INT          |                |

### 接口

#### 获取某音乐人的唱片信息

##### **描述**

- 获取某音乐人的全部唱片基本信息列表

##### **请求URL**	    

- ```
  api/get_album/
  ```

##### **请求方式**

- POST

##### **权限要求**

无

##### **请求参数（JSON）**

```
{	
	"data": {
		"musicianID":  integer 必选, 音乐人ID
		"musicianName": string 可选（搜索时），音乐人名称
	}
}
```

##### **返回参数（JSON）**

```
{	
	/ 必选 /
	"errno": integer 必选, 0:获取信息成功 1:该音乐人不存在
	"msg":    string 必选, 返回信息
	
	/ 可选 /
	"albumList": [
		{
			"albumID":     integer 必选, 唱片ID
			"albumName":    string 必选, 唱片名
			"price":        string 必选, 唱片价格
			"author":       string 必选, 唱片创作者
			"releaseYear":  string 必选, 发行年份
			"releaser":     string 必选, 发行方
			"cover":        string 必选，封面 
			"type":        integer 必选, 唱片类型
			"resource":     string 必选, 唱片资源链接
			"salesVolume": integer 必选, 唱片销量
		}, 多个dict object 可为空
	] 数组对象 成功时候存在, 目标音乐人的所有唱片信息
}

```



#### 获取某一唱片的信息

##### **描述**

- 获取某一唱片基本信息及其歌曲信息列表

##### **请求URL**	    

- ```
  api/get_album_info/
  ```

##### **请求方式**

- POST

##### **权限要求**

无

##### **请求参数（JSON）**

```
{
	"data": {
		"albumID":    integer 必选, 唱片ID
		“albumName”:   string 可选（搜索时），唱片名
		"releaser":    string 可选（搜索时）, 唱片发布者名称
		"musicianID":  string 可选，唱片的发布者ID
	} 
}
```

##### **返回参数（JSON）**

```
{
	/ 必选 /
	"errno": integer 必选, 0:获取信息成功 1:该唱片不存在
	"msg":    string 必选, 返回信息
	
	/ 可选 /
	"generalInfo": {
		"albumID":     integer 必选, 唱片ID
		"albumName":    string 必选, 唱片名
		"price":        string 必选, 唱片价格
		"author":       string 必选, 唱片创作者
		"releaseYear":  string 必选, 发行年份
		"releaser":     string 必选, 发行方
		"cover":        string 必选，封面 
		"type":        integer 必选, 唱片类型
		"resource":     string 必选, 唱片资源链接
		"salesVolume": integer 必选， 唱片销量
	}, 多个dict object 可选 成功时存在，可为空
	
 	"songList": [
		{
			"name":   string 必选, 歌曲名
			"songLast":  integer 必选, 歌曲时长
			"ADT":  string 必选, 歌曲试听链接
			"albumID": integer 必选, 唱片ID
		},
	] 数组对象 可选 成功时存在, 目标唱片拥有的所有歌曲  
}
```



#### 获取当前音乐人的唱片信息

##### 描述

* 获取当前音乐人的所有唱片

##### 请求URL

* ```
  api/get_album/
  ```

##### 请求方式

* GET

##### 权限要求

- 无

##### 请求参数

无

##### 返回参数（JSON）

```
[
	{
		"albumID":     integer 必选, 唱片ID
		"albumName":    string 必选, 唱片名
		"price":        string 必选, 唱片价格
		"author":       string 必选, 唱片创作者
		"releaseYear":  string 必选, 发行年份
		"releaser":     string 必选, 发行方
		"cover":        string 必选，封面 
		"type":        integer 必选, 唱片类型
		"resource":     string 必选, 唱片资源链接
		"salesVolume": integer 必选， 唱片销量
	}, 多个dict object 可为空
]
```



#### 修改/添加当前音乐人的唱片信息

##### 描述

* 修改当前音乐人的唱片信息

##### 请求URL

* ```
  api/set_album/
  ```

##### 请求方式

* POST

##### 权限要求

- 已经登录，且当前账户为音乐人账户

##### 请求参数（JSON）

~~~
{
	"data": {
		"Tag":         integer 必选, 待修改的唱片id 若为-1表示新唱片 待添加
		"albumName":    string 可选, 唱片名
		"price":        string 可选, 唱片价格
		"author":       string 可选, 唱片创作者
		"releaseYear":  string 可选, 发行年份
		"cover":        string 可选，封面 
		"type":        integer 可选, 唱片类型
		"resource":     string 可选, 唱片资源链接
	}
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:添加/修改成功 1:未登录 2:当前账户未绑定音乐人 3:无此唱片或唱片不属于用户
	"msg":    string 必选, 返回信息
}
```



#### 删除当前音乐人的某唱片

##### 描述

* 修改当前音乐人的唱片信息

##### 请求URL

* ```
  api/del_album/
  ```

##### 请求方式

* POST

##### 权限要求

- 已经登录，且当前账户为音乐人账户

##### 请求参数（JSON）

~~~
{
	"data": {
		"Tag":        integer 必选, 待删除的唱片id
	}
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:修改成功 1:唱片不存在 2:当前账户未绑定音乐人 3:唱片不属于用户
	"msg":    string 必选, 返回信息
}
```



## 唱片标签

### 关系模式

| **属性名** | **中文** | **数据类型** | **备注**   |
| ---------- | -------- | ------------ | ---------- |
| SN         | 标签名称 | VARCHAR      | 主码的属性 |
| ST         | 标签类型 | INT          | 主码的属性 |
| SP         | 标签热度 | UNSIGNED INT |            |



## 唱片-唱片标签

### 关系模式

| **属性名** | **中文** | **数据类型** | **备注**     |
| ---------- | -------- | ------------ | ------------ |
| AID        | 唱片ID   | UNSIGNED INT | 唯一主码属性 |
| SN         | 标签名称 | VARCHAR      | 外码的属性   |
| ST         | 标签类型 | INT          | 外码的属性   |

### 接口

#### 获取唱片的TAG

##### 描述

* 获取某唱片的TAG

##### 请求URL

* ```
  api/get_album_tag/
  ```

##### 请求方式

* POST

##### 权限要求

无

##### 请求参数（JSON）

~~~
{
	"data": {
		"albumID":  integer 必选, 唱片ID
	}
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:获取信息成功 1:该唱片不存在
	"msg":    string 必选, 返回信息

	/ 可选 /
	"data": [
		{
			"tag":  string 必选, 唱片标签名
		}, 重复n次 可为空
	] 数组对象 可选 成功时候存在, 唱片的所有标签信息
}
```



#### 添加或删除唱片的TAG

##### 描述

* 添加或删除某唱片的 TAG ，对于某一 TAG 和某一唱片，若唱片已拥有此 TAG，使用此方法会删除该TAG，否之，TAG会被添加到唱片上。
* 此方法的副作用：当 TAG 被添加时，TAG的热度会增加一，被删除时，会减少一。若是未使用过的 TAG，TAG会被自动创建并初始化热度为一；若TAG热度减为0，则TAG会被自动从TAG表中删除。

##### 请求URL

* ```
  api/add_del_album_tag/
  ```

##### 请求方式

* POST

##### 权限要求

无

##### 请求参数（JSON）

~~~
{
	data: {
		"musicianID":  integer 必选, 音乐人ID
		"tagList": 
		[
			{
				"tag":    string 必选, TAG名
				"tagType":   integer 必选, TAG类型
			}
		] 重复n次，可为空
		
	} 对象 必选,
}
~~~

##### 返回参数（JSON）

```
{
	/ 必选 /
	"errno": integer 必选, 0:添加或删除唱片的TAG成功 1:该唱片不存在 2：添加的TAG重复
	"msg":    string 必选, 返回信息
}
```



# 订单

### 关系模式

| 属性名 | 中文         | 数据类型     | 备注           |
| ------ | ------------ | ------------ | -------------- |
| ON     | 订单编号     | UNSIGNED INT | 主码，系统自增 |
| UE     | 客户ID       | VARCHAR      | 外键           |
| AID    | 唱片ID       | UNSIGNED INT | 外键           |
| ST     | 订单创建时间 | DATETIME     |                |

### 接口

#### 生成订单信息

**描述**

- 用户完成购买生成订单信息
- 此方法的副作用：购买的唱片销量加1

**请求URL**

- ```
  api/gen_order/
  ```

**请求方式**

- POST

##### 权限要求

- 已经登录

**请求参数（JSON）**

```
{
	"data":{
		"albumID": integer 必选, 购买的唱片ID
	}
} 默认后端系统自增生成订单ID，自动检测购买时间，根据当前登录用户获得购买者ID
```

**返回参数（JSON）**

```
{
	/ 必选 /
	"errno": integer 必选, 0:购买成功 1:用户未登录 
	"msg":    string 必选, 返回信息
}
```



#### 查询订单信息

**描述**

- 用户查询自身全部订单信息

**请求URL**

- ```
  api/get_order/
  ```

**请求方式**

- GET

##### 权限要求

- 已经登录

**请求参数（JSON）**

无

**返回参数（JSON）**

```
{
	/ 必选 /
	"errno": integer 必选, 0:获取订单信息成功 1:用户未登录 
	"msg":    string 必选, 返回信息
	
	"orderList": [
		{
			"orderNum": integer 必选, 订单编号
			"albumID":  integer 必选, 购买的唱片ID
			"setTime":          必选, 订单创建时间    
		}, 重复n次 可为空
	] 数组对象 可选 成功时候存在, 当前用户的全部订单信息
}
```



# 搜索

### 接口

#### 标签搜索

**描述**

- 获取名字符合关键词的音乐人标签或者唱片标签

**请求URL**

- ```
  api/search_tag/
  ```

**请求方式**

- POST

##### 权限要求

- 无

**请求参数（JSON）**

```
{
	“data": {
		"keyWord": string 必选, 标签关键词
	}
} 
```

**返回参数（JSON）**

```
{
	/ 必选 /
	"errno": integer 必选, 0:搜索成功 1:未知错误 
	"msg":    string 必选, 返回信息

	/ 可选 /
	"musicianList"： [
		{
			"musicianID":    integer 音乐人ID
			"musicianName":   string 音乐人名称
			"photo":          string 音乐人头像   
		}, 重复n次 可为空    
	] 数组对象 可选 搜索音乐人标签成功时候存在, 贴有符合关键词标签的音乐人列表
	
	/ 可选 /
	"albumList": [
		{
			"albumID":      integer 必选, 唱片ID
			"albumName":     string 必选, 唱片名
			"author":        string 必选, 唱片创作者
			"cover":         string 必选，封面 
			"salesVolume":  integer 必选, 唱片销量
		}, 重复n次 可为空
	] 数组对象 搜索唱片标签成功时候存在, 贴有符合关键词标签的唱片列表
}
```

### 接口

#### 音乐人或唱片搜索

**描述**

- 获取名称符合关键词的音乐人或唱片

**请求URL**

- ```
  api/search_musician_album/
  ```

**请求方式**

- POST

##### 权限要求

- 无

**请求参数（JSON）**

```
{
	“data": {
		"keyWord": string 必选, 标签关键词
	}
} 
```

**返回参数（JSON）**

```
{
	/ 必选 /
	"errno": integer 必选, 0:搜索成功 1:未知错误 
	"msg":    string 必选, 返回信息

	/ 可选 /
	"musicianList"： [
		{
			"musicianID":    integer 音乐人ID
			"musicianName":   string 音乐人名称，与搜索关键词匹配
			"photo":          string 音乐人头像   
		}, 重复n次 可为空    
	] 数组对象 可选 成功时候存在, 贴有符合关键词标签的音乐人列表
	
	/ 可选 /
	"albumList": [
		{
			"albumID":      integer 必选, 唱片ID
			"albumName":     string 必选, 唱片名，与搜索关键词匹配
			"author":        string 必选, 唱片创作者
			"cover":         string 必选，封面 
			"salesVolume":  integer 必选, 唱片销量
		}, 重复n次 可为空
	] 数组对象 成功时候存在, 贴有符合关键词标签的唱片列表
}
```



# 显示

### 接口

#### 获取首页信息

**描述**

- 首页显示时使用
- 获取销量最高的4个唱片的部分信息
- 随机获取6个音乐人的部分信息
- 随机获取6个标签的部分信息

**请求URL**

- ```
  api/get_homepage_info/
  ```

**请求方式**

- GET

##### 权限要求

- 无

**返回参数（JSON）**

```
{
	/ 必选 /
	"errno": integer 必选, 0:获取信息成功 1:未知错误 
	"msg":    string 必选, 返回信息

	/ 必选 /
	"musicianList"： [
		{
			"musicianID":    integer 音乐人ID
			"musicianName":   string 音乐人名称
			"photo":          string 音乐人头像 
            "introduction":   string 音乐人简介
		}, 重复6次 可为空    
	] 数组对象 获取音乐人信息成功时候存在, 音乐人信息列表
	
	/ 必选 /
	"albumList": [
		{
			"albumID":      integer 必选, 唱片ID
			"albumName":     string 必选, 唱片名，与搜索关键词匹配
			"author":        string 必选, 唱片创作者
			"cover":         string 必选，封面 
			"tagList": [            必选，唱片的标签列表
				{
					"tag":   string 必选, 标签名
				}, 重复n次 可为空
			]
		}, 重复4次 可为空
	] 数组对象 获取唱片信息成功时候存在, 唱片信息列表
	
	/ 必选 /
	"tagList"： [
		{
			"tag":           string 必选, 标签名
			"tagType":      integer 必选, 标签类型
		}, 重复6次 可为空    
	] 数组对象 获取标签信息成功时候存在, 标签信息列表	
}
```



# 评论

### 关系模式

| 属性名 | 中文         | 数据类型     | 备注           |
| ------ | ------------ | ------------ | -------------- |
| CID    | 评论ID       | UNSIGNED INT | 主码，系统自增 |
| UE     | 评论用户ID   | VARCHAR      | 外键           |
| AID    | 唱片ID       | UNSIGNED INT | 外键           |
| ST     | 评论创建时间 | DATETIME     |                |
| CC     | 评论内容     | VARCHAR      |                |
| LC     | 点赞数       | UNSIGNED INT |                |

### 接口

#### 创建评论

**描述**

- 用户发布评论时创建评论

**请求URL**

- ```
  TODO
  ```

**请求方式**

- POST

##### 权限要求

- 已经登录

**请求参数（JSON）**

```
{
	"data":{
		"albumID": 	  integer 必选，被评论的唱片ID
		"comment":    string  必选，评论内容
	}
} 默认后端系统自增生成评论ID，自动检测评论时间，根据当前登录用户获得评论者ID
```

**返回参数（JSON）**

```
{
	/ 必选 /
	"errno": integer 必选, 0:评论成功 1:用户未登录 
	"msg":    string 必选, 返回信息
}
```



#### 获取唱片评论

**描述**

- 获取某唱片的全部评论

**请求URL**

- ```
  TODO
  ```

**请求方式**

- GET

##### 权限要求

- 无

**请求参数（JSON）**

```
{
	"data":{
		"albumID": 	  integer 必选，被评论的唱片ID
	}
} 
```

**返回参数（JSON）**

```
{
	/ 必选 /
	"errno": integer 必选, 0:获取评论成功 1:未知错误 
	"msg":    string 必选, 返回信息
	
	"commentList": [
		{
			"comment":  string  必选，评论内容
			"UE":  		integer 必选, 评论者的ID
			"setTime":          必选, 评论创建时间    
		}, 重复n次 可为空
	] 数组对象 可选 成功时候存在, 某唱片的全部评论
}
```

## 

# 关注

### 关系模式

| 属性名 | 中文             | 数据类型     | 备注           |
| ------ | ---------------- | ------------ | -------------- |
| FID    | 关注ID           | UNSIGNED INT | 主码，系统自增 |
| UE     | 关注用户ID       | VARCHAR      | 外键           |
| MID    | 被关注的音乐人ID | UNSIGNED INT | 外键           |
| FT     | 关注时间         | DATETIME     |                |

### 接口

#### 产生或取消关注

**描述**

- 用户关注音乐人或者取消关注音乐人
- 此方法的副作用：当用户产生关注时时，MID对应的音乐人的关注数增加一，用户取消关注时时，会减少一。MID对应的音乐人的关注数初始化为0，且最小为0

**请求URL**

- ```
  TODO
  ```

**请求方式**

- POST

##### 权限要求

- 已经登录

**请求参数（JSON）**

```
{
	"data":{
		"musicianID": integer 必选, 被关注的音乐人ID
	}
} 默认后端根据当前登录用户获得当前登录用户ID
```

**返回参数（JSON）**

```
{
	/ 必选 /
	"errno": integer 必选, 0:关注成功 1:用户未登录 
	"msg":    string 必选, 返回信息
}
```



#### 获取关注列表

**描述**

- 获取当前登录用户的关注音乐人列表

**请求URL**

- ```
  TODO
  ```

**请求方式**

- GET

##### 权限要求

- 已经登录

**请求参数（JSON）**

- 无（默认后端根据当前登录用户获得当前登录用户ID）

**返回参数（JSON）**

```
{
	/ 必选 /
	"errno": integer 必选, 0:获取关注列表成功 1:未知错误 
	"msg":    string 必选, 返回信息
	
	"concernList": [
		{
			"musicianID":   integer 必选，音乐人ID
			"musicianName":  string 必选，音乐人名称   
			"avatar":        string 必选，音乐人头像
		}, 重复n次 可为空
	] 数组对象 可选 成功时候存在, 某用户关注的全部音乐人列表
}
```



#### 存在关注

**描述**

- 判断某音乐人是否在当前登录用户的关注列表里，取消关注的辅助接口
- 若不存在，可用于取消关注

**请求URL**

- ```
  TODO
  ```

**请求方式**

- POST

##### 权限要求

- 已经登录

**请求参数（JSON）**

```
{
	"data":{
		"musicianID": integer 必选, 音乐人ID
	}
} 默认后端根据当前登录用户获得当前登录用户ID
```

**返回参数（JSON）**

```
{
	/ 必选 /
	"errno":       integer 必选, 0:判断成功 1:用户未登录 
	"msg":          string 必选 返回信息
	
	"data": {
		"exist":   boolean 可选 判断成功时, 音乐人是否在当前登录用户的关注列表里
	}
}
```

