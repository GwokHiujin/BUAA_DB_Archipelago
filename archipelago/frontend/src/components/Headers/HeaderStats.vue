<template>
  <!-- Header -->
  <div class="relative bg-emerald-600 md:pt-32 pb-0 pt-12"
       :style="`background-image: url('${headerBgd}'); background-repeat: repeat;`">
  </div>
</template>

<script>
import headerBgd from "@/assets/img/header-background.png"

export default {
  data() {
    return {
      headerBgd,
    }
  }
};
</script>
