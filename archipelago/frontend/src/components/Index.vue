<template>
  <el-config-provider namespace="ep">
    <el-container>
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

<style>
#app {
  text-align: center;
  color: var(--ep-text-color-primary);
}

.element-plus-logo {
  width: 50%;
}

.homepage {
  background-image:
      linear-gradient(to top, transparent, white),
      url(https://www.toptal.com/designers/subtlepatterns/uploads/topography.png);
  background-repeat: repeat;
}
</style>
