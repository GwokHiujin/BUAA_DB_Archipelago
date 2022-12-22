<template>
  <div class="flex flex-wrap pt-32">
    <div class="flex flex-col text-center w-full mb-12 mt-4">
      <h1 class="text-2xl font-semibold leading-normal mb-2 text-blueGray-700">
        🔎 {{keyWord}} 的搜索结果
      </h1>
    </div>

    <div class="w-full">
      <ul class="flex mb-0 list-none flex-wrap pt-3 pb-4 flex-row">
        <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
          <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal" v-on:click="toggleTabs(1)" v-bind:class="{'text-emerald-600 bg-white': openTab !== 1, 'text-white bg-emerald-600': openTab === 1}">
            音乐人结果
          </a>
        </li>
        <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
          <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal" v-on:click="toggleTabs(2)" v-bind:class="{'text-emerald-600 bg-white': openTab !== 2, 'text-white bg-emerald-600': openTab === 2}">
            唱片结果
          </a>
        </li>
      </ul>
      <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 rounded">
        <div class="px-4 py-5 flex flex-wrap">
          <div class="tab-content tab-space w-full">
            <div v-bind:class="{'hidden': openTab !== 1, 'block': openTab === 1}">
              <section class="text-gray-600 body-font items-center"
                       v-if="musicianList.length === 0">
                <div class="container px-5 py-24 mx-auto items-center">
                  <div class="xl:w-1/2 lg:w-3/4 w-full mx-auto text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="inline-block w-8 h-8 text-gray-400 mb-8" viewBox="0 0 975.036 975.036">
                      <path d="M925.036 57.197h-304c-27.6 0-50 22.4-50 50v304c0 27.601 22.4 50 50 50h145.5c-1.9 79.601-20.4 143.3-55.4 191.2-27.6 37.8-69.399 69.1-125.3 93.8-25.7 11.3-36.8 41.7-24.8 67.101l36 76c11.6 24.399 40.3 35.1 65.1 24.399 66.2-28.6 122.101-64.8 167.7-108.8 55.601-53.7 93.7-114.3 114.3-181.9 20.601-67.6 30.9-159.8 30.9-276.8v-239c0-27.599-22.401-50-50-50zM106.036 913.497c65.4-28.5 121-64.699 166.9-108.6 56.1-53.7 94.4-114.1 115-181.2 20.6-67.1 30.899-159.6 30.899-277.5v-239c0-27.6-22.399-50-50-50h-304c-27.6 0-50 22.4-50 50v304c0 27.601 22.4 50 50 50h145.5c-1.9 79.601-20.4 143.3-55.4 191.2-27.6 37.8-69.4 69.1-125.3 93.8-25.7 11.3-36.8 41.7-24.8 67.101l35.9 75.8c11.601 24.399 40.501 35.2 65.301 24.399z"></path>
                    </svg>
                    <p class="leading-relaxed text-lg">
                      Oops！你来到了没有音乐存在的荒岛。
                    </p>
                    <span class="inline-block h-1 w-10 rounded bg-indigo-500 mt-8 mb-6"></span>
                    <h2 class="text-gray-900 font-medium title-font tracking-wider text-sm">👂 听听别的？ </h2>
                  </div>
                </div>
              </section>

              <section class="text-gray-600 body-font" v-else>
                <div class="container px-5 py-24 mx-auto items-center">
                  <div class="w-full -m-4 justify-center flex flex-wrap relative">
                    <div class="lg:w-3/12 md:w-6/12 p-4 w-full"
                         v-for="musician in musicianList">
                      <a class="block relative h-48 rounded overflow-hidden">
                        <img alt="ecommerce"
                             class="object-cover object-center w-full h-full block"
                             src={{musician.photo}}>
                      </a>
                      <div class="mt-4">
                        <h2 class="text-gray-900 title-font text-lg font-medium hover:text-emerald-600"
                            @click="gotoMusician(musician.musicianID)">
                          {{musician.musicianName}}
                        </h2>
                      </div>
                    </div>
                  </div>
                </div>
              </section>
            </div>
            <div v-bind:class="{'hidden': openTab !== 2, 'block': openTab === 2}">
              <section class="text-gray-600 body-font items-center"
                       v-if="albumList.length === 0">
                <div class="container px-5 py-24 mx-auto items-center">
                  <div class="xl:w-1/2 lg:w-3/4 w-full mx-auto text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="inline-block w-8 h-8 text-gray-400 mb-8" viewBox="0 0 975.036 975.036">
                      <path d="M925.036 57.197h-304c-27.6 0-50 22.4-50 50v304c0 27.601 22.4 50 50 50h145.5c-1.9 79.601-20.4 143.3-55.4 191.2-27.6 37.8-69.399 69.1-125.3 93.8-25.7 11.3-36.8 41.7-24.8 67.101l36 76c11.6 24.399 40.3 35.1 65.1 24.399 66.2-28.6 122.101-64.8 167.7-108.8 55.601-53.7 93.7-114.3 114.3-181.9 20.601-67.6 30.9-159.8 30.9-276.8v-239c0-27.599-22.401-50-50-50zM106.036 913.497c65.4-28.5 121-64.699 166.9-108.6 56.1-53.7 94.4-114.1 115-181.2 20.6-67.1 30.899-159.6 30.899-277.5v-239c0-27.6-22.399-50-50-50h-304c-27.6 0-50 22.4-50 50v304c0 27.601 22.4 50 50 50h145.5c-1.9 79.601-20.4 143.3-55.4 191.2-27.6 37.8-69.4 69.1-125.3 93.8-25.7 11.3-36.8 41.7-24.8 67.101l35.9 75.8c11.601 24.399 40.501 35.2 65.301 24.399z"></path>
                    </svg>
                    <p class="leading-relaxed text-lg">
                      Oops！你来到了没有音乐存在的荒岛。
                    </p>
                    <span class="inline-block h-1 w-10 rounded bg-indigo-500 mt-8 mb-6"></span>
                    <h2 class="text-gray-900 font-medium title-font tracking-wider text-sm">👂 听听别的？ </h2>
                  </div>
                </div>
              </section>

              <section class="text-gray-600 body-font">
                <div class="container px-5 py-24 mx-auto">
                  <div class="flex flex-wrap -m-4 justify-center flex flex-wrap relative">
                    <div class="lg:w-3/12 md:w-6/12 p-4 w-full"
                         v-for="album in albumList">
                      <a class="block relative h-48 rounded overflow-hidden">
                        <img alt="ecommerce"
                             class="object-cover object-center w-full h-full block"
                             src={{album.cover}}>
                      </a>
                      <div class="mt-4">
                        <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">
                          {{album.author}}
                        </h3>
                        <h2 class="text-gray-900 title-font text-lg font-medium hover:text-emerald-600"
                            @click="gotoAlbum(album.albumID)">
                          {{album.albumName}}
                        </h2>
                        <p class="mt-1">
                          {{album.salesVolume}} Sold
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </section>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SearchPage",
  data() {
    return {
      string: '',
      openTab: 1,
      musicianList: [
        {
          musicianID: -1,
          musicianName: '',
          photo: '',
        }
      ],
      albumList: [
        {
          albumID: -1,
          albumName: '',
          author: '',
          cover: '',
          salesVolume: -1,
        }
      ],
      keyWord: '',
    }
  },
  mounted() {
    let that = this;
    that.keyWord = that.$route.query.target;
    console.log(that.keyWord)
    this.searchString();
  },
  watch: {
    // 利用watch方法检测路由变化：
    $route: function(to, from) {
      if (to.fullPath !== from.fullPath) {
        let that = this;
        that.keyWord = that.$route.query.target;
        console.log(that.keyWord)
        this.searchString();
      }
    }
  },
  methods: {
    toggleTabs: function (tabNum) {
      this.openTab = tabNum;
    },
    searchString: function () {
      let question;
      let that = this;
      question = {
        keyWord: that.$route.query.target,
      };
      console.log(question)
      let url1;
      if (that.$route.query.type === 'tag') {
        url1 = "/search_tag/";
      } else {
        url1 = "/search_musician_album/";
      }
      axios.request({
        url: url1,
        baseURL: '/api',
        method: 'post',
        data: JSON.stringify(question)
      })
          .then((response) => {
            that.musicianList = response.data.musicianList;
            that.albumList = response.data.albumList;
            console.log(response.data)
          }).catch((e) => {
        console.log(e)
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