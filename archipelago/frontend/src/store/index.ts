import { createStore } from 'vuex'

export default createStore({
  state: {
    userInfo: {
      username: '', //用户昵称
      password: '', //用户密码
      avatar: "src/assets/img/avatar-default.jpg", //用户头像
      email: '', //邮箱
      profile: '', //签名
      usertype: 0, //用户类型
    },
    isLogin: false,
    aseKey: "20373543"
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
