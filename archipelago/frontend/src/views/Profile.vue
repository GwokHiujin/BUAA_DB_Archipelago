<template>
  <div>
    <navbar />
    <main class="profile-page">
      <section class="relative block h-500-px">
        <div
          class="absolute top-0 w-full h-full bg-center bg-cover"
          style="
            background-image: url('https://images.unsplash.com/photo-1507838153414-b4b713384a76?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80');
          "
        >
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
              <div class="flex flex-wrap justify-center">
                <div
                  class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center"
                >
                  <div class="relative">
                    <img
                      alt="..."
                      :src="team2"
                      class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px"
                    />
                  </div>
                </div>
                <div
                  class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center"
                >
                  <div class="py-6 px-3 mt-32 sm:mt-0">
                    <button
                      class="bg-emerald-500 active:bg-emerald-600 uppercase text-white font-bold hover:shadow-md shadow text-sm px-6 py-2 rounded outline-none focus:outline-none sm:mr-2 mb-1 ease-linear transition-all duration-150"
                      type="button"
                    >
                      <i
                          class="fas fa-heart mr-2 text-white"
                      ></i>
                      关注
                    </button>
                    <button
                        class="bg-blueGray-200 active:bg-blueGray-600 uppercase text-blueGray-400 font-bold hover:shadow-md shadow text-sm px-6 py-2 rounded outline-none focus:outline-none sm:mr-2 mb-1 ease-linear transition-all duration-150"
                        type="button"
                        v-if="this.$cookies.get('userInfo_usertype') === '1'"
                    >
                      <i
                          class="fas fa-pen mr-2 text-blueGray-400"
                      ></i>
                      编辑
                    </button>
                  </div>
                </div>
                <div class="w-full lg:w-4/12 px-4 lg:order-1">
                  <div class="flex justify-center py-4 lg:pt-4 pt-8">
                    <div class="mr-4 p-3 text-center">
                      <span
                        class="text-xl font-bold block uppercase tracking-wide text-blueGray-600"
                      >
                        22
                      </span>
                      <span class="text-sm text-blueGray-400">
                        关注者
                      </span>
                    </div>
                    <div class="mr-4 p-3 text-center">
                      <span
                        class="text-xl font-bold block uppercase tracking-wide text-blueGray-600"
                      >
                        10
                      </span>
                      <span class="text-sm text-blueGray-400">
                        唱片数
                      </span>
                    </div>
                    <div class="lg:mr-4 p-3 text-center">
                      <span
                        class="text-xl font-bold block uppercase tracking-wide text-blueGray-600"
                      >
                        89
                      </span>
                      <span class="text-sm text-blueGray-400">
                        被购买数
                      </span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="text-center mt-12">
                <h3
                  class="text-5xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2"
                >
                  向北航行 BUAA
                </h3>
                <div
                  class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase"
                >
                  <i
                    class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"
                  ></i>
                  北京，中国
                </div>
                <div class="mb-2 text-blueGray-600 mt-10">
                  <i
                    class="fas fa-birthday-cake mr-2 text-lg text-blueGray-400"
                  ></i>
                  成立年份 - 2022
                </div>
                <div class="mb-2 text-blueGray-600">
                  <i
                    class="fas fa-music mr-2 text-lg text-blueGray-400"
                  ></i>
                  音乐风格 - 校园民谣
                </div>
              </div>
              <div class="mt-10 py-10 border-t border-blueGray-200 text-center">
                <div class="flex flex-wrap justify-center">
                  <div class="w-full lg:w-9/12 px-4">
                    <p class="mb-4 text-lg leading-relaxed text-blueGray-700">
                      我们是一支来自北京航空航天大学的校园民谣乐队，希望大家能够喜欢我们的音乐！
                    </p>
                    <span
                        class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-100 uppercase last:mr-0 mr-2 mt-2"
                        v-for="tag in musicianTags"
                    >
                      {{tag.value}}
                    </span>
                  </div>
                </div>
              </div>

              <CardMusicianMems/>

              <div class="relative w-full mt-8 pt-8 pb-16">
                <div class="text-center">
                  <router-link to="/admin/tables">
                  <button
                      class="mx-8 bg-emerald-500 text-white focus:bg-blueGray-800 active:bg-emerald-600 font-bold uppercase text-sm px-4 py-4 rounded-full shadow hover:shadow-lg outline-none mb-1 ease-linear transition-all duration-150"
                      type="button"
                  >
                    <i class="fas fa-guitar mr-2"></i> 探索该音乐人的唱片页
                  </button>
                  </router-link>
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
import Navbar from "@/components/Navbars/AuthNavbar.vue";
import FooterComponent from "@/components/Footers/Footer.vue";
import CardTable from "@/components/Cards/CardTable";

import team2 from "@/assets/img/team-2-800x800.jpg";
import CardMusicianMems from "../components/Cards/CardMusicianMems";

export default {
  data() {
    return {
      team2,
      musicianTags: [
        {
          value: "校园民谣"
        },
        {
          value: "欢快清新"
        },
        {
          value: "怀旧"
        },
        {
          value: "木吉他"
        }
      ]
    };
  },
  components: {
    CardMusicianMems,
    Navbar,
    FooterComponent,
    CardTable,
  },
};
</script>
