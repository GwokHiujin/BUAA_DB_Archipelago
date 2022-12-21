<template>
  <div class="flex flex-wrap pt-32">
    <div class="flex flex-col text-center w-full mb-12 mt-4">
      <h1 class="text-2xl font-semibold leading-normal mb-2 text-blueGray-700">
        🔎 SEARCHSTRING 的搜索结果
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
          <div class="tab-content tab-space">
            <div v-bind:class="{'hidden': openTab !== 1, 'block': openTab === 1}">
              <section class="text-gray-600 body-font">
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
                        <h2 class="text-gray-900 title-font text-lg font-medium"
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
                        <h2 class="text-gray-900 title-font text-lg font-medium"
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
    }
  },
  mounted() {
    this.searchString();
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