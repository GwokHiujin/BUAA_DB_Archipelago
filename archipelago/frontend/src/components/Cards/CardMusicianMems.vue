<template>
  <div
      class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-white"
  >
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-blueGray-700 text-center">
            👩‍🎤👨‍🎤 音乐人成员 👨‍🎤👩‍🎤
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
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
            名称
          </th>

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
            生日
          </th>

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
            职务 / 角色
          </th>

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
            活动年份
          </th>
        </tr>
        </thead>
        <tbody>
        <tr >
          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
              v-for="mem in member_info"
          >
            {{mem.name}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
              v-for="mem in member_info"
          >
            {{mem.birthday}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
              v-for="mem in member_info"
          >
            {{mem.role}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
              v-for="mem in member_info"
          >
            {{mem.activeYear}}
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>

import axios from "axios";

export default {
  name: 'CardMusicianMems',
  props:['mid'],
  data() {
    return {
      member_info: [
        {
          name: '',
          birthday: '',
          role: '',
          activeYear: '',
        }
      ],
      curID: this.mid
    };
  },
  mounted() {
    this.getMemInfo();
  },
  methods: {
    getMemInfo: function () {
      let that = this;
      let data = {
        musicianID: that.curID
      }
      axios.request({
        url: "/get_musician_member/",
        baseURL: '/api',
        method: 'get',
        data: JSON.stringify(data)
      })
          .then(function (response) {
            console.log(response.data)
            that.member_info = response.data
          }).catch(function (error) {
        console.log(error)
      })
    }
  }
};
</script>
