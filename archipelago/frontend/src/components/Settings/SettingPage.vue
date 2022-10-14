<template>
  <el-config-provider namespace="ep">
    <el-container>
      <el-aside width="250px" v-if="type === 0">
        <AudienceSide/>
      </el-aside>
      <el-aside width="250px" v-if="type === 1">
        <MusicianSide/>
      </el-aside>
      <el-container>
        <el-header height="70px">
          <UserHeader/>
        </el-header>
        <el-main className="homepage">
          <SettingCard class="card"/>
        </el-main>
      </el-container>
    </el-container>
  </el-config-provider>
</template>

<script setup>
import {ref} from 'vue'
const type = ref(0)
</script>

<style>
.card {
  margin-left: 200px;
  margin-top: 20px;
  position: absolute;
}
</style>
