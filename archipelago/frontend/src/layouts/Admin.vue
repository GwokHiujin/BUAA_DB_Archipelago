<template>
  <div>
    <!-- Basic layouts -->
    <sidebar />
    <Logout v-if="this.$cookies.get('flag_logOut_showModal') === 'true'" class="transition-all duration-150"/>
    <div class="relative md:ml-64 bg-blueGray-100">
      <admin-navbar />
      <header-stats />
      <div class="px-4 md:px-10 mx-auto w-full -m-24">
        <router-view />
        <footer-admin />
      </div>
    </div>
  </div>
</template>

<script>
import AdminNavbar from "@/components/Navbars/AdminNavbar.vue";
import Sidebar from "@/components/Sidebar/Sidebar.vue";
import HeaderStats from "@/components/Headers/HeaderStats.vue";
import FooterAdmin from "@/components/Footers/FooterAdmin.vue";
import Logout from "@/components/Cards/CardLogout.vue";

export default {
  name: "admin-layout",
  data: function () {
    return {
      showModal: false,
    }
  },
  components: {
    AdminNavbar,
    Sidebar,
    HeaderStats,
    FooterAdmin,
    Logout,
  },
  mounted() {
    /*
    if (this.$cookies.getCookie("flag_isLogin") !== true) {
      this.$router.push("/");
    }
     */
    console.log("Logout Card's showModal is " + this.$cookies.get("flag_logOut_showModal"));
  }
};
</script>
