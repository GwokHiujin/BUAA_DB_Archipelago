<template>
  <el-affix>
    <el-menu
        :default-active="this.$route.path" router
        class="el-menu-demo"
        mode="horizontal"
        :ellipsis="false"
    >

      <el-menu-item index="/SettingPage">
        <img src="src/assets/img/avatar-default.jpg" class="head-avatar" />
      </el-menu-item>

      <div class="flex-grow" />
      <el-menu-item index="/">
        <el-icon><Promotion /></el-icon>
        LOG OUT
      </el-menu-item>
      <el-menu-item index="/UserDelete" style="color: #b21a20">
        <el-icon><DeleteFilled /></el-icon>
        Delete
      </el-menu-item>
    </el-menu>
  </el-affix>
</template>

<style>
.flex-grow {
  flex-grow: 1;
}

.el-menu-demo {
  font-family: "Berlin Sans FB";
  font-size: larger;
}

.head-avatar {
  width: 45px;
  border-radius: 100%;
  margin-top: auto;
  margin-bottom: auto;
  margin-left: 10px;
  border: 2px solid transparent;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.24);
  background: white;
}
</style>
