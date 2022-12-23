<template>
  <div>
    <!-- Basic layouts -->
    <sidebar />
    <div class="relative md:ml-64 bg-white">
      <admin-navbar :key="componentKey1"/>
      <header-stats />
      <div class="px-4 md:px-10 mx-auto w-full -m-24">
        <div class="flex flex-wrap">
          <div class="w-full">
            <CardSettings @change="changeNavBar()"/>
          </div>
        </div>
        <footer-admin />
      </div>
    </div>
  </div>
</template>
<script>
import CardSettings from "@/components/Cards/CardSettings.vue";
import AdminNavbar from "@/components/Navbars/AdminNavbar.vue";
import Sidebar from "@/components/Sidebar/Sidebar.vue";
import HeaderStats from "@/components/Headers/HeaderStats.vue";
import FooterAdmin from "@/components/Footers/FooterAdmin.vue";

export default {
  components: {
    CardSettings,
    AdminNavbar,
    Sidebar,
    HeaderStats,
    FooterAdmin,
  },
  data() {
    return {
      componentKey1: 0,
    }
  },
  methods: {
    changeNavBar: function (componentKey1) {
      console.log(componentKey1)
      this.componentKey1 = componentKey1;
    }
  }
};
</script>
