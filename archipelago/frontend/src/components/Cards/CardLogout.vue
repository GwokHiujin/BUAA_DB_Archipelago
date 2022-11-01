<template>
  <div>
    <div class="py-40 px-12 mx-64 overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex">
      <div class="relative w-auto my-6 max-w-4xl shadow-2xl">
        <!--content-->
        <div class="border-0 rounded-lg shadow-2xl px-3 py-3 relative flex flex-col w-full bg-white outline-none focus:outline-none">
          <!--header-->
          <div class="flex items-start justify-between p-5 text-center border-b border-solid border-blueGray-200 rounded-t">
            <h3 class="text-3xl font-semibold place-content-center ml-auto">
              注销账号
            </h3>
            <button class="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none" v-on:click="toggleModal()">
              <span class="bg-transparent text-black opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                ×
              </span>
            </button>
          </div>
          <!--body-->
          <div class="relative px-6 flex-auto py-6">
            <p class="text-blueGray-500 text-sm leading-relaxed w-card text-center mb-4">
              请注意，您即将注销此账号！此操作不可撤回。
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
                class="text-red-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1 mt-4 ease-linear transition-all duration-150"
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
    <div class="opacity-25 fixed inset-0 z-40 bg-black"></div>
  </div>
</template>

<script>
import axios from 'axios';
import CryptoJS from 'crypto-js'

export default {
  name: "CardLogout",
  data() {
    return {
      showModal: false
    }
  },
  mounted() {
    /*
    if (this.$cookies.getCookie("flag_isLogin") !== true) {
      this.$router.push("/");
    }
     */
    this.showModal = this.$cookies.get("flag_logOut_showModal") === "true";
    console.log("showModal is " + this.showModal);
  },
  methods: {
    toggleModal: function () {
      let that = this;
      that.showModal = !that.showModal;
      this.$cookies.set("flag_logOut_showModal", that.showModal.toString());
      location.reload();
    },
    deleteAccount: function () {
      let that = this;
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

      axios.request({
        method: 'post',
        url: "/api/delete_account",
        data: JSON.stringify({
          userEmail: this.$cookies.get("userInfo_email"),
          password0: password0,
          password1: password1
        })
      }).then(
          res => {
            console.log(res.data)
            if (res.data.errno === 0) {
              this.$message({
                message: "成功注销账户",
                type: 'success',
                showClose: true
              })
              that.showModal = !that.showModal;
              this.$cookies.remove("flag_logOut_showModal");
              this.$router.push("/");
            } else {
              this.$message({
                message: "注销账户失败！",
                type: 'error',
                showClose: true
              })
              that.showModal = !that.showModal;
              this.$cookies.set("flag_logOut_showModal", that.showModal.toString());
              location.reload();
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