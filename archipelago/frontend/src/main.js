import { createApp } from "vue";
import { createWebHistory, createRouter } from "vue-router";
import axios from "axios";
import VueCookies from "vue3-cookies";

// styles

import "@fortawesome/fontawesome-free/css/all.min.css";
import "@/assets/styles/tailwind.css";

// mouting point for the whole app

import App from "@/App.vue";

// layouts

import Admin from "@/layouts/Admin.vue";
import Auth from "@/layouts/Auth.vue";

// views for Admin layout

import Settings from "@/views/admin/Settings.vue";
import Tables from "@/views/admin/Tables.vue";
import Maps from "@/views/admin/Maps.vue";
import AdminIndex from "@/views/admin/AdminIndex.vue";
import Album from "@/views/admin/Album.vue";
import Orders from "@/views/admin/OrderList.vue";
import AddAlbum from "@/views/admin/AddAlbum.vue"

// views for Auth layout

import Login from "@/views/auth/Login.vue";
import Register from "@/views/auth/Register.vue";

// views without layouts

import Landing from "@/views/Landing.vue";
import Profile from "@/views/Profile.vue";
import Index from "@/views/Index.vue";
import CardAddAlbum from "./components/Cards/CardAddAlbum";

// routes

const routes = [
  {
    path: "/admin",
    redirect: "/admin/dashboard",
    component: Admin,
    children: [
      {
        path: "/admin/settings",
        component: Settings,
      },
      {
        path: "/admin/tables",
        component: Tables,
      },
      {
        path: "/admin/maps",
        component: Maps,
      },
      {
        path: "/admin/index",
        component: AdminIndex,
      },
      {
        path: "/admin/album",
        component: Album,
      },
      {
        path: "/admin/orders",
        component: Orders,
      },
      {
        path: "/admin/addalbum",
        component: AddAlbum,
      }
    ],
  },
  {
    path: "/auth",
    redirect: "/auth/login",
    component: Auth,
    children: [
      {
        path: "/auth/login",
        component: Login,
      },
      {
        path: "/auth/register",
        component: Register,
      },
    ],
  },
  {
    path: "/landing",
    component: Landing,
  },
  {
    path: '/profile',
    component: Profile,
  },
  {
    path: "/",
    component: Index,
  },
  { path: "/:pathMatch(.*)*", redirect: "/" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const Vue = createApp(App);
Vue.config.globalProperties.$axios = axios

Vue.use(VueCookies, {
  expireTimes: "1d",
  path: "/",
  domain: "",
  secure: true,
  sameSite: "None",
}).use(router).mount("#app");