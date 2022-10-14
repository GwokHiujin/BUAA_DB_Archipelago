import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        userInfo: {
            username: '', //用户昵称
            password: 'aaabbb', //用户密码
            avatar: "src/assets/img/avatar-default", //用户头像
            email: '', //邮箱
            profile: '', //签名
            usertype: "0", //用户类型
        },
        isLogin: false,
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