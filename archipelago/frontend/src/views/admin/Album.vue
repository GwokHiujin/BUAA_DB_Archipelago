<template>
<div class="flex flex-wrap pt-12">
  <section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
      <div class="lg:w-4/5 mx-auto flex flex-wrap">
        <img alt="ecommerce" class="lg:w-6/12 w-full lg:h-auto h-64 object-cover object-center rounded" src="https://dummyimage.com/400x400">
        <div class="lg:w-6/12 w-full lg:pl-10 lg:py-6 mt-6 lg:mt-0 pl-10">
          <h2 class="text-sm title-font text-gray-500 tracking-widest">
            Album release Year
          </h2>
          <h1 class="text-gray-900 text-3xl title-font font-medium mb-1">
            Album Name
          </h1>
          <div class="flex mb-4">
          <span class="flex items-center text-gray-600">
            4 Sold
          </span>
          <span class="flex ml-3 pl-3 py-2 border-l-2 border-gray-200 space-x-2s text-gray-500">
            Album Releaser
          </span>
          </div>
          <p class="leading-relaxed">Fam locavore kickstarter distillery. Mixtape chillwave tumeric sriracha taximy chia microdosing tilde DIY. XOXO fam indxgo juiceramps cornhole raw denim forage brooklyn. Everyday carry +1 seitan poutine tumeric. Gastropub blue bottle austin listicle pour-over, neutra jean shorts keytar banjo tattooed umami cardigan.</p>
          <div class="flex mt-6 items-center pb-5 border-b-2 border-gray-100 mb-5 pb-6">
            <span
                class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-100 uppercase last:mr-0 mr-2 mt-2"
                v-for="tag in albumTags"
            >
              {{tag.value}}
            </span>
          </div>
          <div class="flex">
            <span class="title-font font-medium text-2xl text-gray-900">
              ￥ Album Price
            </span>
            <button class="flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded active:bg-blueGray-600 ease-linear">
              购买
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="text-gray-600 body-font w-full px-12">
    <div class="container px-5 mx-auto">
    <div class="flex flex-wrap mt-6 flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-100 border-0">
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
          <tr >
            <td
                class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
            >
              test
            </td>

            <td
                class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
            >
              test
            </td>

            <td
                class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
            >
              test
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    </div>
  </section>
</div>
</template>

<script>
export default {
  name: "Album",
  data() {
    return {
      albumTags: [
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
    }
  }
}
</script>

<style scoped>

</style>