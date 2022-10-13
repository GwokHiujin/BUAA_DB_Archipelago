<template>
  <el-header>

  </el-header>

  <el-carousel :interval="4000" type="card" height="300px">
    <el-carousel-item>
      <img
          src="https://images.unsplash.com/photo-1511379938547-c1f69419868d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
          height="300"
      />
    </el-carousel-item>
    <el-carousel-item>
      <img
          src="https://images.unsplash.com/photo-1523297554394-dc159677ffe1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=579&q=80"
          height="300"
      />
    </el-carousel-item>
    <el-carousel-item>
      <img
          src="https://images.unsplash.com/photo-1527181579058-10c7b0de6e49?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80"
          height="300"
      />
    </el-carousel-item>
    <el-carousel-item>
      <img
          src="https://images.unsplash.com/photo-1565791381266-8047707de6bc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80"
          height="300"
      />
    </el-carousel-item>
  </el-carousel>
  <el-divider/>
  <br>
  <span class="el-descriptions" style="font-family: Gabriola; font-size: 21px">
      Archipelago, help you discover amazing new music and directly support the artists who make it.
  </span>
</template>

<style scoped>
.el-carousel__item h3 {
  display: flex;
  color: #475669;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
