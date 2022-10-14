<template>
  <div>
    <div class="sider">
      <el-aside width="250px">
        <BaseSide/>
      </el-aside>
    </div>
    <div class="main">
      <div class="container">
        <div class="form-box">
          <div class="register-box hidden">
            <h1>register</h1>
            <input type="text" placeholder="用户名" id="un1">
            <input type="email" placeholder="邮箱" id="email1">
            <input type="password" placeholder="密码" id="pw1">
            <input type="password" placeholder="确认密码" id="pw2" @keyup.enter="toRegister">
            <el-radio-group v-model="utype" class="ml-4">
              <el-radio label="0" size="large">我是听众</el-radio>
              <el-radio label="1" size="large">我是音乐人</el-radio>
            </el-radio-group>
            <button @click="toRegister()">确认注册</button>
          </div>
          <div class="login-box">
            <h1>login</h1>
            <input type="email" placeholder="邮箱" id="email2">
            <input type="password" placeholder="密码" id="pw" @keyup.enter="toLogin">
            <button @click="toLogin()">登录</button>
          </div>
        </div>
        <div class="con-box left">
          <h2>欢迎您<span>注册</span></h2>
          <img src="../../assets/img/register.png" alt="加载失败">
          <p>已有账号</p>
          <button id="login">去登录</button>
        </div>
        <div class="con-box right">
          <h2>欢迎您<span>登陆</span></h2>
          <img src="../../assets/img/login.png" alt="加载失败">
          <p>没有账号？</p>
          <button id="register">去注册</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import qs from "qs";
axios.defaults.withCredentials = true;

export default {
  name: 'LoginAndRegister',
  data() {
    return {
      utype: "0",
    }
  },
  components: {
  },
  mounted() {
    this.initPage()
  },
  methods: {

    toLogin: function () {
      let params;
      let tempthis = this;
      params = {
        email: document.getElementById('email2').value,
        password: document.getElementById('pw').value
      };
      this.axios({
        method: 'post',
        url: "login/login/", //暂定
        data: qs.stringify(params)
      })
      .then(res => {
        console.log(res.data)
        if(res.data.errno === 0) {

          this.$store.state.userInfo.email = res.data.email; //邮箱
          this.$store.state.userInfo.username = res.data.username; //用户昵称
          this.$store.state.userInfo.avatar = res.data.avatar; //头像地址
          this.$store.state.userInfo.usertype = res.data.usertype //用户类型
          this.$store.state.userInfo.profile = res.data.profile //用户简介
          this.$store.state.userInfo.password = res.data.password //用户密码
          this.$store.state.isLogin = true;

          this.$message({
            message: '登陆成功',
            type: 'success',
            showClose: true,
          })
          tempthis.isLogin = true;
          this.$router.push('/');


        } else {
          this.$message({
            message: res.data.msg,
            type: 'error',
            showClose: true,
          })
        }

      })
      .catch(err => {
        console.log(err)
      })
    },
    toRegister: function (){
      let params;
      params = {
        username: document.getElementById('un1').value,
        email: document.getElementById('email1').value,
        password_1: document.getElementById('pw1').value,
        password_2: document.getElementById('pw2').value,
        usertype: this.utype
      };
      console.log(params);
      this.axios({
        method: 'post',
        url: "login/register/", //待定
        data: qs.stringify(params)
      })
      .then(res => {
        console.log(res.data)
        if(res.data.errno === 0) {

          //this.$store.state.uid = res.data.uid;
          //this.$store.state.userInfo.username = user.username;
          //this.$store.state.isLogin = true;
          this.$message({
            message: '注册成功',
            type: 'success',
            showClose: true,
          })
          location.reload();

        } else {
          if(res.data.msg === '密码格式错误' ) {
            this.$message({
              message: res.data.msg+':必须包含字母和数字，且长度在8和18之间',
              type: 'error',
              showClose: true,
            })
          }
          else {
            this.$message({
              message: res.data.msg,
              type: 'error',
              showClose: true,
            })
          }
        }

      })
      .catch(err => {
        console.log(err)
      })
    },
    initPage() {
      let login=document.getElementById('login');
      let register=document.getElementById('register');
      let form_box=document.getElementsByClassName('form-box')[0];
      let register_box=document.getElementsByClassName('register-box')[0];
      let login_box=document.getElementsByClassName('login-box')[0];
      register.addEventListener('click',()=>{
        form_box.style.transform='translateX(100%)';
        login_box.classList.add('hidden');
        register_box.classList.remove('hidden');
      })
      login.addEventListener('click',()=>{
        form_box.style.transform='translateX(0%)';
        register_box.classList.add('hidden');
        login_box.classList.remove('hidden');
      })
    }
  }
}
</script>
<style scoped>
/* 把单选框隐藏 */
input[type="radio"] {
  display: none;
}

.radio-box {

}

/* 自定义单选框初始样式 */
.radio {
  display: inline-block;
  position: relative;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  border: 2px solid #777;
  vertical-align: -4px;
}
/* 自定义单选框选中样式 初始隐藏*/
.radio::after {
  content: "";
  width: 10px;
  height: 10px;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
  background-color: #299;
  border-radius: 50%;
  display: none;
}
/* 显示自定义单选框 */
input[type="radio"]:checked+.radio::after {
  display: block;
}
/* 切换自定义单选框border颜色 */
input[type="radio"]:checked+.radio {
  border-color: #299;
}

/* 选中时，文本加颜色 */
input[type="radio"]:checked~.item {
  color: #199;
}

.sider{
  /* 100%窗口高度 */
  height: 100vh;
  width: 18%;
  /* 弹性布局 水平+垂直居中 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  float: left;
  /* 渐变背景 */
  /*background: linear-gradient(200deg,#f3e7e9,#e3eeff);*/
  top: 0px;
  left: 0px;
}

.main{
  /* 100%窗口高度 */
  height: 100vh;
  width: 82%;
  /* 弹性布局 水平+垂直居中 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* 渐变背景 */
  background: linear-gradient(200deg,#f3e7e9,#e3eeff);
  top: 0px;
  left: 0px;
}
.container{
  background-color: #fff;
  width: 750px;
  height: 515px;
  border-radius: 5px;
  /* 阴影 */
  box-shadow: 5px 5px 5px rgba(0,0,0,0.1);
  /* 相对定位 */
  position: relative;

}
.form-box{
  /* 绝对定位 */
  position: absolute;
  background-color: #79c5ef;
  width: 375px;
  height: 515px;
  border-radius: 5px;
  box-shadow: 2px 0 10px rgba(0,0,0,0.1);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
  /* 动画过渡 加速后减速 */
  transition: 0.5s ease-in-out;
}
.register-box,.login-box{
  /* 弹性布局 垂直排列 */
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}
.hidden{
  display: none;
  transition: 0.5s;
}
h1{
  text-align: center;
  margin-bottom: 25px;
  font-size: 28px;
  font-weight: 700;
  /* 大写 */
  text-transform: uppercase;
  color: #fff;
  /* 字间距 */
  letter-spacing: 5px;
}
input{
  background-color: transparent;
  width: 70%;
  color: #fff;
  border: none;
  /* 下边框样式 */
  border-bottom: 1px solid rgba(255,255,255,0.4);
  padding: 10px 0;
  text-indent: 10px;
  margin: 8px 0;
  font-size: 14px;
  letter-spacing: 2px;
}
input::placeholder{
  color: #fff;
}
input:focus{
  color: #8e9aaf;
  outline: none;
  border-bottom: 1px solid rgba(50, 102, 238, 0.5);
  transition: 0.5s;
}
input:focus::placeholder{
  opacity: 0;
}
.form-box button{
  width: 70%;
  margin-top: 35px;
  background-color: #f6f6f6;
  outline: none;
  border-radius: 8px;
  padding: 13px;
  color: #79c5ef;
  letter-spacing: 2px;
  border: none;
  cursor: pointer;
}
.form-box button:hover{
  background-color: #4989c8;
  color: #f6f6f6;
  transition: background-color 0.5s ease;
}
.con-box{
  width: 50%;
  /* 弹性布局 垂直排列 居中 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* 绝对定位 居中 */
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
.con-box.left{
  left: -2%;
}
.con-box.right{
  right: -2%;
}
.con-box h2{
  color: #8e9aaf;
  font-size: 25px;
  font-weight: bold;
  letter-spacing: 3px;
  text-align: center;
  margin-bottom: 4px;
}
.con-box p{
  font-size: 12px;
  letter-spacing: 2px;
  color: #8e9aaf;
  text-align: center;
}
.con-box span{
  color: #4989c8;
}
.con-box img{
  width: 150px;
  height: 150px;
  opacity: 0.9;
  margin: 40px 0;
}
.con-box button{
  margin-top: 3%;
  background-color: #fff;
  color: #4989c8;
  border: 1px solid #4989c8;
  padding: 6px 10px;
  border-radius: 5px;
  letter-spacing: 1px;
  outline: none;
  cursor: pointer;
}
.con-box button:hover{
  background-color: #4989c8;
  color: #fff;
}
</style>
