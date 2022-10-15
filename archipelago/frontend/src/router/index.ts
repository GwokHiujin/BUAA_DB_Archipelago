import { createRouter, createWebHashHistory } from "vue-router";

// Index page
import Index from '../components/layouts/Index.vue'
import AudienceIndex from '../components/layouts/AudienceIndex.vue'
import MusicianIndex from '../components/layouts/MusicianIndex.vue'
// Album page
import AlbumTable from '../components/Album/AlbumTable.vue'
// Musician page
import MusicianProfile from '../components/Musician/MusicianProfile.vue'
// Setting page
import SettingPage from '../components/Settings/SettingPage.vue'
// Admin page
import UserDelete from '../components/layouts/DeleteUser.vue'
import LoginNRegister from "~/components/layouts/LoginNRegister.vue";

//LoginAndRegister page
import LoginAndRegister from '../components/LogingAndRegister/LoginAndRegister.vue'

const routes = [
    {
        path: "/",
        name: "Index",
        component: Index
    },
    {
        path: "/AudienceIndex",
        name: "AudienceIndex",
        component: AudienceIndex
    },
    {
        path: "/MusicianIndex",
        name: "MusicianIndex",
        component: MusicianIndex
    },
    {
        path: "/MusicianProfile",
        name: "MusicianProfile",
        component: MusicianProfile,
    },
    {
        path: "/AlbumTable",
        name: "AlbumTable",
        component: AlbumTable,
    },
    {
        path: "/LoginNRegister",
        name: "LoginNRegister",
        component: LoginNRegister
    },
    // {
    //     path: "/UserDelete",
    //     name: "UserDelete",
    //     component: UserDelete
    // },
    {
        path: "/Login&Register",
        name: "Login&Register",
        component: LoginNRegister
    },
    {
        path: "/SettingPage",
        name: "SettingPage",
        component: SettingPage,
    }
]

export const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})
