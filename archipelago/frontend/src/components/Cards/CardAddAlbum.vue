<template>
  <div
      class="flex flex-wrap mt-32 flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0"
  >

    <div v-if="alertOpen"
         class="top-95-px px-12 mx-32 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-pink-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
      <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">添加失败！</b> 添加唱片失败 ☹ 请检查您是否输入了正确的信息！
    </span>
      <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
              v-on:click="closeAlert()">
        <span>×</span>
      </button>
    </div>

    <div class="rounded-t bg-white mb-0 px-6 py-6">
      <div class="text-center flex justify-between">
        <h6 class="text-blueGray-700 text-xl font-bold">
          🎼 发布新唱片
        </h6>
        <button
            class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-sm px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
            type="button"
            @click="addNewAlbum()"
        >
          确认发布
        </button>
      </div>
    </div>

    </div>
</template>

<script>
export default {
  name: "CardAddAlbum",
  data() {
    return {
      alertOpen: false,
    }
  },
  methods: {
    closeAlert: function() {
      this.alertOpen = false;
    },
    addNewAlbum: function () {

    }
  }
}
</script>

<style scoped>

</style>