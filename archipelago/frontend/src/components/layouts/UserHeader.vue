<template>
  <el-affix>
    <el-menu
        default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        :ellipsis="false"
    >

      <el-menu-item index="1" @click="this.$router.push('/SettingPage')">
        <img src="../../assets/img/avatar-default.jpg" class="head-avatar" />
      </el-menu-item>

      <div class="flex-grow" />
      <el-menu-item index="2" @click="logOut()">
        <el-icon><Promotion /></el-icon>
        LOG OUT
      </el-menu-item>
      <el-menu-item index="3" @click="this.$router.push('/UserDelete')" style="color: #b21a20">
        <el-icon><DeleteFilled /></el-icon>
        Delete
      </el-menu-item>
    </el-menu>
  </el-affix>
</template>

<script>
export default {
  methods: {
    logOut: function () {
      this.$store.state.isLogin = false;
      this.$router.push('/');
    }
  }
}
</script>

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
