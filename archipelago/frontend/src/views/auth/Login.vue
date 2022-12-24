<template>
  <div v-if="alertOpen"
       class="top-95-px px-12 mx-64 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-pink-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
    <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">登录失败！</b> ☹ 请检查您是否输入了正确的信息！
    </span>
    <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
            v-on:click="closeAlert()">
      <span>×</span>
    </button>
  </div>

  <div v-if="alertOpen1"
       class="top-95-px px-12 mx-64 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-emerald-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
    <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">登录成功！</b> ✨ 欢迎开启群岛之旅
    </span>
    <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
            v-on:click="closeAlert1()">
      <span>×</span>
    </button>
  </div>


  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-center justify-center h-full">
      <div class="w-full lg:w-4/12 px-4">
        <div
          class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0"
        >
          <div class="rounded-t mb-0 px-6 py-6">
            <div class="text-center mb-3">
              <h6 class="text-blueGray-500 text-lg font-bold">
                登录
              </h6>
            </div>
            <hr class="mt-6 border-b-1 border-blueGray-300" />
          </div>
          <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
            <form>
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  邮箱
                </label>
                <input
                  type="email"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="邮箱"
                  id="emailAddress"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  密码
                </label>
                <input
                  type="password"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="密码"
                  id="password"
                />
              </div>

              <div class="text-center mt-8">
                  <button
                    class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                    type="button"
                    @click="login()"
                  >
                    登录
                  </button>
              </div>
            </form>
          </div>
        </div>
        <div class="flex flex-wrap mt-6 relative">
          <div class="w-1/2">

          </div>
          <div class="w-1/2 text-right">
            <router-link to="/auth/register" class="text-blueGray-200">
              <small>新用户注册 >></small>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CryptoJS from 'crypto-js'

axios.defaults.withCredentials = true;

export default {
  name: "login",
  data() {
    return {
      alertOpen: false,
      alertOpen1: false,
    }
  },
  components: {

  },
  mounted() {

  },
  methods: {
    closeAlert: function () {
      this.alertOpen = false;
    },
    closeAlert1: function () {
      this.alertOpen1 = false;
    },
    login: function () {
      let params;
      let password = document.getElementById("password").value;
      let password_key = CryptoJS.AES.encrypt(password, CryptoJS.enc.Utf8.parse(this.$cookies.get("aseKey")), {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
      }).toString();
      params = {
        email: document.getElementById("emailAddress").value,
        password: password_key,
      };
      this.$cookies.remove("mid", '/')
      this.$cookies.remove("userInfo_email", '/')
      this.$cookies.remove("userInfo_avatar", '/')
      this.$cookies.remove("userInfo_usertype", '/')
      this.$cookies.remove("userInfo_bio", '/')
      this.$cookies.remove("userInfo_password", '/')
      this.$cookies.remove("flag_isLogin", '/')
      axios({
        method: 'post',
        url: "/api/login/",
        data: JSON.stringify(params)
      }).then(
          res => {
            console.log(res.data)
            if (res.data.errno === 0) {
              this.alertOpen1 = true;

              this.$cookies.remove("mid", '/')
              this.$cookies.remove("userInfo_email", '/')
              this.$cookies.remove("userInfo_avatar", '/')
              this.$cookies.remove("userInfo_usertype", '/')
              this.$cookies.remove("userInfo_bio", '/')
              this.$cookies.remove("userInfo_password", '/')
              this.$cookies.remove("flag_isLogin", '/')

              this.$cookies.set("userInfo_email", res.data.email, '', '/')
              this.$cookies.set("userInfo_username", res.data.name, '', '/')
              this.$cookies.set("userInfo_avatar", res.data.avatar, '', '/')
              this.$cookies.set("mid", res.data.musicianID, '', '/')
              this.$cookies.set("userInfo_usertype", res.data.type === 1 ? 1 : 0, '', '/')
              this.$cookies.set("userInfo_bio", res.data.bio !== '' ? res.data.bio : "江空岛石出，霜落天宇净 :)", '', '/')
              this.$cookies.set("userInfo_password", password_key, '', '/')
              this.$cookies.set("flag_isLogin", true, '', '/')

              console.log('im here')
              console.log(res.data.type)
              console.log(this.$cookies.get("userInfo_usertype"))

              this.$router.push("/admin/index");
            } else {
              this.alertOpen = true;
            }
          }
      ).catch(
          err => {
            console.log(err)
          }
      )
    }
  }
}
</script>
