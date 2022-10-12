<template>
  <el-affix>
      <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
      >
        <div style="display: flex">
          <div>
            <img alt="Archipelago logo" src="src/assets/img/logo-long.png" width="220"/>
          </div>
        </div>
        <el-menu-item index="1">
          <template #title>
          <el-icon><HomeFilled /></el-icon>
          <span>Home</span>
          </template>
        </el-menu-item>
        <el-menu-item index="2">
          <template #title>
          <el-icon><Tools /></el-icon>
          <span>Settings</span>
          </template>
        </el-menu-item>
        <el-menu-item index="3">
          <template #title>
          <el-icon><BrushFilled /></el-icon>
          <span>Musician Profile</span>
          </template>
        </el-menu-item>
        <el-menu-item index="4">
          <template #title>
          <el-icon><Headset /></el-icon>
          <span>Album</span>
          </template>
        </el-menu-item>
      </el-menu>
  </el-affix>
</template>

<script lang="ts" setup>

const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

