<template>
  <div
      class="flex flex-wrap mt-32 flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0"
  >
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-blueGray-700">
            📀 我的订单列表
          </h3>
        </div>
      </div>
    </div>
    <div class="block w-full overflow-x-auto justify-center">
      <!-- Projects table -->
      <table class="items-center w-full bg-transparent border-collapse">
        <thead>
        <tr>
          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
          >
            订单编号
          </th>

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
          >
            唱片 ID
          </th>

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
          >
            订单创建时间
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="order in orderList">
          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
            {{order.orderNum}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 hover:text-emerald-600"
              @click="gotoAlbum(order.albumID)"
          >
            {{order.albumID}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
            {{timeTrans(order.setTime)}}
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import dayjs from "dayjs";
import utc from "dayjs/plugin/utc";

export default {
  name: "OrderList",
  data() {
    return {
      orderList: [
        {
          orderNum: -1,
          albumID: -1,
          setTime: '',
        }
      ]
    }
  },
  mounted() {
    this.getOrder();
  },
  methods: {
    timeTrans: function (data) {
      let time = data //将需要格式化的数据传入
      let utc = require('dayjs/plugin/utc')
      dayjs.extend(utc)

      time = this.dayjs(time).format('YYYY-MM-DD HH:mm:ss');
      return time;
    },
    getOrder: function () {
      let that = this;
      axios.request({
        url: "/get_order/",
        baseURL: '/api',
        method: 'get',
      })
          .then(function (response) {
            console.log(response.data.orderList)
            that.orderList = response.data.orderList
          }).catch(function (error) {
        console.log(error)
      })
    },
    gotoAlbum: function (aid) {
      let that = this;
      that.$router.push({
        path: '/admin/album',
        query: {
          aid: aid
        }
      })
    }
  }
}
</script>

<style scoped>

</style>