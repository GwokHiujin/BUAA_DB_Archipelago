import { createRouter,createWebHashHistory} from "vue-router";

// Index page
import Index from '../components/Index.vue'
import AudienceIndex from '../components/AudienceIndex.vue'
import MusicianIndex from '../components/MusicianIndex.vue'

// Album page
import AlbumTable from '../components/Album/AlbumTable.vue'
import AlbumChange from '../components/Album/AlbumChange.vue'

// Musician page
import MusicianProfile from '../components/Musician/MusicianProfile.vue'
import MusicianProfileChange from '../components/Musician/MusicianChange.vue'

// Setting page
import Settings from '../components/Settings/SettingPage.vue'
import SettingsChangePWD from '../components/Settings/ChangePWD.vue'
import SettingsChangeNN from '../components/Settings/ChangeNN.vue'

// Admin page
import UserRegister from '../components/Admin/Register.vue'
import UserLogin from '../components/Admin/Login.vue'
import UserDelete from '../components/Admin/DeleteUser.vue'

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
        children: [
            {
                path: "MusicianProfileChange",
                name: "MusicianProfileChange",
                component: MusicianProfileChange
            }
        ]
    },
    {
        path: "/AlbumTable",
        name: "AlbumTable",
        component: AlbumTable,
        children: [
            {
                path: "AlbumChange",
                name: "AlbumChange",
                component: AlbumChange
            }
        ]
    },
    {
        path: "/Settings",
        name: "Settings",
        component: Settings,
        children: [
            {
                path: "SettingsChangePWD",
                name: "SettingsChangePWD",
                component: SettingsChangePWD
            },
            {
                path: "SettingsChangeNN",
                name: "SettingsChangeNN",
                component: SettingsChangeNN
            }
        ]
    },
    {
        path: "/UserRegister",
        name: "UserRegister",
        component: UserRegister
    },
    {
        path: "/UserLogin",
        name: "UserLogin",
        component: UserLogin
    },
    {
        path: "/UserDelete",
        name: "UserDelete",
        component: UserDelete
    },
    {
        path: "/Login&Register",
        name: "Login&Register",
        component: LoginAndRegister
    }
]

export const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})
