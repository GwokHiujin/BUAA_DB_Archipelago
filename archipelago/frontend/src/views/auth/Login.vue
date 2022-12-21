<template>
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

    }
  },
  components: {

  },
  mounted() {

  },
  methods: {
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
      axios({
        method: 'post',
        url: "/api/login/",
        data: JSON.stringify(params)
      }).then(
          res => {
            console.log(res.data)
            if (res.data.errno === 0) {
              this.$cookies.set("userInfo_email", res.data.email)
              this.$cookies.set("userInfo_username", res.data.name)
              if (res.data.avatar !== '') {
                // const myBlob = new window.Blob(res.data.avatar, {type: 'image/jpeg'})
                // this.$cookies.set("userInfo_avatar", window.URL.createObjectURL(myBlob))
                this.$cookies.set("userInfo_avatar", res.data.avatar)
              } else {
                this.$cookies.set("userInfo_avatar", "@/assets/img/avatar-default.jpg")
              }
              this.$cookies.set("mid", res.data.musicianID)
              this.$cookies.set("userInfo_usertype", res.data.type)
              this.$cookies.set("userInfo_bio", res.data.bio !== '' ? res.data.bio : "江空岛石出，霜落天宇净 :)")
              this.$cookies.set("userInfo_password", password_key)
              this.$cookies.set("flag_isLogin", true)
              
              this.$router.push("/admin/index");
            } else {
              // TODO: Alert
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
