<template>
  <nav
    class="md:left-0 md:block md:fixed md:top-0 md:bottom-0 md:overflow-y-auto md:flex-row md:flex-nowrap md:overflow-hidden shadow-xl bg-white flex flex-wrap items-center justify-between relative md:w-64 z-10 py-4 px-6"
  >
    <div
      class="md:flex-col md:items-stretch md:min-h-full md:flex-nowrap px-0 flex flex-wrap items-center justify-between w-full mx-auto"
    >
      <!-- Toggler -->
      <button
        class="cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
        type="button"
        v-on:click="toggleCollapseShow('bg-white m-2 py-3 px-6')"
      >
        <i class="fas fa-bars"></i>
      </button>
      <!-- Brand -->
      <router-link
        class="md:block md:pb-2 mr-0 inline-block uppercase p-4 px-0"
        to="/admin/index"
      >
        <img src="@/assets/img/logo-long.png">
      </router-link>
      <!-- User -->
      <ul class="md:hidden items-center flex flex-wrap list-none">
        <li class="inline-block relative">
          <notification-dropdown />
        </li>
        <li class="inline-block relative">
          <user-dropdown />
        </li>
      </ul>
      <!-- Collapse -->
      <div
        class="md:flex md:flex-col md:items-stretch md:opacity-100 md:relative md:mt-4 md:shadow-none shadow absolute top-0 left-0 right-0 z-40 overflow-y-auto overflow-x-hidden h-auto items-center flex-1 rounded"
        v-bind:class="collapseShow"
      >
        <!-- Collapse header -->
        <div
          class="md:min-w-full md:hidden block pb-4 mb-4 border-b border-solid border-blueGray-200"
        >
          <div class="flex flex-wrap">
            <div class="w-6/12">
              <router-link
                class="md:block text-left md:pb-2 text-blueGray-600 mr-0 inline-block whitespace-nowrap text-sm uppercase font-bold p-4 px-0"
                to="/auth/index"
              >
                群岛 Archipelago
              </router-link>
            </div>
            <div class="w-6/12 flex justify-end">
              <button
                type="button"
                class="cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
                v-on:click="toggleCollapseShow('hidden')"
              >
                <i class="fas fa-times"></i>
              </button>
            </div>
          </div>
        </div>
        <!-- Form -->
        <form class="mt-6 mb-4 md:hidden">
          <div class="mb-3 pt-0">
            <input
              type="text"
              placeholder="Search"
              class="border-0 px-3 py-2 h-12 border border-solid border-blueGray-500 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-base leading-snug shadow-none outline-none focus:outline-none w-full font-normal"
            />
          </div>
        </form>

        <!-- Divider -->
        <hr class="my-4 md:min-w-full" />

        <!-- Navigation -->
        <ul class="md:flex-col md:min-w-full flex flex-col list-none">
          <li class="items-center">
            <router-link
              to="/admin/index"
              v-slot="{ href, navigate, isActive }"
            >
              <a
                :href="href"
                @click="navigate"
                class="text-base uppercase py-4 font-bold block"
                :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-blueGray-600 hover:text-blueGray-400',
                ]"
              >
                <i
                  class="fas fa-paper-plane mr-2 text-base"
                  :class="[isActive ? 'opacity-75' : 'text-blueGray-300']"
                ></i>
                发现音乐
              </a>
            </router-link>
          </li>

          <li
              class="items-center"
              v-if="$cookies.get('userInfo_usertype') === '1'"
          >
            <router-link
                class="text-blueGray-600 hover:text-blueGray-400 text-base uppercase py-4 font-bold block"
                to="/profile"
            >
              <i class="fas fa-user-circle text-blueGray-300 mr-2 text-base"></i>
              我的音乐人主页
            </router-link>
          </li>

          <li
              class="items-center"
              v-if="$cookies.get('userInfo_usertype') === '1'"
          >
            <router-link
              to="/admin/tables"
              v-slot="{ href, navigate, isActive }"
            >
              <a
                :href="href"
                @click="navigate"
                class="text-base uppercase py-4 font-bold block"
                :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-blueGray-600 hover:text-blueGray-400',
                ]"
              >
                <i
                  class="fas fa-table mr-2 text-base"
                  :class="[isActive ? 'opacity-75' : 'text-blueGray-300']"
                ></i>
                我的唱片
              </a>
            </router-link>
          </li>

          <li
              class="items-center"
          >
            <router-link
                to="/admin/orders"
                v-slot="{ href, navigate, isActive }"
            >
              <a
                  :href="href"
                  @click="navigate"
                  class="text-base uppercase py-4 font-bold block"
                  :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-blueGray-600 hover:text-blueGray-400',
                ]"
              >
                <i
                    class="fas fa-receipt mr-2 text-base"
                    :class="[isActive ? 'opacity-75' : 'text-blueGray-300']"
                ></i>
                我的订单
              </a>
            </router-link>
          </li>

          <li class="items-center">
            <router-link
                to="/admin/settings"
                v-slot="{ href, navigate, isActive }"
            >
              <a
                  :href="href"
                  @click="navigate"
                  class="text-base uppercase py-4 font-bold block"
                  :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-blueGray-600 hover:text-blueGray-400',
                ]"
              >
                <i
                    class="fas fa-tools mr-2 text-base"
                    :class="[isActive ? 'opacity-75' : 'text-blueGray-300']"
                ></i>
                设置
              </a>
            </router-link>
          </li>

          <!-- Divider -->
          <hr class="my-4 md:min-w-full" />

          <li class="items-center">
            <button
                class="lg:bg-opacity-0 font-bold uppercase text-sm py-3 pr-12 hover:text-pink-500 outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                type="button"
                @click="logout()"
            >
              <i
                  class="fas fa-forward mr-2 text-base"
                  :class="[isActive ? 'opacity-75' : 'text-pink-500']"
              ></i>
              退出登录
            </button>
          </li>

          <li class="items-center">
            <div>
              <CardLogout/>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
); }

<script>
import NotificationDropdown from "@/components/Dropdowns/NotificationDropdown.vue";
import UserDropdown from "@/components/Dropdowns/UserDropdown.vue";
import CardLogout from "../Cards/CardLogout";

export default {
  data() {
    return {
      collapseShow: "hidden",
    };
  },
  mounted() {
    this.$cookies.set("userInfo_usertype", 1)
  },
  components: {
    CardLogout,
    NotificationDropdown,
    UserDropdown,
  },
  methods: {
    toggleCollapseShow: function (classes) {
      this.collapseShow = classes;
    },
    logout: function () {
      this.$cookies.set("flag_isLogin", "false");
      this.$router.push("/");
    }
  }
};
</script>
