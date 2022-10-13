<template>
  <el-config-provider namespace="ep">
    <el-container>
      <el-aside width="250px">
        <AudienceSide/>
      </el-aside>
      <el-container>
        <el-header height="70px">
          <UserHeader/>
        </el-header>
        <el-main class="homepage">
          <HelloWorld />
        </el-main>
      </el-container>
    </el-container>
  </el-config-provider>
</template>

<script>
export default {
  name: "AudienceIndex"
}
</script>

<style>
#app {
  text-align: center;
  color: var(--ep-text-color-primary);
}
</style>
