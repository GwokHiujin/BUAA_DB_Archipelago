<template>
  <div>
    <button
        class="lg:bg-opacity-0 font-bold uppercase text-sm py-3 pr-12 hover:text-pink-500 outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
        type="button"
        v-on:click="toggleModal()"
    >
      <i
          class="fas fa-lock mr-2 text-base text-pink-500"
      ></i>
      注销账号
    </button>

    <div v-if="alertOpen"
         class="top-95-px px-12 mx-64 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-pink-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
      <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">注销失败！</b> 注销操作失败 ☹ 请检查您是否输入了正确的信息！
    </span>
      <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
              v-on:click="closeAlert()">
        <span>×</span>
      </button>
    </div>

    <div v-if="showModal"
         class="top-95-px px-12 mx-64 overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex" >
      <div class="relative w-auto my-6 mx-auto max-w-4xl shadow-2xl">
        <!--content-->
        <div class="border-0 rounded-lg shadow-2xl px-3 py-3 relative flex flex-col w-full bg-white outline-none focus:outline-none">
          <!--header-->
          <div class="flex items-start justify-between p-5 text-center border-b border-solid border-blueGray-200 rounded-t">
            <h3 class="text-3xl font-semibold place-content-center ml-auto">
              注销账号
            </h3>
            <button class="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none" v-on:click="toggleModal()">
              <span class="bg-transparent text-black hover:text-red-500 opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                ×
              </span>
            </button>
          </div>
          <!--body-->
          <div class="relative px-6 flex-auto py-6">
            <p class="text-blueGray-500 text-sm leading-relaxed w-card text-center mb-4">
              确定要注销当前群岛账号吗？此操作不可撤回。
            </p>
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                请输入原账号密码
              </label>
              <input
                  type="password"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="原密码"
                  id="password"
              />
            </div>
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                请确认原账号密码
              </label>
              <input
                  type="password"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="确认密码"
                  id="confirmPassword"
              />
            </div>
          </div>
          <!--footer-->
          <div class="flex items-center justify-end p-6 border-t border-solid border-blueGray-200 rounded-b">
            <button
                class="bg-white text-red-500 font-bold uppercase px-6 py-3 text-sm rounded hover:bg-gray-100 outline-none focus:outline-none mr-1 mb-1 mt-4 ease-linear transition-all duration-150"
                type="button"
                v-on:click="toggleModal()"
            >
              Close
            </button>
            <button
                class="bg-blueGray-600 text-white active:bg-red-500 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:bg-red-500 outline-none focus:outline-none mr-1 mb-1 mt-4 ease-linear transition-all duration-150"
                type="button"
                v-on:click="deleteAccount()"
            >
              注销
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="showModal" class="opacity-25 fixed inset-0 z-40 bg-black"></div>
  </div>
</template>

<script>
import axios from 'axios';
import CryptoJS from 'crypto-js'

export default {
  name: "CardLogout",
  data() {
    return {
      showModal: false,
      alertOpen: false
    }
  },
  methods: {
    toggleModal: function () {
      console.log("showModal is ", this.showModal)
      this.showModal = !this.showModal;
    },
    closeAlert: function(){
      this.alertOpen = false;
    },
    deleteAccount: function () {
      let originPassword = document.getElementById("password").value;
      let confirmPassword = document.getElementById("confirmPassword").value;

      let password0 = CryptoJS.AES.encrypt(originPassword, CryptoJS.enc.Utf8.parse(this.$cookies.get("aseKey")), {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
      }).toString();
      let password1 = CryptoJS.AES.encrypt(confirmPassword, CryptoJS.enc.Utf8.parse(this.$cookies.get("aseKey")), {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
      }).toString();

      if (password0 !== password1) {
        this.showModal = false;
        this.alertOpen = true;
      } else {
        axios.request({
          method: 'post',
          url: "/delete_account",
          baseURL: '/api',
          data: JSON.stringify({
            userEmail: this.$cookies.get("userInfo_email"),
            password0: password0,
            password1: password1
          })
        }).then(
            res => {
              console.log(res.data)
              if (res.data.errno === 0) {
                this.$router.push("/");
              } else {
                this.showModal = false;
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
}
</script>