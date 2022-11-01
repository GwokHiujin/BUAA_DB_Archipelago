<template>
  <div>
    <!-- Basic layouts -->
    <sidebar />
    <Logout v-if="this.$cookies.get('flag_logOut_showModal') === 'true'"/>
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
    this.showModal = this.$cookies.get("flag_logOut_showModal") === "true";
    console.log("showModal is " + this.showModal);
  },
  methods: {
    toggleModal: function () {
      let that = this;
      that.showModal = !that.showModal;
      this.$cookies.set("flag_logOut_showModal", that.showModal.toString());
      console.log("showModal is " + this.$cookies.get('flag_logOut_showModal'));
      location.reload();
    }
  }
};
</script>
