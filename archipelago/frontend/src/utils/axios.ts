// src/axios.ts
import axios from 'axios'
const env = import.meta.env.VITE_API_BASE_URL;
const ConfigBaseURL = env.VITE_APP_BASE_SERVER + env.VITE_API_BASE_URL //默认路径，这里也可以使用env来判断环境
//使用create方法创建axios实例
const Axios = axios.create({
    timeout: 5000, // 请求超时时间
    baseURL: ConfigBaseURL,
    headers: {
        'Content-Type': 'application/json;charset=UTF-8'
    }
})
// 添加请求拦截器
Axios.interceptors.request.use(config => {
    console.log(config)
    return config
})
// 添加响应拦截器
Axios.interceptors.response.use(response => {
    console.log(response)
    return response.data
}, error => {
    console.log('Response: error', error)
    const msg = error.Message !== undefined ? error.Message : ''
    // alert(msg)
    return Promise.reject(error)
})

export default Axios;