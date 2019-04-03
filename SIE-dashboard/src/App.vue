<template>
  <div id="app">
    <NavBar />
     <router-view class="view"></router-view>
    <carousel :per-page="1" :navigate-to="someLocalProperty" :mouse-drag="false" :autoplay="true" :autoplayTimeout="10000" :loop="true">
      <slide>
        <Home />
      </slide>
      <slide>
        Slide 2 Content
      </slide>
    </carousel>
  </div>
</template>

<script>
import NavBar from './components/layout/NavBar'
import Home from './components/view/Home';

import Vue from 'vue';
import VueCarousel from 'vue-carousel';

Vue.use(VueCarousel);

export default {
  name: 'App',
  components: {
    NavBar,
    Home
  }
}
</script>