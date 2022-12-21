<template>
  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-center justify-center h-full">
      <div class="w-full lg:w-6/12 px-4">
        <div
          class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0"
        >
          <div class="rounded-t mb-0 px-6 py-6">
            <div class="text-center mb-3">
              <h6 class="text-blueGray-500 text-lg font-bold">
                新用户注册
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
                  用户名
                </label>
                <input
                  type="email"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="用户名"
                  id="username"
                />
              </div>

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
                  id="originPassword"
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                    class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                    htmlFor="grid-password"
                >
                  确认密码
                </label>
                <input
                    type="password"
                    class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    placeholder="确认密码"
                    id="confirmPassword"
                />
              </div>

              <div class="relative w-full mt-8">
                <div class="text-center">
                  <button
                      class="mx-8 bg-emerald-500 text-white focus:bg-blueGray-800 active:bg-emerald-600 font-bold uppercase text-sm px-4 py-4 rounded-full shadow hover:shadow-lg outline-none mb-1 ease-linear transition-all duration-150"
                      type="button"
                      @click="setMusician()"
                  >
                    <i class="fas fa-guitar mr-2"></i> 我是音乐人
                  </button>

                  <button
                      class="mx-8 bg-emerald-500 text-white focus:bg-blueGray-800 active:bg-emerald-600 font-bold uppercase text-sm px-4 py-4 rounded-full shadow hover:shadow-lg outline-none mb-1 ease-linear transition-all duration-150"
                      type="button"
                      @click="setAudience()"
                  >
                    <i class="fas fa-headphones mr-2"></i> 我是听众
                  </button>
                </div>
              </div>

              <div class="text-center mt-8">
                  <button
                    class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                    type="button"
                    @click="register()"
                  >
                    注册
                  </button>
              </div>
            </form>
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
  name: 'Register',
  data() {
    return {
      userType: -1
    }
  },
  components: {

  },
  mounted() {

  },
  methods: {
    setAudience: function () {
      let that = this;
      that.userType = 0;
    },
    setMusician: function () {
      let that = this;
      that.userType = 1;
    },
    register: function () {
      let params;
      let originPassword = document.getElementById("originPassword").value;
      let confirmPassword = document.getElementById("confirmPassword").value;
      params = {
        email: document.getElementById("emailAddress").value,
        name: document.getElementById("username").value,
        password_1: CryptoJS.AES.encrypt(originPassword, CryptoJS.enc.Utf8.parse(this.$cookies.get("aseKey")), {
          mode: CryptoJS.mode.ECB,
          padding: CryptoJS.pad.Pkcs7
        }).toString(),
        password_2: CryptoJS.AES.encrypt(confirmPassword, CryptoJS.enc.Utf8.parse(this.$cookies.get("aseKey")), {
          mode: CryptoJS.mode.ECB,
          padding: CryptoJS.pad.Pkcs7
        }).toString(),
        type: this.userType
      };
      console.log(params);
      axios({
        method: 'post',
        url: "/api/register/",
        data: JSON.stringify(params)
      }).then(
          res => {
            console.log(res.data)
            if (res.data.errno === 0) {
              this.$message({
                message: '注册成功',
                type: 'success',
                showClose: true,
              })
              this.$router.push('/auth/login')
              location.reload()
            } else {
              if (res.data.msg === "密码格式错误") {
                this.$message({
                  message: res.data.msg + ":必须包含字母和数字，且长度在8和18之间",
                  type: 'error',
                  showClose: true,
                })
              } else {
                this.$message({
                  message: res.data.msg,
                  type: 'error',
                  showClose: true,
                })
              }
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
