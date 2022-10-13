<template>
  <el-config-provider namespace="ep">
    <el-container>
      <el-aside width="250px">
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

<script>
export default {
  name: "SettingPage"
}
</script>

<style>
.card {
  margin-left: 200px;
  margin-top: 20px;
  position: absolute;
}
</style>
