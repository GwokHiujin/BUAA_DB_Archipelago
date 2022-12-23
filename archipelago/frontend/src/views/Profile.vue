<template>
  <div>
    <navbar />
    <main class="profile-page">
      <section class="relative block h-500-px">
        <div
          class="absolute top-0 w-full h-full bg-center bg-cover"
        >
          <img :src="musicianInfo.photo" class="w-full bg-cover bg-center"/>
          <span
            id="blackOverlay"
            class="w-full h-full absolute opacity-50 bg-black"
          ></span>
        </div>

        <div
          class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden h-70-px"
          style="transform: translateZ(0);"
        >
          <svg
            class="absolute bottom-0 overflow-hidden"
            xmlns="http://www.w3.org/2000/svg"
            preserveAspectRatio="none"
            version="1.1"
            viewBox="0 0 2560 100"
            x="0"
            y="0"
          >
            <polygon
              class="text-blueGray-200 fill-current"
              points="2560 0 2560 100 0 100"
            ></polygon>
          </svg>
        </div>
      </section>
      <section class="relative py-16 bg-blueGray-200">
        <div class="container mx-auto px-4">
          <div
            class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg -mt-64"
          >
            <div class="px-6">
              <div class="flex flex-wrap justify-center justify-center">
                <div class="w-full lg:w-4/12 px-4 lg:order-1">
                  <div class="flex justify-center py-4 lg:pt-4 pt-8">
                    <div class="mr-4 p-3 text-center">
                      <span
                          class="text-xl font-bold block uppercase tracking-wide text-blueGray-600"
                      >
                        {{musicianInfo.followerNum}}
                      </span>
                      <span class="text-sm text-blueGray-400">
                        关注者
                      </span>
                    </div>
                    <div class="mr-4 p-3 text-center">
                      <span
                          class="text-xl font-bold block uppercase tracking-wide text-blueGray-600"
                      >
                        2
                      </span>
                      <span class="text-sm text-blueGray-400">
                        唱片数
                      </span>
                    </div>
                    <div class="lg:mr-4 p-3 text-center">
                      <span
                          class="text-xl font-bold block uppercase tracking-wide text-blueGray-600"
                      >
                        1
                      </span>
                      <span class="text-sm text-blueGray-400">
                        评论数
                      </span>
                    </div>
                  </div>
                </div>

                <div
                    class="w-full lg:w-3/12 px-4 lg:order-1 justify-center flex"
                >
                  <div class="relative">
                    <img
                        :src="team2"
                        class="shadow-xl rounded-full h-auto align-middle border-none -m-16 -ml-20 lg:-ml-16 max-w-200-px"
                        v-if="musicianInfo.photo === ''"
                    />
                    <img
                        :src=musicianInfo.avatar
                        class="shadow-xl rounded-full h-auto align-middle border-none -m-16 -ml-20 lg:-ml-16 max-w-200-px"
                        v-else
                    />
                  </div>
                </div>

                <div class="w-full lg:w-4/12 px-4 lg:order-1">
                  <div class="flex justify-center py-4 lg:pt-4 pt-8" v-if="this.$route.query.mid !== this.$cookies.get('mid')">
                    <button class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-sm px-6 py-3 rounded-full shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                            type="button"
                            v-if="followed === false" @click="follow()">
                      <i class="fas fa-heart"></i> 关注
                    </button>
                    <button class="bg-blueGray-600 text-white active:bg-emerald-600 font-bold uppercase text-sm px-6 py-3 rounded-full shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                            type="button"
                            v-if="followed === true" @click="follow()">
                      <i class="fas fa-leaf"></i> 取关
                    </button>
                  </div>
                </div>
              </div>
              <div class="text-center mt-12">
                <h3
                  class="text-5xl font-semibold leading-normal mb-2 text-blueGray-700 pt-12"
                >
                  {{musicianInfo.musicianName}}
                </h3>
                <div
                  class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase"
                >
                  <i
                    class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"
                  ></i>
                  {{musicianInfo.location}}，{{musicianInfo.originCountry}}
                </div>
                <div class="mb-2 text-blueGray-600 mt-10">
                  <i
                    class="fas fa-birthday-cake mr-2 text-lg text-blueGray-400"
                  ></i>
                  成立年份 - {{musicianInfo.formedYear}}
                </div>
                <div class="mb-2 text-blueGray-600">
                  <i
                    class="fas fa-music mr-2 text-lg text-blueGray-400"
                  ></i>
                  创作主题 - {{musicianInfo.lyricalThemes}}
                </div>
              </div>
              <div class="mt-10 py-10 border-t border-blueGray-200 text-center">
                <div class="flex flex-wrap justify-center">
                  <div class="w-full lg:w-9/12 px-4">
                    <p class="mb-4 text-lg leading-relaxed text-blueGray-700">
                      {{musicianInfo.introduction}}
                    </p>
                    <span
                        class="text-xs font-semibold hover:text-emerald-600 inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-100 uppercase last:mr-0 mr-2 mt-2"
                        v-for="tag in musicianTags"
                        @click="search(tag.tag)"
                    >
                      {{tag.tag}}
                    </span>
                  </div>
                </div>
              </div>

              <div class="relative w-full mt-8 pt-8 pb-6">
                <div class="flex flex-wrap mt-4">
                  <div class="w-full px-4">
                    <CardMusicianMems :mid="this.$route.query.mid"/>
                  </div>
                </div>
              </div>

              <div class="relative w-full mt-8 pt-8 pb-16">
                <div class="flex flex-wrap mt-4">
                  <div class="w-full mb-12 px-4">
                    <CardTable :mid="this.$route.query.mid"/>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
    <footer-component />
  </div>
</template>
<script>
import Navbar from "@/components/Navbars/AdminNavbar.vue";
import FooterComponent from "@/components/Footers/Footer.vue";

import team2 from "@/assets/img/team-2-800x800.jpg";
import CardMusicianMems from "@/components/Cards/CardMusicianMems";
import CardTable from "@/components/Cards/CardTable.vue";
import axios from "axios";

export default {
  data() {
    return {
      team2,
      musicianTags: [
        {
          tag: '',
        }
      ],
      musicianInfo: {
        musicianName: '',
        photo: '',
        originCountry: '',
        location: '',
        lyricalThemes: '',
        formedYear: '',
        introduction: '',
        avatar: '',
        followerNum: 0,
      },
      followed: false,
    };
  },
  components: {
    CardMusicianMems,
    Navbar,
    FooterComponent,
    CardTable,
  },
  mounted() {
    this.getMusicianInfo();
    this.getFollowed();
  },
  methods: {
    getMusicianInfo: function () {
      let that = this;
      let musician_id = this.$route.query.mid;
      let data = {
        musicianID: musician_id,
      }
      axios.request({
        url: "api/get_musician/",
        method: 'post',
        data: JSON.stringify(data)
      })
          .then(function (response) {
            console.log(response.data)
            that.musicianInfo = response.data.data
            console.log(that.musicianInfo.followerNum)
          }).catch(function (error) {
        console.log(error)
      })

      data = {
        musicianId: musician_id,
      }
      axios.request({
        url: "api/get_musician_tag/",
        method: 'post',
        data: JSON.stringify(data)
      })
          .then(function (response) {
            console.log(response.data)
            that.musicianTags = response.data.data
          }).catch(function (error) {
        console.log(error)
      })
    },
    search: function (tag) {
      let toSearch = tag;
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
    getFollowed() {
      let that = this;
      let musician_id = this.$route.query.mid;
      let data = {
        musicianID: musician_id,
      }
      axios.request({
        url: "api/test_subscribe/",
        method: 'post',
        data: JSON.stringify(data)
      })
          .then(function (response) {
            console.log(response.data)
            that.followed = response.data.data.exist
          }).catch(function (error) {
        console.log(error)
      })
    },
    follow() {
      this.followed = !this.followed;
      let data = {
        musicianID: this.$route.query.mid,
      };
      axios.request({
        url: "api/subscribe/",
        method: 'post',
        data: JSON.stringify(data)
      })
          .then(function (response) {
            console.log(response.data)
            this.getMusicianInfo();
          }).catch(function (error) {
        console.log(error)
      })
    }
  }
};
</script>
