import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueRouter from 'vue-router'
import ToggleButton from 'vue-js-toggle-button'

import Netatmo from './components/view/Netatmo'
import NanoLeaf from './components/view/NanoLeaf'
import Home from './components/view/Home'
import FlowerPot from './components/view/FlowerPot'
import About from './components/view/About'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(VueRouter)
Vue.use(ToggleButton)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', redirect: { name: 'netatmo' } },
    { path: '/home', name: 'home', component: Home },
    { path: '/flowerpot', name: 'flowerpot', component: FlowerPot },
    { path: '/netatmo', name: 'netatmo', component: Netatmo },
    { path: '/nanoleaf', name: 'projectdetails', component: NanoLeaf },
    { path: '/about', name: 'about', component: About },
    { path: "*", component: Home }
  ]
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

