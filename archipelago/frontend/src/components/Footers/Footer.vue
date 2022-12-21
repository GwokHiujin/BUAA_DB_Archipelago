<template>
  <footer class="relative bg-blueGray-200 pt-8 pb-6">
    <div
      class="bottom-auto top-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden -mt-20 h-20"
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
    <div class="container mx-auto px-4">
      <div class="flex flex-wrap text-center lg:text-left">
        <div class="w-full lg:w-6/12 px-4">
          <h4 class="text-3xl font-semibold">
            Let's keep in touch!
          </h4>
          <h5 class="text-lg mt-5 mb-2 text-blueGray-600">
            如果你对群岛 Archipelago 平台有更好的开发意见,
            欢迎联系我们。
          </h5>
          <div class="flex flex-wrap relative">
          <div class="mt-6 lg:mb-0 mb-6">
            <div
              class="bg-white text-lightBlue-400 text-center p-3 shadow-lg font-normal h-10 w-10 items-center justify-center align-center rounded-full outline-none inline-flex focus:outline-none mr-2"
            >
              <i class="fas fa-envelope"></i>
            </div>
          </div>
          <div class="mt-6 lg:mb-0 mb-6">
            <p class="mt-2 mb-4 text-blueGray-500 px-4">
              20373543@buaa.edu.cn
            </p>
          </div>
          </div>
        </div>
      </div>
      <hr class="my-6 border-blueGray-300" />
      <div
        class="flex flex-wrap items-center md:justify-between justify-center"
      >
        <div class="w-full md:w-4/12 px-4 mx-auto text-center">
          <div class="text-sm text-blueGray-500 font-semibold py-1">
            Copyright © {{ date }} Archipelage by BUAA DATABASE
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      date: new Date().getFullYear(),
    };
  },
};
</script>
