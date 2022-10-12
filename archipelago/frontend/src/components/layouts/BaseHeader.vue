<script lang="ts" setup>
import { toggleDark } from '~/composables';
import brandImg from 'src/assets/img/logo-long.png'
</script>

<template>
  <el-affix>
    <el-menu
        default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        :ellipsis="false"
    >

      <div class="flex-grow" />
      <el-menu-item index="1">
        <el-icon><Reading /></el-icon>
        LOG IN
      </el-menu-item>
      <el-menu-item index="2">
        <el-icon><UserFilled /></el-icon>
        REGISTER
      </el-menu-item>
    </el-menu>
  </el-affix>
</template>

<style>
.flex-grow {
  flex-grow: 1;
}
</style>
