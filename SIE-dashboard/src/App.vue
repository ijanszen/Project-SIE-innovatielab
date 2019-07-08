<template>
  <div id="app">
    <NavBar/>
    <transition v-if="demoStatus == 'on'" name="router-anim" mode="out-in" enter-active-class="animated fadeInRight" leave-active-class="animated fadeOutLeft">
      <router-view class="view"></router-view>
    </transition>

    <router-view class="view" v-if="demoStatus == 'off'"></router-view>

  </div>
</template>

<script>
import NavBar from "./components/layout/NavBar";

export default {
  name: "App",
  components: {
    NavBar,
  },
  data() {
    return {
      demoStatus: "off"
    }
  },
  created() {
    this.$root.$on('clicked', (demoStatus) => {
      this.demoStatus = demoStatus;
    })
  }
};
</script>

<style scoped>
@import "https://cdn.jsdelivr.net/npm/animate.css@3.5.1";

.view {
  margin-top: 2%;
}
</style>
