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
        <el-main>
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
</style>
