<template>
  <el-affix>
    <el-menu
        :default-active="this.$route.path" router
        class="el-menu-vertical-demo"
    >
      <div style="display: flex">
        <div>
          <img alt="Archipelago logo" src="src/assets/img/logo-long.png" width="220"/>
        </div>
      </div>
      <el-menu-item index="/AudienceIndex">
        <template #title>
          <el-icon><HomeFilled /></el-icon>
          <span>Home</span>
        </template>
      </el-menu-item>

      <el-menu-item index="/SettingPage">
        <template #title>
          <el-icon><Tools /></el-icon>
          <span>Settings</span>
        </template>
      </el-menu-item>
    </el-menu>
  </el-affix>
</template>

<script>
export default {
  name: "AudienceSide"
}

</script>

<style>
.el-menu-vertical-demo {
  font-family: "Berlin Sans FB";
  height: 100vh;
  background-image: url(src/assets/img/background-index.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: bottom;
}
</style>

