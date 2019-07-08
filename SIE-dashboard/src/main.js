import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueRouter from 'vue-router'
import ToggleButton from 'vue-js-toggle-button'

import Netatmo from './components/view/Netatmo'
import NanoLeaf from './components/view/NanoLeaf'
import Home from './components/view/Home'
import LaMetric from './components/view/LaMetric'
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
    { path: '/', redirect: { name: 'home' } },
    { path: '/home', name: 'home', component: Home },
    { path: '/lametric', redirect: { name: 'lametric' } },
    { path: '/lametric', name: 'lametric', component: LaMetric },
    { path: '/netatmo', redirect: { name: 'netatmo' } },
    { path: '/netatmo', name: 'netatmo', component: Netatmo },
    { path: '/nanoleaf', redirect: { name: 'nanoleaf' } },
    { path: '/nanoleaf', name: 'nanoleaf', component: NanoLeaf },
    { path: '/about', redirect: { name: 'about' } },
    { path: '/about', name: 'about', component: About },
    { path: "*", component: Home },
  ]
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

