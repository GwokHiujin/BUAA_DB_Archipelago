<template>
<div class="flex-wrap flex mt-10">
  <section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
      <div class="flex flex-wrap -m-2"
           v-for="follow in followList">
        <div class="p-2 lg:w-1/3 md:w-1/2 w-full">
          <div class="h-full flex items-center border-gray-200 border p-4 rounded-lg">
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
    </div>
  </section>
</div>
</template>

<script>
export default {
  name: "Follows",
  data() {
    return {
      followList: [
        {
          musicianID: -1,
          musicianName: "Havok",
          avatar: 'https://images.unsplash.com/photo-1507808973436-a4ed7b5e87c9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80',
        }
      ]
    }
  },
  mounted() {
    this.getFollowList();
  },
  methods: {
    getFollowList: function () {

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