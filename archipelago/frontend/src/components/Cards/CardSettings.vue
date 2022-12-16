<template>
  <div
    class="flex flex-wrap mt-32 flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0"
  >
    <div v-if="alertOpen"
         class="top-95-px px-12 mx-32 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-pink-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
      <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">修改失败！</b> 修改用户信息失败 ☹ 请检查您是否输入了正确的信息！
    </span>
      <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
              v-on:click="closeAlert()">
        <span>×</span>
      </button>
    </div>

    <div class="rounded-t bg-white mb-0 px-6 py-6">
      <div class="text-center flex justify-between">
        <h6 class="text-blueGray-700 text-xl font-bold">欢迎您，{{this.$cookies.get("userInfo_username")}}！</h6>
        <span
            class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-200 uppercase last:mr-0 mr-2 mt-2"
            v-if="userInfo.type === 1"
        >
          音乐人用户
        </span>
        <span
            class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-200 uppercase last:mr-0 mr-2 mt-2"
            v-else
        >
          普通用户
        </span>
        <button
          class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
          type="button"
          @click="setUserInfo()"
        >
          修改
        </button>
      </div>
    </div>
    <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
      <form>
        <h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
          用户信息
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                用户名
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model.lazy="userInfo.name"
                :placeholder="userInfo.name"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                邮箱
              </label>
              <p
                class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow w-full"
              >
                {{userInfo.email}}
              </p>
            </div>
          </div>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
          修改密码
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                旧密码
              </label>
              <input
                type="password"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                placeholder="请输入旧密码"
                v-model.lazy="old_password"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                新密码
              </label>
              <input
                type="password"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                placeholder="请输入新密码"
                v-model.lazy="new_password1"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                确认新密码
              </label>
              <input
                type="password"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                placeholder="请确认新密码"
                v-model.lazy="new_password2"
              />
            </div>
          </div>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
          修改头像图片
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                上传头像图片
              </label>
              <input
                  type="file"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="请上传头像图片"
                  id="new_userInfo_avatar"
              />
            </div>
          </div>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
          修改个性签名
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <textarea
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                rows="4"
                :placeholder="this.$cookies.get(`userInfo_bio`)"
                v-model.lazy="userInfo.bio"
              >
                  </textarea
              >
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CryptoJS from 'crypto-js'

axios.defaults.withCredentials = true;

export default {
  name: "settings",
  data() {
    return {
      userInfo: {
        email: '',
        name: '',
        avatar: '',
        type: '',
        bio: ''
      },
      old_password: '',
      new_password1: '',
      new_password2: '',
      alertOpen: false,
    }
  },
  mounted() {
    this.getUserInfo();
  },
  methods: {
    closeAlert: function(){
      this.alertOpen = false;
    },
    getUserInfo: function () {
      let that = this;
      axios.request({
        url: "api/get_user_info/",
        method: 'get'
      })
          .then(function (response) {
            console.log(response.data)
            that.userInfo = response.data
          }).catch(function (error) {
        console.log(error)
      })
    },
    setUserInfo: function () {
      let newUserInfo;
      let that = this;
      if (that.new_password1 !== that.new_password2) {
        that.alertOpen = true;
      } else {
        let old_pwd_key = CryptoJS.AES.encrypt(that.old_password, CryptoJS.enc.Utf8.parse(that.$cookies.get("aseKey")), {
          mode: CryptoJS.mode.ECB,
          padding: CryptoJS.pad.Pkcs7
        }).toString();
        let new_pwd_key = CryptoJS.AES.encrypt(that.new_password1, CryptoJS.enc.Utf8.parse(that.$cookies.get("aseKey")), {
          mode: CryptoJS.mode.ECB,
          padding: CryptoJS.pad.Pkcs7
        }).toString();

        newUserInfo = {
          name: that.userInfo.name,
          avatar: document.getElementById("new_userInfo_avatar").id,
          oldPassword: old_pwd_key,
          password: new_pwd_key,
          bio: that.userInfo.bio
        };
        axios({
          method: 'post',
          url: "api/set_user_info/",
          data: JSON.stringify(newUserInfo)
        }).then(res => {
          console.log(res.data)
          if (res.data.errno === 0) {
            location.reload();
          } else {
            that.alertOpen = true;
          }
          location.reload();
        }).catch(err => {
          console.log(err)
        })
      }
    }
  }
}
</script>
