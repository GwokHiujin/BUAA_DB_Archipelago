<template>
  <div
    class="flex flex-wrap mt-32 flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg mt-16"
  >
    <div class="px-6">
      <div class="flex flex-wrap justify-center">
        <div class="w-full px-4 flex justify-center">
          <div class="relative">
            <img
                alt="..."
                :src="userInfo.avatar"
                class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px"
            />
          </div>
        </div>
        <div class="w-full px-4 text-center mt-20">
        </div>
      </div>
      <div class="text-center mt-12">
        <h3
          class="text-xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2"
        >
          {{userInfo.name}}
        </h3>
        <div class="mb-2 text-blueGray-600 mt-10"
             v-if="userInfo.type === `1`">
          <i class="fas fa-microphone mr-2 text-lg text-blueGray-400"></i>
          音乐人用户
        </div>
        <div class="mb-2 text-blueGray-600 mt-10"
             v-else>
          <i class="fas fa-music mr-2 text-lg text-blueGray-400"></i>
          普通用户
        </div>
      </div>
      <div class="mt-10 py-10 border-t border-blueGray-200 text-center">
        <div class="flex flex-wrap justify-center">
          <div class="w-full lg:w-9/12 px-4">
            <p class="mb-4 text-lg leading-relaxed text-blueGray-700">
              {{userInfo.bio}}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import team2 from "@/assets/img/team-2-800x800.jpg";
import axios from "axios";

export default {
  data() {
    return {
      team2,
      userInfo: {
        name: '',
        avatar: '-1',
        type: '',
        bio: ''
      },
    };
  },
  mounted() {
    this.getUserInfo();
    console.log(this.userInfo.avatar)
  },
  methods: {
    getUserInfo: function () {
      let that = this;
      axios.request({
        url: "/get_user_info/",
        baseURL: '/api',
        method: 'get'
      })
          .then(function (response) {
            console.log(response.data)
            that.userInfo = response.data.data
          }).catch(function (error) {
        console.log(error)
      })
    }
  },
};
</script>
