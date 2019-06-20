<template>
  <div id="app">
    <NavBar/>
    <router-view class="view"></router-view>
  </div>
</template>

<script>
import NavBar from "./components/layout/NavBar";

export default {
  name: "App",
  components: {
    NavBar
  }
};
</script>

<style scoped>
.view {
  margin-top: 2%;
}
</style>
