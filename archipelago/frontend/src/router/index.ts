import { createRouter,createWebHashHistory} from "vue-router";

import Index from '../components/Index.vue'

const routes = [
    {
        path: "/",
        name: "index",
        component: Index
    }
]

export const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})
