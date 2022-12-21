<template>
  <div
    class="flex flex-wrap flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-100 border-0"
  >
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-blueGray-700">
            🎛 唱片列表
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
            唱片名
          </th>

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
          >
            售价
          </th>

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
          >
            作者
          </th>

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
          >
            发布年份
          </th>

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
          >
            发布者
          </th>

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
          >
            唱片类型
          </th>

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
          >
            销量
          </th>
        </tr>
        </thead>
        <tbody>
        <tr >
          <td
              class="border-t-0 px-6 align-middle hover:text-emerald-600 border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
              v-for="disc in discInfo"
              @click="gotoAlbum(disc.albumID)"
          >
            {{disc.albumName}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
              v-for="disc in discInfo"
          >
            {{disc.price}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
              v-for="disc in discInfo"
          >
            {{disc.author}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
              v-for="disc in discInfo"
          >
            {{disc.releaseYear}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
              v-for="disc in discInfo"
          >
            {{disc.releaser}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
              v-for="disc in discInfo"
          >
            {{map.albumType[disc.type]}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
              v-for="disc in discInfo"
          >
            {{disc.salesVolume}}
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import axios from "axios";

const map = {
  albumType: {
    0: 'EP',
    1: 'Single',
    2: 'Album',
    3: 'Live',
    4: 'Demo',
    5: 'Split',
    6: 'Compilations',
    7: 'Various Artists',
    8: 'Original Soundtrack'
  }
}

export default {
  props:['mid'],
  data() {
    return {
      discInfo: [
        {
          albumID: '',
          albumName: '',
          price: '',
          author: '',
          releaseYear: '',
          releaser: '',
          cover: '',
          type: '',
          resource: '',
          salesVolume: '',
        }
      ],
      map,
      curID: this.mid,
    };
  },
  mounted() {
    this.getAlbumInfo();
  },
  methods: {
    getAlbumInfo: function () {
      let that = this;
      let data = {
        musicianID: that.curID
      }
      axios.request({
        url: "/get_album/",
        baseURL: '/api',
        method: 'get',
        data: JSON.stringify(data)
      })
          .then(function (response) {
            console.log(response.data)
            this.discInfo = response.data
          }).catch(function (error) {
        console.log(error)
      })
    },
    gotoAlbum: function (aid) {
      this.$router.push({
        path: '/admin/album',
        query: {
          aid: aid
        }
      })
    }
  }
};
</script>
