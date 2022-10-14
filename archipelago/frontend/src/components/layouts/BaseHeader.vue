<template>
  <el-affix>
    <el-menu
        default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        :ellipsis="false"
    >

      <div class="flex-grow" />
      <el-menu-item index="1" @click="this.$router.push('/Login&Register')">
        <el-icon><Reading /></el-icon>
        LOG IN
      </el-menu-item>
      <el-menu-item index="2" @click="this.$router.push('/Login&Register')">
        <el-icon><UserFilled /></el-icon>
        SIGN UP
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
