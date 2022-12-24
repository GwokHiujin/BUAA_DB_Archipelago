<template>
<div class="flex-wrap flex mt-10">
  <section class="text-gray-600 body-font mt-24 w-full" v-if="followList.length !== 0">
    <div class="flex flex-wrap -m-2 w-full">
      <div class="p-2 lg:w-4/12 md:w-6/12 w-full" v-for="follow in followList">
        <div class="h-full flex items-center border-gray-200 border-b-2 p-4 hover:bg-gray-100 ease-linear transition">
          <img alt="team" class="w-16 h-16 bg-gray-100 object-cover object-center flex-shrink-0 rounded-full mr-4"
               :src=follow.avatar>
          <div class="flex-grow">
            <h2 class="text-gray-900 title-font font-medium hover:text-emerald-600"
                @click="gotoMusician(follow.musicianID)">
              {{follow.musicianName}}
            </h2>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="text-gray-600 body-font mx-64" v-else>
    <div class="container px-5 py-24 mx-auto justify-center">
      <div class="xl:w-1/2 lg:w-3/4 w-full mx-auto text-center mt-16">
        <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="inline-block w-8 h-8 text-gray-400 mb-8" viewBox="0 0 975.036 975.036">
          <path d="M925.036 57.197h-304c-27.6 0-50 22.4-50 50v304c0 27.601 22.4 50 50 50h145.5c-1.9 79.601-20.4 143.3-55.4 191.2-27.6 37.8-69.399 69.1-125.3 93.8-25.7 11.3-36.8 41.7-24.8 67.101l36 76c11.6 24.399 40.3 35.1 65.1 24.399 66.2-28.6 122.101-64.8 167.7-108.8 55.601-53.7 93.7-114.3 114.3-181.9 20.601-67.6 30.9-159.8 30.9-276.8v-239c0-27.599-22.401-50-50-50zM106.036 913.497c65.4-28.5 121-64.699 166.9-108.6 56.1-53.7 94.4-114.1 115-181.2 20.6-67.1 30.899-159.6 30.899-277.5v-239c0-27.6-22.399-50-50-50h-304c-27.6 0-50 22.4-50 50v304c0 27.601 22.4 50 50 50h145.5c-1.9 79.601-20.4 143.3-55.4 191.2-27.6 37.8-69.4 69.1-125.3 93.8-25.7 11.3-36.8 41.7-24.8 67.101l35.9 75.8c11.601 24.399 40.501 35.2 65.301 24.399z"></path>
        </svg>
        <p class="leading-relaxed text-lg">
          您还没有关注音乐人哦…去主页探索一下？
        </p>
        <span class="inline-block h-1 w-10 rounded bg-indigo-500 mt-8 mb-6"></span>
      </div>
    </div>
  </section>
</div>
</template>

<script>
import axios from "axios";

export default {
  name: "Follows",
  data() {
    return {
      followList: [
        {
          musicianID: -1,
          musicianName: '',
          avatar: '',
        }
      ]
    }
  },
  mounted() {
    this.getFollowList();
  },
  methods: {
    getFollowList: function () {
      let that = this;
      axios.request({
        url: "/get_subscribe/",
        baseURL: '/api',
        method: 'get',
      })
          .then(function (response) {
            console.log(response.data)
            that.followList = response.data.concernList
          }).catch(function (error) {
        console.log(error)
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
    }
  }
}
</script>

<style scoped>

</style>