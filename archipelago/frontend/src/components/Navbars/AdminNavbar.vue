<template>
  <!-- Navbar -->
  <nav
    class="absolute top-0 left-0 w-full z-10 bg-transparent md:flex-row md:flex-nowrap md:justify-start flex items-center p-4"
  >
    <div
      class="w-full mx-autp items-center flex justify-between md:flex-nowrap flex-wrap md:px-10 px-4"
    >
      <!-- Brand -->
      <router-link to="/admin/index">
      <p
        class="text-white text-sm uppercase hidden lg:inline-block font-semibold"
      >
        群岛 Archipelago
      </p>
      </router-link>
      <!-- Form -->
      <form
        class="md:flex hidden flex-row flex-wrap items-center lg:ml-auto mr-4"
      >
        <div class="relative flex w-full flex-wrap items-stretch">
          <span
            class="z-10 h-full leading-snug font-normal absolute text-center text-blueGray-300 absolute bg-transparent rounded text-base items-center justify-center w-8 pl-3 py-3"
          >
          <i class="fas fa-search"></i>
          </span>
          <input
            type="text"
            placeholder="搜索音乐人/唱片名"
            class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 relative bg-white bg-white rounded text-sm shadow outline-none focus:outline-none focus:ring w-full pl-10"
            id="string"
            @keyup.enter="search()"
          />
          <Input v-show="false"></Input>
        </div>
      </form>
      <!-- User -->
      <ul class="flex-col md:flex-row list-none items-center hidden md:flex">
        <div class="items-center flex">
        <span
            class="w-12 h-12 text-sm text-white bg-blueGray-200 inline-flex items-center justify-center rounded-full"
        >
          <img
              class="w-full rounded-full align-middle border-none shadow-lg"
              :src=avatar
              v-if="this.$cookies.get('userInfo_avatar') !== ''"
          />
           <img
               class="w-full rounded-full align-middle border-none shadow-lg"
               :src=team2
               v-else
           />
        </span>
        </div>
      </ul>
    </div>
  </nav>
  <!-- End Navbar -->
</template>

<script>
import team2 from "@/assets/img/team-2-800x800.jpg";
export default {
  data() {
    return {
      avatar: this.$cookies.get('userInfo_avatar'),
      team2,
    }
  },
  methods: {
    search: function () {
      let that = this;
      let toSearch = document.getElementById("string").value;
      if (toSearch !== '') {
        that.$router.push({
          path: '/admin/search',
          query: {
            target: toSearch,
            type: 'normal',
          }
        })
      }
    }
  }
}
</script>
