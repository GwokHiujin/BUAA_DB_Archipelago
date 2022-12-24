<template>
<div class="flex flex-wrap pt-12">
  <div v-if="alertOpen"
       class="top-95-px px-12 mx-32 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-pink-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
    <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">购买失败！</b> 购买唱片失败 ☹
    </span>
    <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
            v-on:click="closeAlert()">
      <span>×</span>
    </button>
  </div>

  <div v-if="alertOpen1"
       class="top-95-px px-12 mx-32 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-emerald-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
    <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">购买成功！</b> 成功收下此唱片 👓
    </span>
    <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
            v-on:click="closeAlert1()">
      <span>×</span>
    </button>
  </div>

  <section class="text-gray-600 body-font w-full items-center">
    <div class="container px-5 pt-24 pb-16 mx-auto">
      <div class="lg:w-4/5 mx-auto flex flex-wrap">
        <a class="block relative square-album rounded overflow-hidden">
          <img class="object-cover object-center w-full h-full block rounded"
               :src=generalInfo.cover>
        </a>
        <div class="lg:w-6/12 w-full lg:pl-10 lg:py-6 mt-6 lg:mt-0 pl-10">
          <h2 class="text-sm title-font text-gray-500 tracking-widest">
            {{generalInfo.releaseYear}}
          </h2>
          <h1 class="text-gray-900 text-3xl title-font font-medium mb-1">
            {{generalInfo.albumName}}
          </h1>
          <div class="flex mb-4">
          <span class="flex items-center text-gray-600">
            {{generalInfo.salesVolume}} Sold
          </span>
          <span class="flex ml-3 pl-3 py-2 border-l-2 border-gray-200 space-x-2s text-gray-500">
            {{map.albumType[generalInfo.type]}}
          </span>
          </div>
          <p class="leading-relaxed">
            由 {{generalInfo.author}} 制作，
            <t class="hover:text-emerald-600"
               @click="gotoMusician(generalInfo.musicianID)">
              {{generalInfo.releaser}}
            </t> 发布
          </p>
          <div class="flex mt-2 items-center"
               v-if="showTags.length !== 0"
               v-for="arr in showTags">
            <span
                class="text-xs hover:text-emerald-600 font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-100 uppercase last:mr-0 mr-2 mt-2"
                v-if="arr.length !== 0"
                v-for="tag in arr"
                @click="search(tag.tag)"
            >
              {{tag.tag}}
            </span>
          </div>
          <div class="flex mt-2 items-center"
               v-else>
            <span
                class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-100 uppercase last:mr-0 mr-2 mt-2"
            >
              该唱片未填写标签
            </span>
          </div>
          <div class="flex mt-10 border-gray-200 border-t-2 pt-8">
            <span class="title-font font-medium text-2xl text-gray-900">
              ￥ {{generalInfo.price}}
            </span>
            <button class="flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded active:bg-blueGray-600 ease-linear"
                    @click="buy()">
              购买
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="text-gray-600 body-font w-full px-12">
    <div class="container px-5 mx-auto">
    <div class="flex flex-wrap flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-100 border-0">
      <div class="rounded-t mb-0 px-4 py-3 border-0">
        <div class="flex flex-wrap items-center">
          <div class="relative w-full px-4 max-w-full flex-grow flex-1">
            <h3 class="font-semibold text-lg text-blueGray-700">
              🎹 歌曲列表
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
              歌曲名
            </th>

            <th
                class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
            >
              歌曲时长
            </th>

            <th
                class="px-6 align-middle bg-blueGray-50 text-blueGray-500 border-blueGray-100 border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
            >
              试听链接
            </th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="song in songList">
            <td
                class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
            >
              {{song.name}}
            </td>

            <td
                class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
            >
              {{(song.songLast / 60).toString().split('.').at(0)}} : {{(song.songLast % 60).toString().substring(0, 2)}}
            </td>

            <td
                class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
            >
              {{song.ADT}}
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    </div>
  </section>

  <section class="text-gray-600 body-font w-full px-12 pt-12">
    <div class="flex-grow pr-12 md:pr-16 flex flex-col items-start mb-16 text-left">
      <h1 class="title-font text-4xl mb-4 font-medium text-gray-900">#评论区
      </h1>
      <div class="w-full lg:w-12/12 pt-2">
        <div class="relative w-full mb-3">
          <textarea
              type="text"
              class="border-0 bg-gray-100 px-3 py-3 placeholder-blueGray-400 text-blueGray-600 bg-white rounded text-sm focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              rows="2"
              placeholder="✨跟大家分享你的看法吧！:)"
              id="curComment"
          >
              </textarea
              >
        </div>
      </div>
      <button class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-xs px-4 py-2 rounded-full shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
              type="button"
              @click="addComment()">
        发布评论
      </button>
      <strong class="mb-8 leading-relaxed mt-8">
        最新评论({{commentList.length}})</strong>
    </div>


    <div class="flex w-full mt-4" v-for="comment in commentList" v-if="commentList.length !== 0" :key="commentKey">
      <div class="flex-shrink-0 mr-3">
        <img class="rounded-full w-8 h-8 sm:square-8 border border-white"
             :src="comment.avatar">
      </div>
      <div class="flex-1 border rounded-lg px-4 py-2 sm:px-6 sm:py-4 leading-relaxed">
        <strong>{{comment.username}}</strong> <span class="text-xs text-gray-400">{{timeTrans(comment.setTime)}}</span>
        <p class="text-sm w-full">
          {{comment.comment}}
        </p>
      </div>
    </div>

  </section>


</div>
</template>

<script>
import axios from "axios";
import dayjs from "dayjs";

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
};

let compareTime = function (x, y) {
  let time1 = Date.parse(x.setTime);
  let time2 = Date.parse(y.setTime);
  if (time2 < time1) {
    return -1;
  } else {
    return 1;
  }
}

export default {
  name: "Album",
  data() {
    return {
      albumTags: [
        {
          tag: '',
        }
      ],
      showTags: [
        [
          {
            tag: '',
          }
        ]
      ],
      generalInfo: {
        albumID: -1,
        albumName: '',
        price: '',
        author: '',
        releaseYear: '',
        releaser: '',
        cover: '',
        type: -1,
        resource: '',
        salesVolume: -1,
        musicianID: -1,
      },
      songList: [
        {
          name: '',
          songLast: -1,
          ADT: '',
          albumID: -1,
        }
      ],
      commentList: [
        {
          comment: '',
          username: '',
          avatar: '',
          setTime: '',
        }
      ],
      alertOpen: false,
      alertOpen1: false,
      map,
      commentKey: 0,
    }
  },
  mounted() {
    console.log("hey")
    this.getAlbumInfo();
    this.getTags();
    this.getComments();
  },
  methods: {
    timeTrans: function (data) {
      let time = data //将需要格式化的数据传入
      let utc = require('dayjs/plugin/utc')
      dayjs.extend(utc)

      console.log(time, 'before')
      time = this.dayjs.utc(time).format('YYYY-MM-DD HH:mm:ss');
      console.log(time, 'after')
      return time;
    },
    closeAlert: function () {
      this.alertOpen = false;
    },
    closeAlert1: function () {
      this.alertOpen1 = false;
    },
    getAlbumInfo: function () {
      let that = this;
      let aid = that.$route.query.aid;
      let data = {
        albumID: aid,
      }
      axios.request({
        url: "/get_album_info/",
        baseURL: '/api',
        method: 'post',
        data: JSON.stringify(data)
      })
          .then(function (response) {
            console.log(response.data)
            that.generalInfo = response.data.generalInfo
            that.songList = response.data.songList
          }).catch(function (error) {
        console.log(error)
      })
    },
    getTags: function () {
      let that = this;
      let aid = that.$route.query.aid;
      that.showTags = that.showTags.slice(1);
      let data = {
        albumID: aid,
      }
      axios.request({
        url: "/get_album_tag/",
        baseURL: '/api',
        method: 'post',
        data: JSON.stringify(data)
      })
          .then(function (response) {
            console.log(response.data.data)
            that.albumTags = response.data.data
            let size = 4;
            for(let i = 0; i < response.data.data.length; i += size){
              that.showTags.push(response.data.data.slice(i, i+size));
            }
          }).catch(function (error) {
        console.log(error)
      })
    },
    getComments: function () {
      let that = this;
      that.commentList = that.commentList.slice(1);
      let aid = that.$route.query.aid;
      let data = {
        albumID: aid,
      }
      axios.request({
        url: "/get_comment/",
        baseURL: '/api',
        method: 'post',
        data: JSON.stringify(data)
      })
          .then(function (response) {
            that.commentList = response.data.commentList.sort(compareTime)
            console.log(response.data.commentList.setTime)
            console.log(that.commentList)
          }).catch(function (error) {
        console.log(error)
      })
    },
    addComment: function () {
      let that = this;
      let aid = that.$route.query.aid;
      let data = {
        albumID: aid,
        comment: document.getElementById("curComment").value
      }
      console.log(data)
      axios.request({
        url: "/add_comment/",
        baseURL: '/api',
        method: 'post',
        data: JSON.stringify(data)
      })
          .then(function (response) {
            that.getComments();
            that.commentKey += 1;
          }).catch(function (error) {
        console.log(error)
      })
    },
    buy: function () {
      let that = this;
      let aid = that.$route.query.aid;
      let data = {
        albumID: aid,
      }
      axios({
        method: 'post',
        url: "/gen_order/",
        baseURL: '/api',
        data: JSON.stringify(data)
      }).then(res => {
        console.log(res.data)
        if (res.data.errno === 0) {
          that.alertOpen1 = true;
        } else {
          that.alertOpen = true;
        }
        this.getAlbumInfo()
      }).catch(err => {
        console.log(err)
      })
    },
    gotoMusician: function (mid) {
      let that = this;
      that.$router.push({
        path: '/profile',
        query: {
          mid: mid
        }
      })
    },
    search: function (tag) {
      let toSearch = tag;
      if (toSearch !== undefined && toSearch !== '') {
        this.$router.push({
          path: '/admin/search',
          query: {
            target: toSearch,
            type: 'tag'
          }
        })
      }
    }
  }
}
</script>

<style scoped>

</style>