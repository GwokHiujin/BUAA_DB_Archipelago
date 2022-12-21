<template>
  <div
      class="flex flex-wrap mt-32 flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0"
  >

    <div v-if="showModal"
         class="top-95-px px-12 mx-32 overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex" >
      <div class="relative w-auto my-6 mx-auto max-w-4xl shadow-2xl">
        <!--content-->
        <div class="border-0 rounded-lg shadow-2xl px-3 py-3 relative flex flex-col w-full bg-white outline-none focus:outline-none">
          <!--header-->
          <div class="flex items-start justify-between p-5 text-center border-b border-solid border-blueGray-200 rounded-t">
            <h3 class="text-3xl font-semibold place-content-center ml-auto">
              添加新歌曲
            </h3>
            <button class="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none" @click.native="toggleModal()">
              <span class="bg-transparent text-black hover:text-red-500 opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                ×
              </span>
            </button>
          </div>
          <!--body-->
          <div class="relative px-6 flex-auto py-6">
            <form class="w-card">
              <h6 class="text-blueGray-400 text-sm mt-6 mb-6 font-bold uppercase">
                填写歌曲基础信息 |
              </h6>

              <div class="flex flex-wrap w-full">
                <div class="relative w-full mb-3">
                  <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                  >
                    歌曲名
                  </label>
                  <input
                      type="text"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      id="newSongName"
                  />
                </div>
              </div>

              <div class="flex flex-wrap w-full">
                <div class="relative w-full mb-3">
                  <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                  >
                    歌曲时长（单位：秒）
                  </label>
                  <input
                      type="number"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      id="newSongTime"
                  />
                </div>
              </div>

              <div class="flex flex-wrap w-full">
                <div class="relative w-full mb-3">
                  <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                  >
                    试听链接
                  </label>
                  <input
                      type="text"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      id="newSongADT"
                  />
                </div>
              </div>
            </form>
          </div>
          <!--footer-->
          <div class="flex items-center justify-end p-6 border-t border-solid border-blueGray-200 rounded-b">
            <button
                class="bg-white text-red-500 font-bold uppercase px-6 py-3 text-sm rounded hover:bg-gray-100 outline-none focus:outline-none mr-1 mb-1 mt-4 ease-linear transition-all duration-150"
                type="button"
                @click.native="toggleModal()"
            >
              关闭
            </button>
            <button
                class="bg-blueGray-600 text-white active:bg-red-500 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:bg-red-500 outline-none focus:outline-none mr-1 mb-1 mt-4 ease-linear transition-all duration-150"
                type="button"
                @click.native="addNewSong()"
            >
              添加
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="showModal" class="opacity-25 fixed inset-0 z-40 bg-black"></div>

    <div v-if="alertOpen"
         class="top-95-px px-12 mx-32 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-pink-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
      <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">发布失败！</b> 发布新唱片失败 ☹ 请检查您是否输入了正确的信息！
    </span>
      <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
              @click.native="closeAlert()">
        <span>×</span>
      </button>
    </div>

    <div class="rounded-t bg-white mb-0 px-6 py-6">
      <div class="text-center flex justify-between">
        <h6 class="text-blueGray-700 text-xl font-bold">
          🎼 发布新唱片
        </h6>
        <button
            class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-sm px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
            type="button"
            @click="addNewAlbum()"
        >
          确认发布
        </button>
      </div>
    </div>

    <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
      <form>
        <h6 class="text-blueGray-400 text-sm mt-6 mb-6 font-bold uppercase lg:w-3/12">
          填写唱片基础信息 |
        </h6>

        <div class="flex flex-wrap">
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                唱片名
              </label>
              <input
                  type="text"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  v-model.lazy="discInfo.albumName"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                唱片售价（单位：人民币）
              </label>
              <input
                  type="text"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  v-model.lazy="discInfo.price"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                创作者
              </label>
              <input
                  type="text"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  v-model.lazy="discInfo.author"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                发行年份（填写格式形如“2022“的发行年份）
              </label>
              <input
                  type="text"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  v-model.lazy="discInfo.releaseYear"
              />
            </div>
          </div>
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                上传唱片封面图
              </label>
              <input
                  type="file"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="请上传封面图片"
                  id="album_cover"
                  accept=".jpg,.gif,.png,.bmp"
              />
            </div>
          </div>
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                选择唱片类型
              </label>

              <ul class="flex mb-0 list-none flex-wrap pt-3 pb-4 flex-row">
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal" @click.native="toggleTabs(0)" v-bind:class="{'text-emerald-600 bg-white': openTab !== 0, 'text-white bg-emerald-600': openTab === 0}">
                    EP
                  </a>
                </li>
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal" @click.native="toggleTabs(1)" v-bind:class="{'text-emerald-600 bg-white': openTab !== 1, 'text-white bg-emerald-600': openTab === 1}">
                    Single
                  </a>
                </li>
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal" @click.native="toggleTabs(2)" v-bind:class="{'text-emerald-600 bg-white': openTab !== 2, 'text-white bg-emerald-600': openTab === 2}">
                    Album
                  </a>
                </li>
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal" @click.native="toggleTabs(3)" v-bind:class="{'text-emerald-600 bg-white': openTab !== 3, 'text-white bg-emerald-600': openTab === 3}">
                    Live
                  </a>
                </li>
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal" @click.native="toggleTabs(4)" v-bind:class="{'text-emerald-600 bg-white': openTab !== 4, 'text-white bg-emerald-600': openTab === 4}">
                    Demo
                  </a>
                </li>
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal" @click.native="toggleTabs(5)" v-bind:class="{'text-emerald-600 bg-white': openTab !== 5, 'text-white bg-emerald-600': openTab === 5}">
                    Split
                  </a>
                </li>
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal" @click.native="toggleTabs(6)" v-bind:class="{'text-emerald-600 bg-white': openTab !== 6, 'text-white bg-emerald-600': openTab === 6}">
                    Compilations
                  </a>
                </li>
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal" @click.native="toggleTabs(7)" v-bind:class="{'text-emerald-600 bg-white': openTab !== 7, 'text-white bg-emerald-600': openTab === 7}">
                    Various Artists
                  </a>
                </li>
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal" @click.native="toggleTabs(8)" v-bind:class="{'text-emerald-600 bg-white': openTab !== 8, 'text-white bg-emerald-600': openTab === 8}">
                    Original Soundtrack
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <h6 class="text-blueGray-400 text-sm mt-6 mb-6 font-bold uppercase lg:w-3/12">
          为唱片添加歌曲 |
        </h6>

        <div class="rounded-t mb-0 py-3 border-0">
          <div class="flex flex-wrap items-center flex-row">
            <div class="relative flex-grow flex-1">
              <h3 class="font-semibold text-lg text-blueGray-700 flex-auto">
                🎹 当前唱片拥有歌曲
              </h3>
            </div>
            <div class="relative flex-grow flex-1 text-right">
              <button class="text-emerald-500 flex-auto bg-transparent border border-solid border-gray-200 shadow hover:bg-emerald-500 hover:text-white active:bg-blueGray-600 font-bold uppercase text-xs px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                      type="button"
                      @click="toggleModal()">
                添加新歌曲
              </button>
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
            <tr v-for="song in discInfo.songs">
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

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <div class="flex-auto px-4 lg:px-10 py-10 pt-8 bg-white">
          <form>
            <div class="text-center flex justify-between pb-16">
              <h6 class="text-blueGray-400 text-sm mt-6 mb-6 font-bold uppercase">
                添加标签 | (请以 tag1;tag2;tag3;... 的格式填写，用半角分号区分标签！)
              </h6>
            </div>

            <div class="flex flex-wrap">
              <div class="w-full px-4">
                <div class="relative w-full mb-3">
                  <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                  >
                    风格流派标签
                  </label>
                  <input
                      type="text"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      v-model.lazy="tag0"
                  />
                </div>
              </div>

              <div class="w-full px-4">
                <div class="relative w-full mb-3">
                  <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                  >
                    音乐情绪标签
                  </label>
                  <input
                      type="text"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      v-model.lazy="tag1"
                  />
                </div>
              </div>

              <div class="w-full px-4">
                <div class="relative w-full mb-3">
                  <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                  >
                    器乐元素标签
                  </label>
                  <input
                      type="text"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      v-model.lazy="tag2"
                  />
                </div>
              </div>
            </div>
          </form>
        </div>
      </form>
    </div>

    </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CardAddAlbum",
  data() {
    return {
      alertOpen: false,
      showModal: false,
      tagList: [
        {
          tag: '',
          tagType: 0,
        },
        {
          tag: '',
          tagType: 1,
        },
        {
          tag: '',
          tagType: 2,
        }
      ],
      discInfo: {
        Tag: -1,
        albumName: '',
        price: '',
        author: '',
        releaseYear: '',
        cover: '',
        type: 0,
        resource: '',
        songs: [],
      },
      tag0: '',
      tag1: '',
      tag2: '',
      openTab: 0,
    }
  },
  methods: {
    closeAlert: function() {
      this.alertOpen = false;
    },
    toggleTabs: function (tabNum) {
      console.log(this.openTab)
      let that = this;
      that.discInfo.type = tabNum;
      this.openTab = tabNum;
    },
    toggleModal: function () {
      this.showModal = !this.showModal;
    },
    addNewAlbum: function () {
      let that = this;
      let aid = -1;
      console.log(that.discInfo)
      axios({
        method: 'post',
        url: "/set_album/",
        baseURL: '/api',
        data: JSON.stringify(that.discInfo)
      }).then(res => {
        console.log(res.data)
        aid = res.data.albumID;
      }).catch(err => {
        console.log(err)
      })

      that.tagList.at(0).tag = that.tag0;
      that.tagList.at(1).tag = that.tag1;
      that.tagList.at(2).tag = that.tag2;

      let tagInfo;
      tagInfo = {
        ID: aid,
        tagList: that.tagList,
      };
      axios({
        method: 'post',
        url: "/add_del_album_tag/",
        baseURL: '/api',
        data: JSON.stringify(tagInfo)
      }).then(res => {
        console.log(res.data)
        that.$router.push('/admin/tables')
      }).catch(err => {
        console.log(err)
      })
    },
    addNewSong: function () {
      let that = this;
      let name = document.getElementById("newSongName").value;
      let time = document.getElementById("newSongTime").value;
      let ADT = document.getElementById("newSongADT").value;
      if (name !== '' && time !== '' && ADT !== '') {
        let newData = {
          name: name,
          songLast: time,
          ADT: ADT
        };
        that.discInfo.songs.push(newData);
      }
      this.showModal = false;
      console.log(that.discInfo.songs)
    },
  }
}
</script>

<style scoped>

</style>