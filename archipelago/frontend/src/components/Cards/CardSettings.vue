<template>
  <div class="w-full flex-wrap flex justify-center">
  <div
    class="flex flex-wrap mt-32 flex-col break-words mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0 lg:w-8/12"
  >
    <div v-if="showModal"
         class="top-25-px px-12 mx-32 overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex" >
      <div class="relative w-auto my-6 mx-auto max-w-4xl shadow-2xl">
        <!--content-->
        <div class="border-0 rounded-lg shadow-2xl px-3 py-3 relative flex flex-col w-full bg-white outline-none focus:outline-none">
          <!--header-->
          <div class="flex items-start justify-between p-5 text-center border-b border-solid border-blueGray-200 rounded-t">
            <h3 class="text-3xl font-semibold place-content-center ml-auto">
              添加新成员
            </h3>
            <button class="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none" v-on:click="toggleModal()">
              <span class="bg-transparent text-black hover:text-red-500 opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                ×
              </span>
            </button>
          </div>
          <!--body-->
          <div class="relative px-6 flex-auto py-6">
            <form class="w-card">
              <h6 class="text-blueGray-400 text-sm mt-6 mb-6 font-bold uppercase">
                填写成员基础信息 |
              </h6>

              <div class="flex flex-wrap w-full">
                <div class="relative w-full mb-3">
                  <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                  >
                    名称
                  </label>
                  <input
                      type="text"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      v-model.lazy="musicianMember.name"
                  />
                </div>
              </div>

              <div class="flex flex-wrap w-full">
                <div class="relative w-full mb-3">
                  <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                  >
                    生日
                  </label>
                  <input
                      type="date"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      v-model.lazy="musicianMember.birthday"
                  />
                </div>
              </div>

              <div class="flex flex-wrap w-full">
                <div class="relative w-full mb-3">
                  <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                  >
                    职务 / 角色(如: 吉他手)
                  </label>
                  <input
                      type="text"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      v-model.lazy="musicianMember.role"
                  />
                </div>
              </div>

              <div class="flex flex-wrap w-full">
                <div class="relative w-full mb-3">
                  <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                  >
                    活跃年份(格式为形如 2002-2022 或 2002-今 的字符串)
                  </label>
                  <input
                      type="text"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      v-model.lazy="musicianMember.activeYear"
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
                v-on:click="toggleModal()"
            >
              关闭
            </button>
            <button
                class="bg-blueGray-600 text-white active:bg-red-500 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:bg-red-500 outline-none focus:outline-none mr-1 mb-1 mt-4 ease-linear transition-all duration-150"
                type="button"
                v-on:click="setMusicianMember()"
            >
              添加
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="showModal" class="opacity-25 fixed inset-0 z-40 bg-black"></div>

    <div v-if="showModal1"
         class="top-25-px px-12 mx-32 overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex" >
      <div class="relative w-auto my-6 mx-auto max-w-4xl shadow-2xl">
        <!--content-->
        <div class="border-0 rounded-lg shadow-2xl px-3 py-3 relative flex flex-col w-full bg-white outline-none focus:outline-none">
          <!--header-->
          <div class="flex items-start justify-between p-5 text-center border-b border-solid border-blueGray-200 rounded-t">
            <h3 class="text-3xl font-semibold place-content-center ml-auto">
              删除成员
            </h3>
            <button class="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none" v-on:click="toggleModal1()">
              <span class="bg-transparent text-black hover:text-red-500 opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                ×
              </span>
            </button>
          </div>
          <!--body-->
          <div class="relative px-6 flex-auto py-6">
            <form class="w-card">
              <h6 class="text-blueGray-400 text-sm mt-6 mb-6 font-bold uppercase">
                提交需要删除的成员名称 |
              </h6>

              <div class="flex flex-wrap w-full">
                <div class="relative w-full mb-3">
                  <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="grid-password"
                  >
                    名称
                  </label>
                  <input
                      type="text"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="请输入需要删除的成员的名称"
                      v-model.lazy="toBeDelete"
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
                v-on:click="toggleModal1()"
            >
              关闭
            </button>
            <button
                class="bg-blueGray-600 text-white active:bg-red-500 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:bg-red-500 outline-none focus:outline-none mr-1 mb-1 mt-4 ease-linear transition-all duration-150"
                type="button"
                v-on:click="deleteMusicianMember()"
            >
              删除
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="showModal1" class="opacity-25 fixed inset-0 z-40 bg-black"></div>

    <div v-if="alertOpen"
         class="top-95-px px-12 mx-32 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-pink-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
      <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">修改失败！</b> 修改用户信息失败 ☹ 请检查您是否输入了正确的信息！
    </span>
      <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
              v-on:click="closeAlert()">
        <span>×</span>
      </button>
    </div>

    <div v-if="alertOpen1"
         class="top-95-px px-12 mx-32 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-pink-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
      <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">修改失败！</b> 修改音乐人信息失败 ☹ 请检查您是否输入了正确的信息！
    </span>
      <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
              v-on:click="closeAlert1()">
        <span>×</span>
      </button>
    </div>

    <div v-if="alertOpen2"
         class="top-95-px px-12 mx-32 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-pink-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
      <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">修改失败！</b> 修改音乐人成员失败 ☹ 请检查您是否输入了正确的信息！
    </span>
      <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
              v-on:click="closeAlert2()">
        <span>×</span>
      </button>
    </div>

    <div v-if="alertOpen3"
         class="top-95-px px-12 mx-32 md:w-6/12 overflow-x-hidden overflow-y-auto rounded fixed inset-0 z-50 outline-none text-white py-4 border-0 fixed bg-emerald-500 justify-center items-center flex">
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell"></i>
    </span>
      <span class="inline-block align-middle mr-8 px-2">
      <b class="capitalize">修改成功！</b> 修改信息成功 👓
    </span>
      <button class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
              v-on:click="closeAlert3()">
        <span>×</span>
      </button>
    </div>

    <div class="rounded-t bg-white mb-0 px-6 py-6">
      <div class="text-center flex justify-between">
        <h6 class="text-blueGray-700 text-xl font-bold">欢迎您，{{userInfo.name}}！</h6>
        <span
            class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-200 uppercase last:mr-0 mr-2 mt-2"
            v-if="userInfo.type === `1`"
        >
          音乐人用户
        </span>
        <span
            class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-200 uppercase last:mr-0 mr-2 mt-2"
            v-else
        >
          普通用户
        </span>
        <button
          class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
          type="button"
          @click="setUserInfo()"
        >
          提交用户信息修改
        </button>
      </div>
    </div>
    <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
      <form>
        <h6 class="text-blueGray-400 text-sm mt-6 mb-6 font-bold uppercase">
          修改用户信息
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                用户名
              </label>
              <input
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                v-model.lazy="userInfo.name"
                :placeholder="userInfo.name"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                邮箱
              </label>
              <p
                class="border-0 px-3 py-3 text-blueGray-600 bg-white rounded text-sm shadow w-full"
              >
                {{userInfo.email}}
              </p>
            </div>
          </div>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
          修改密码
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                旧密码
              </label>
              <input
                type="password"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                placeholder="请输入旧密码"
                v-model.lazy="old_password"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                新密码
              </label>
              <input
                type="password"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                placeholder="请输入新密码"
                v-model.lazy="new_password1"
              />
            </div>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                确认新密码
              </label>
              <input
                type="password"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                placeholder="请确认新密码"
                v-model.lazy="new_password2"
              />
            </div>
          </div>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
          修改头像图片
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                上传头像图片
              </label>
              <input
                  type="file"
                  class="upload"
                  @change="readAvatarFile($event)"
                  accept="image/*"
                  placeholder="请上传头像图片"
              />
            </div>
          </div>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
          修改个性签名
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <textarea
                type="text"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                rows="4"
                :placeholder="userInfo.bio"
                v-model.lazy="userInfo.bio"
              >
                  </textarea
              >
            </div>
          </div>
        </div>
      </form>
    </div>

    <hr class="mt-6 border-b border-blueGray-50" v-if="userInfo.type === '1'"/>

    <!--Musician Info-->
    <div class="flex-auto px-4 lg:px-10 py-10 pt-8 bg-white" v-if="userInfo.type === '1'">
      <form>
        <div class="text-center flex justify-between">
          <h6 class="text-blueGray-700 text-xl font-bold">音乐人基本信息</h6>
          <button
              class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
              type="button"
              @click="setMusicianInfo()"
          >
            提交音乐人信息修改
          </button>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <h6 class="text-blueGray-400 text-sm mt-6 mb-6 font-bold uppercase">
          修改音乐人信息
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                音乐人名称
              </label>
              <input
                  type="text"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  v-model.lazy="musicianInfo.musicianName"
              />
            </div>
          </div>

          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                音乐人国籍
              </label>
              <input
                  type="text"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  v-model.lazy="musicianInfo.originCountry"
              />
            </div>
          </div>

          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                音乐人所在地区
              </label>
              <input
                  type="text"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  v-model.lazy="musicianInfo.location"
              />
            </div>
          </div>

          <div class="w-full lg:w-6/12 px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                音乐人成立年份
              </label>
              <input
                  type="date"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  v-model.lazy="musicianInfo.formedYear"
              />
            </div>
          </div>

          <div class="w-full px-4">
            <div class="relative w-full mb-3">
              <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
              >
                音乐人照片
              </label>
              <input
                  type="file"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="请上传音乐人照片"
                  @change="readPhotoFile($event)"
                  accept="image/*"
              />
            </div>
          </div>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <h6 class="text-blueGray-400 text-sm mt-6 mb-6 font-bold uppercase">
          修改音乐人创作主题
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <textarea
                  type="text"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  rows="4"
                  v-model.lazy="musicianInfo.lyricalThemes"
                  placeholder="请输入您的创作主题"
              >
                  </textarea
                  >
            </div>
          </div>
        </div>

        <hr class="mt-6 border-b-1 border-blueGray-300" />

        <h6 class="text-blueGray-400 text-sm mt-6 mb-6 font-bold uppercase">
          修改音乐人介绍信息
        </h6>
        <div class="flex flex-wrap">
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <textarea
                  type="text"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  rows="4"
                  v-model.lazy="musicianInfo.introduction"
              >
                  </textarea
                  >
            </div>
          </div>
        </div>

      </form>
    </div>

    <!--Musician Member-->
    <div class="flex-auto px-4 lg:px-10 py-10 pt-8" v-if="userInfo.type === '1'">
      <form>
        <div class="text-center flex justify-between pb-16">
          <h6 class="text-blueGray-700 text-xl font-bold">音乐人成员信息</h6>
          <div>
            <button
                class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                type="button"
                @click="toggleModal()"
            >
              添加成员
            </button>
            <button
                class="bg-blueGray-600 text-white active:bg-red-500 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md hover:bg-red-500 outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
                type="button"
                @click="toggleModal1()"
            >
              删除成员
            </button>
          </div>
        </div>

        <div class="rounded-t mb-0 py-3 border-0 flex-wrap flex">
          <CardMusicianMems :mid="this.$cookies.get('mid')" :key="componentKey"/>
        </div>
      </form>
    </div>

    <hr class="mt-6 border-b-1 border-0" v-if="userInfo.type === '1'"/>

    <div class="flex-auto px-4 lg:px-10 py-10 pt-8 bg-white" v-if="userInfo.type === '1'">
      <form>
        <div class="text-center flex justify-between">
          <h6 class="text-blueGray-700 text-xl font-bold">音乐人标签信息</h6>
          <button
              class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150"
              type="button"
              @click="addMusicianTags()"
          >
            提交标签信息修改
          </button>
        </div>

        <div class="text-center flex justify-between">
          <h6 class="text-blueGray-400 text-sm mt-6 mb-6 font-bold uppercase ml-3">
            请以 tag1;tag2;tag3;... 的格式填写，用分号区分标签
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
  </div>

    <div class="lg:w-4/12 px-8 pt-20">
      <CardProfile :key="componentKey2"/>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CryptoJS from 'crypto-js'
import CardMusicianMems from "@/components/Cards/CardMusicianMems.vue";
import CardProfile from "@/components/Cards/CardProfile.vue";

axios.defaults.withCredentials = true;

export default {
  name: "settings",
  components: {
    CardMusicianMems,
    CardProfile,
  },
  data() {
    return {
      userInfo: {
        email: '',
        name: '',
        avatar: '',
        type: '',
        bio: ''
      },
      musicianInfo: {
        musicianName: '',
        photo: '',
        originCountry: '',
        location: '',
        lyricalThemes: '',
        formedYear: '',
        introduction: '',
      },
      musicianMember: {
        musicianID: '',
        name: '',
        birthday: '',
        role: '',
        activeYear: '',
      },
      old_password: '',
      new_password1: '',
      new_password2: '',
      alertOpen: false,
      alertOpen1: false,
      alertOpen2: false,
      alertOpen3: false,
      showModal: false,
      showModal1: false,
      toBeDelete: '',
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
      tag0: '',
      tag1: '',
      tag2: '',
      componentKey: 0,
      componentKey1: 0,
      componentKey2: 0,
    }
  },
  mounted() {
    this.getUserInfo();
    if (this.$cookies.get("userInfo_usertype") === '1') {
      this.getMusicianInfo();
    }
  },
  methods: {
    closeAlert: function() {
      this.alertOpen = false;
    },
    closeAlert1: function () {
      this.alertOpen1 = false;
    },
    closeAlert2: function () {
      this.alertOpen2 = false;
    },
    closeAlert3: function () {
      this.alertOpen3 = false;
      this.componentKey1 += 1;
      this.componentKey2 += 1;
      this.$emit('change', this.componentKey1);
    },
    toggleModal: function () {
      this.showModal = !this.showModal;
    },
    toggleModal1: function () {
      this.showModal1 = !this.showModal1;
    },
    getUserInfo: function () {
      let that = this;
      axios.request({
        url: "/get_user_info/",
        baseURL: '/api',
        method: 'get'
      })
          .then(function (response) {
            that.userInfo = response.data.data
            console.log(that.userInfo)
            that.$cookies.set("userInfo_bio", response.data.data.bio, '', '/')
            that.$cookies.set("userInfo_avatar", response.data.data.avatar, '', '/')
            that.$cookies.set("userInfo_username", response.data.data.name, '', '/')
            console.log(response.data.data.name)
          }).catch(function (error) {
        console.log(error)
      })
    },
    getMusicianInfo: function () {
      let that = this;
      axios.request({
        url: "/get_musician/",
        baseURL: '/api',
        method: 'get',
      })
          .then(function (response) {
            console.log(response.data)
            that.musicianInfo = response.data.data
          }).catch(function (error) {
        console.log(error)
      })
    },
    setUserInfo: function () {
      let newUserInfo;
      let that = this;
      if (that.new_password1 !== that.new_password2) {
        that.alertOpen = true;
      } else {
        let old_pwd_key = this.$cookies.get("userInfo_password");
        let new_pwd_key = this.$cookies.get("userInfo_password");
        if (that.new_password1 !== '' && that.new_password2 !== ''
            && that.new_password1 !== undefined && that.new_password2 !== undefined) {
          old_pwd_key = CryptoJS.AES.encrypt(that.old_password, CryptoJS.enc.Utf8.parse(that.$cookies.get("aseKey")), {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
          }).toString();
          new_pwd_key = CryptoJS.AES.encrypt(that.new_password1, CryptoJS.enc.Utf8.parse(that.$cookies.get("aseKey")), {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
          }).toString();
        }

        newUserInfo = {
          name: that.userInfo.name,
          avatar: that.userInfo.avatar,
          oldPassword: old_pwd_key,
          password: new_pwd_key,
          bio: that.userInfo.bio
        };

        axios({
          url: "/set_user_info/",
          baseURL: '/api',
          method: 'post',
          data: JSON.stringify({newUserInfo})
        }).then(res => {
          console.log(res.data)
          if (res.data.errno === 0) {
            this.alertOpen3 = true;
            this.getUserInfo();
            this.componentKey1 += 1;
            this.$emit('change', this.componentKey1);
          } else {
            console.log(res.data)
            that.alertOpen = true;
          }
        }).catch(err => {
          console.log(err)
        })
      }
    },
    setMusicianInfo: function () {
      let that = this;
      axios({
        method: 'post',
        url: "/set_musician/",
        baseURL: '/api',
        data: JSON.stringify(that.musicianInfo)
      }).then(res => {
        console.log(res.data)
        if (res.data.errno === 0) {
          this.alertOpen3 = true;
          console.log("hey")
          that.$router.push({
            path: '/profile',
            query: {
              mid: this.$cookies.get("mid")
            }
          })
        } else {
          that.alertOpen1 = true;
        }
      }).catch(err => {
        console.log(err)
      })
    },
    setMusicianMember: function () {
      let that = this;
      that.musicianMember.musicianID = that.$cookies.get("mid")
      console.log(that.musicianMember.musicianID)
      axios({
        method: 'post',
        url: "/add_musician_member/",
        baseURL: '/api',
        data: JSON.stringify(that.musicianMember)
      }).then(res => {
        console.log(res.data)
        if (res.data.errno === 0) {
          this.alertOpen3 = true;
          that.showModal = false;
          this.componentKey += 1;
        } else {
          that.alertOpen2 = true;
          console.log(res.data.msg)
        }
        that.$router.push("/admin/settings")
      }).catch(err => {
        console.log(err)
      })
    },
    deleteMusicianMember: function () {
      let that = this;
      let data = {
        name: that.toBeDelete
      };
      axios({
        method: 'post',
        url: "/del_musician_member/",
        baseURL: '/api',
        data: JSON.stringify(data)
      }).then(res => {
        console.log(res.data)
        if (res.data.errno === 0) {
          that.showModal1 = false;
          this.alertOpen3 = true;
          this.componentKey += 1;
        } else {
          this.alertOpen2 = true;
        }
      }).catch(err => {
        console.log(err)
      })
    },
    addMusicianTags: function () {
      let that = this;
      let tagInfo;

      that.tagList.at(0).tag = that.tag0;
      that.tagList.at(1).tag = that.tag1;
      that.tagList.at(2).tag = that.tag2;

      tagInfo = {
        ID: that.$cookies.get("mid"),
        tagList: that.tagList,
      };
      axios({
        method: 'post',
        url: "/set_musician_tag/",
        baseURL: '/api',
        data: JSON.stringify(tagInfo)
      }).then(res => {
        if (res.data.errno === 0) {
          console.log(res.data)
          that.tagList = []
          this.alertOpen3 = true;
          that.$router.push("/admin/settings")
        }
      }).catch(err => {
        console.log(err)
      })
    },
    readAvatarFile(e) {
      const file = e.target.files[0];
      const formData = new FormData();
      formData.append("file", file);
      console.log(formData)
      axios({
        method: 'post',
        url: "/upload_img/",
        baseURL: '/api',
        data: formData
      }).then(res => {
        console.log(res.data)
        this.userInfo.avatar = res.data.img_url;
      }).catch(err => {
        console.log(err)
      })
    },
    readPhotoFile(e) {
      const file = e.target.files[0];
      const formData = new FormData();
      formData.append("file", file);
      console.log(formData)
      axios({
        method: 'post',
        url: "/upload_img/",
        baseURL: '/api',
        data: formData
      }).then(res => {
        console.log(res.data)
        this.musicianInfo.photo = res.data.img_url
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>
