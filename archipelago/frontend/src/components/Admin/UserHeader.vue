<template>
  <el-affix>
    <el-menu
        default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        :ellipsis="false"
    >

      <div class="flex-grow" />
      <el-menu-item index="/SettingPage">
        <el-avatar>

        </el-avatar>
      </el-menu-item>
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
</style>
