<template>
  <div id="app">
    <NavBar/>
    <transition name="router-anim" mode="out-in" enter-active-class="animated fadeIn" leave-active-class="animated fadeOut">
      <router-view class="view"></router-view>
    </transition>
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
      text: "hello"
    }
  },
  created() {
    this.$root.$on('send', (text) => {
      console.log(this.text)
      this.text = text;
      console.log(this.text)
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
