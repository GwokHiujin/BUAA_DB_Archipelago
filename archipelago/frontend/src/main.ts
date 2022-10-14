import { createApp } from 'vue'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import App from './App.vue'
import {router} from './router'
import 'uno.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import axios from "axios";
import store from './store'

const app = createApp(App).use(store)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

app.config.globalProperties.$http=axios
app.use(ElementPlus)
app.use(router)
app.mount('#app')
