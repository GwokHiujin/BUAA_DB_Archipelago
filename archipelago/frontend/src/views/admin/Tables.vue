<template>
  <div class="flex flex-wrap mt-4">
    <div class="w-full mb-4 px-4 mt-24">
      <router-link to="/admin/addalbum">
        <button class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                type="button">
          添加唱片
        </button>
      </router-link>
    </div>

    <div class="w-full mb-12 px-4">
      <CardSelfTable :mid="this.$cookies.get('mid')"/>
    </div>
  </div>
</template>
<script>
import CardSelfTable from "@/components/Cards/CardSelfTable.vue";

export default {
  components: {
    CardSelfTable,
  },
};
</script>
