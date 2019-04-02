import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueRouter from 'vue-router' 

import Netatmo from './components/view/Netatmo'
import NanoLeaf from './components/view/NanoLeaf'
import Home from './components/view/Home'
import FlowerPot from './components/view/FlowerPot'


// Import base styles
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(VueRouter)
const NotFound = { template: '<h1> Page not found, how did you get here? </h1>' }

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {path: '/', redirect: { name: 'netatmo' }},
    {path: '/home',  name: 'home',     component :Home},
    {path: '/flowerpot', name: 'flowerpot',     component :FlowerPot},
    {path: '/netatmo',  name: 'netatmo',     component :Netatmo},
    {path: '/nanoleaf', name: 'projectdetails',     component :NanoLeaf},
    {path: "*", component: Home }
  ]
})

new Vue({
  el: '#app',
  router,
  //routes, not this
  render: h => h(App)
})

