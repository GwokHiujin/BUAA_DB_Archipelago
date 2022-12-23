<template>
  <div
      class="flex flex-wrap flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-100 border-0"
  >
    <div v-if="alertOpen"
         class="top-95-px px-12 mx-64 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-pink-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
      <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">删除失败！</b> 抱歉，删除唱片操作失败 ☹
    </span>
      <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
              v-on:click="closeAlert()">
        <span>×</span>
      </button>
    </div>

    <div v-if="showModal"
         class="top-95-px px-12 mx-32 overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex" >
      <div class="relative w-auto my-6 mx-auto max-w-4xl shadow-2xl">
        <!--content-->
        <div class="border-0 rounded-lg shadow-2xl px-3 py-3 relative flex flex-col w-full bg-white outline-none focus:outline-none">
          <!--header-->
          <div class="flex items-start justify-between p-5 text-center border-b border-solid border-blueGray-200 rounded-t">
            <h3 class="text-3xl font-semibold place-content-center ml-auto">
              删除唱片
            </h3>
            <button class="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none" v-on:click="toggleModal()">
              <span class="bg-transparent text-black hover:text-red-500 opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                ×
              </span>
            </button>
          </div>
          <!--body-->
          <div class="relative px-6 flex-auto py-6">
            <p class="text-blueGray-500 text-sm leading-relaxed w-card text-center mb-4">
              确定要删除该唱片吗？此操作不可撤回。
            </p>
          </div>
          <!--footer-->
          <div class="flex items-center justify-end p-6 border-t border-solid border-blueGray-200 rounded-b">
            <button
                class="bg-white text-red-500 font-bold uppercase px-6 py-3 text-sm rounded hover:bg-gray-100 outline-none focus:outline-none mr-1 mb-1 mt-4 ease-linear transition-all duration-150"
                type="button"
                v-on:click="toggleModal()"
            >
              Close
            </button>
            <button
                class="bg-blueGray-600 text-white active:bg-red-500 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:bg-red-500 outline-none focus:outline-none mr-1 mb-1 mt-4 ease-linear transition-all duration-150"
                type="button"
                v-on:click="deleteAlbum()"
            >
              删除
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="showModal" class="opacity-25 fixed inset-0 z-40 bg-black"></div>

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

          <th
              class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
          >
            删除唱片
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="disc in discInfo">
          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 hover:text-emerald-600"
              @click="gotoAlbum(disc.albumID)"
          >
            {{disc.albumName}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
            ￥{{disc.price}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
            {{disc.author}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
            {{disc.releaseYear}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
            {{disc.releaser}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
            {{map.albumType[disc.type]}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
            {{disc.salesVolume}}
          </td>

          <td
              class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
            <button class="background-transparent text-gray-500 font-bold uppercase text-xs px-4 py-2 rounded hover:text-pink-500 outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                    type="button"
                    id="toDeleteAlbum"
                    @click="toggleModal(disc.albumID)">
              <i class="fas fa-trash"></i>
            </button>
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
  data() {
    return {
      discInfo: [
        {
          albumID: -1,
          albumName: '',
          price: '',
          author: '',
          releaseYear: '',
          releaser: '',
          cover: '',
          type: -1,
          resource: '',
          salesVolume: '',
        }
      ],
      map,
      showModal: false,
      alertOpen: false,
      toDelete: '',
    };
  },
  mounted() {
    this.getAlbumInfo();
  },
  methods: {
    toggleModal: function (id) {
      let that = this;
      this.showModal = !this.showModal;
      that.toDelete = id;
      console.log(that.toDelete)
    },
    closeAlert: function(){
      this.alertOpen = false;
    },
    deleteAlbum: function () {
      let that = this;
      let data = {
        Tag: that.toDelete
      }
      axios({
        method: 'post',
        url: "/del_album/",
        baseURL: '/api',
        data: JSON.stringify(data)
      }).then(res => {
        console.log(res.data)
        this.alertOpen = false;
        this.showModal = false;
        this.getAlbumInfo();
      }).catch(err => {
        this.alertOpen = true;
        console.log(err)
      })
    },
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
            that.discInfo = response.data
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
