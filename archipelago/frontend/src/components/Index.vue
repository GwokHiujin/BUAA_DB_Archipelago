<template>
  <el-config-provider namespace="ep">
    <el-container class="page">
      <el-aside width="250px">
        <BaseSide/>
      </el-aside>
      <el-container>
        <el-header height="70px">
          <BaseHeader/>
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
  name: "Index"
}
</script>

<style>
#app {
  text-align: center;
  color: var(--ep-text-color-primary);
}

.homepage {
  height: 100%;
  background-image: url(src/assets/img/grey.png);
  background-size: auto;
}
</style>
