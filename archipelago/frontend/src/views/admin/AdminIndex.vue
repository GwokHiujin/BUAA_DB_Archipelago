<template>
<div>
  <div class="flex flex-wrap">
    <section class="text-gray-600 body-font mx-8 mt-24 w-full items-center">
      <div class="container px-5 py-24 mx-auto items-center">
        <div class="w-full mb-20 justify-center flex flex-wrap relative">
          <div class="lg:w-6/12 mb-6 lg:mb-0">
            <h1 class="text-5xl font-semibold leading-normal mb-2 text-blueGray-700">
              本周推荐 🎧
            </h1>
            <div class="h-1 w-16 bg-emerald-500 rounded"></div>
          </div>

          <div class="lg:w-6/12 mb-6 lg:mb-0">
            <p class="leading-relaxed text-gray-500 mt-2 text-sm">
              🏞  群岛为您精选了上周销售量最高的一批唱片——点击下方的唱片链接，看看大家都在关注什么！<br>
              ✨  当然，欢迎您使用搜索功能，探索自己喜爱的音乐岛屿！
            </p>
          </div>
        </div>

        <div class="flex flex-wrap -m-4 justify-center flex flex-wrap relative mt-12">
          <div class="xl:w-3/12 md:w-6/12 p-4" v-for="album in albumList">
            <div class="bg-gray-100 p-6 rounded-lg h-500-px">
              <img class="h-40 rounded w-auto object-cover object-center mb-6"
                   src={{album.cover}}>
              <h3 class="tracking-wide text-emerald-500 text-xs font-medium title-font">
                {{album.author}}
              </h3>
              <h2 class="text-lg text-gray-900 font-medium title-font mb-4 hover:text-emerald-600"
                  @click="toAlbum(album.albumID)">
                {{ album.albumName }}
              </h2>
              <div class="flex mt-6 items-center pb-5 border-b-2 border-gray-100 mb-5 pb-6">
                <span
                    class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-100 uppercase last:mr-0 mr-2 mt-2"
                    v-for="tag in album.tagList"
                >
                  {{tag.tag}}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="text-gray-600 body-font justify-center flex flex-wrap relative w-full items-center">
      <div class="container px-5 py-4 mx-auto">
        <div class="flex flex-col text-center w-full mb-12 items-center">
          <h1 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700">
            👨‍🎤 最受欢迎音乐人 👩‍🎤
          </h1>
          <p class="lg:w-2/3 mx-auto leading-relaxed text-base">
            群岛为您推荐了这些平台最受欢迎音乐人——看看有没有您心仪的乐手吧！
          </p>
        </div>

        <div class="flex flex-wrap -m-4 justify-center flex flex-wrap relative">
          <div class="lg:w-4/12 sm:w-6/12 p-4"
               v-for="musician in musicianList">
            <div class="flex relative">
              <img class="absolute inset-0 w-full h-full object-cover object-center"
                   src={{musician.photo}}>
              <div class="px-8 py-10 relative z-10 w-full border-4 border-gray-200 bg-white opacity-0 hover:opacity-100">
                <h2 class="tracking-wide text-sm title-font font-medium text-emerald-500 mb-1 hover:text-emerald-600"
                    @click="toMusician(musician.musicianID)">
                  {{musician.musicianName}}
                </h2>
                <p class="leading-relaxed">
                  {{musician.introduction}}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="text-gray-600 body-font justify-center flex flex-wrap relative">
      <div class="container px-4 lg:pt-24 mx-auto">
        <div class="flex flex-col text-center w-full mb-24">
          <h1 class="text-3xl font-semibold leading-normal mb-2 text-blueGray-700">
            自由探索心仪的流派标签
          </h1>
          <p class="lg:w-2/3 mx-auto leading-relaxed text-base mt-2">
            🎸 群岛平台为您推荐这些音乐标签，点击即可自由探索音乐岛屿！
          </p>
          <p class="lg:w-2/3 mx-auto leading-relaxed text-base mt-2">
            💖 邂逅喜欢的音乐后，别忘了分享给您的朋友~
          </p>
        </div>
        
        <div class="flex flex-wrap justify-center flex flex-wrap relative">
          <div class="p-2 lg:w-4/12 md:w-6/12 w-full"
               v-for="tag in tagList">
            <div class="h-full flex items-center p-4 rounded-lg"
                 style="background-image: url('https://www.toptal.com/designers/subtlepatterns/uploads/stripes-light.png')">
              <div class="flex-grow">
                <h2 class="text-gray-900 title-font font-medium hover:text-emerald-600"
                    @click="search(tag.tag)">
                  {{tag.tag}}
                </h2>
                <p class="text-gray-500" v-if="tag.tagType === `0`">
                  风格流派
                </p>
                <p class="text-gray-500" v-if="tag.tagType === `1`">
                  音乐情绪
                </p>
                <p class="text-gray-500" v-if="tag.tagType === `2`">
                  器乐元素
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <h1 class="text-2xl font-semibold leading-normal mb-12 text-blueGray-700 pt-12">
        🧐 没有喜欢的？试试标签检索功能!
      </h1>
      <div class="relative flex w-full flex-wrap items-stretch mb-3 mx-32">
        <span class="z-10 h-full leading-normal font-normal absolute text-center text-blueGray-300 absolute bg-transparent rounded text-lg items-center justify-center w-8 pl-3 py-4">
          <i class="fas fa-search"></i>
        </span>
        <input type="text"
               placeholder="搜索标签"
               class="px-3 py-4 placeholder-blueGray-300 text-blueGray-600 relative bg-white bg-white rounded text-base border border-blueGray-300 outline-none focus:outline-none focus:shadow-outline w-10/12 pl-10"
               v-model.lazy="searchTag"
               @keyup.enter="search()"/>
        <Input v-show="false"></Input>
        <button class="bg-emerald-500 text-white ml-3 active:bg-emerald-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                type="button"
                @click="search()">
          搜索
        </button>
      </div>
    </section>

    <span class="inline-block h-1 w-full rounded bg-gray-100 mt-4 mb-4"></span>

    <!-- footer -->
    <section class="text-gray-500 body-font mx-32 mt-10">
      <div class="container px-5 py-20 mx-auto pt-6"
           :style="`background-image: url('${indexFooter}'); background-size: cover;`">
        <div class="xl:w-1/2 lg:w-3/4 w-full text-center px-8 pb-16 pt-0 bg-white-linear opacity-100">
          <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="inline-block w-8 h-8 text-gray-400 mb-8" viewBox="0 0 975.036 975.036">
            <path d="M925.036 57.197h-304c-27.6 0-50 22.4-50 50v304c0 27.601 22.4 50 50 50h145.5c-1.9 79.601-20.4 143.3-55.4 191.2-27.6 37.8-69.399 69.1-125.3 93.8-25.7 11.3-36.8 41.7-24.8 67.101l36 76c11.6 24.399 40.3 35.1 65.1 24.399 66.2-28.6 122.101-64.8 167.7-108.8 55.601-53.7 93.7-114.3 114.3-181.9 20.601-67.6 30.9-159.8 30.9-276.8v-239c0-27.599-22.401-50-50-50zM106.036 913.497c65.4-28.5 121-64.699 166.9-108.6 56.1-53.7 94.4-114.1 115-181.2 20.6-67.1 30.899-159.6 30.899-277.5v-239c0-27.6-22.399-50-50-50h-304c-27.6 0-50 22.4-50 50v304c0 27.601 22.4 50 50 50h145.5c-1.9 79.601-20.4 143.3-55.4 191.2-27.6 37.8-69.4 69.1-125.3 93.8-25.7 11.3-36.8 41.7-24.8 67.101l35.9 75.8c11.601 24.399 40.501 35.2 65.301 24.399z"></path>
          </svg>
          <p class="leading-relaxed text-lg">
            音乐不仅是最原始、最普遍的艺术, 而且是最完美的艺术, <br>可以普及深入一般民众,
            从根本上陶冶人的性格。
          </p>
          <p class="mt-4 leading-relaxed text-lg">
            在其他艺术, 实质与形式多少可以分别出来, 了解实质与了解形式可以分为两事;
            音乐却完全融化实质与形式的分别, 实质即形式, 形式亦即实质, 内外一致, 天衣无缝。
          </p>
          <p class="mt-4 leading-relaxed text-lg">
            所以音乐达到了艺术的最高理想。
          </p>
          <span class="inline-block h-1 w-10 rounded bg-emerald-500 mt-4 mb-4"></span>
          <h2 class="text-gray-900 font-medium title-font tracking-wider text-sm pt-16"> 朱光潜 </h2>
          <p class="text-gray-500 mt-2"> 《音乐与教育》 </p>
        </div>
      </div>
    </section>
  </div>
</div>
</template>

<script>
import indexFooter from "@/assets/img/index-footer.jpg";
import axios from "axios";

export default {
  name: "AdminIndex",
  data() {
    return {
      indexFooter,
      searchTag: '',
      musicianList: [
        {
          musicianID: -1,
          musicianName: '',
          photo: '',
          introduction: '',
        }
      ],
      albumList: [
        {
          albumID: -1,
          albumName: '',
          author: '',
          cover: '',
          tagList: [{
            tag: ''
          }]
        }
      ],
      tagList: [
        {
          tag: '',
          tagType: -1,
        }
      ]
    }
  },
  mounted() {
    this.getData();
  },
  methods: {
    search: function (tag) {
      let that = this;
      let toSearch = tag === '' ? that.searchTag : tag;
      console.log(toSearch)
      if (toSearch !== undefined) {
        this.$router.push({
          path: '/admin/search',
          query: {
            target: toSearch,
            type: 'tag'
          }
        })
      }
    },
    getData: function () {
      let that = this;
      axios.request({
        url: "/get_homepage_info/",
        baseURL: '/api',
        method: 'get',
      })
          .then(function (response) {
            that.musicianList = response.data.musicianList
            that.albumList = response.data.albumList
            that.tagList = response.data.tagList
            console.log(response.data.albumList.tagList)
          }).catch(function (error) {
        console.log(error)
      })
    },
    toAlbum: function (aid) {
      this.$router.push({
        path: '/admin/album',
        query: {
          aid: aid
        }
      })
    },
    toMusician: function (mid) {
      this.$router.push({
        path: '/profile',
        query: {
          mid: mid
        }
      })
    }
  }
}
</script>

<style scoped>

</style>