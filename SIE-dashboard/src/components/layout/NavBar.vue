<template>
    <b-navbar type="light" variant="faded">
    <b-navbar-brand class="brand" to="home">
      <img src="../../assets/hu.jpg" width="100%" alt="HU">
    </b-navbar-brand>

    <b-navbar-nav> 
      <b-nav-item to="home">Home</b-nav-item>
      <b-nav-item to="netatmo">Netatmo</b-nav-item>
      <b-nav-item to="nanoleaf">Nanoleaf</b-nav-item>
      <b-nav-item to="lametric">LaMetric</b-nav-item>
      <b-nav-item to="about">About</b-nav-item>
    </b-navbar-nav>    

    <b-navbar-nav class="ml-auto">
       <toggle-button v-model="demonstratieModus" class= "button" 
          :value="false"
          :color="{checked: '#42b983', unchecked: '#CCCCCC'}"
          :sync="true"
          :width="230"
          :height="40"
          :font-size="15"
          :labels="{checked: 'Demonstratiemodus: Aan', unchecked: 'Demonstratiemodus: Uit'}"
          @change="click"/>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>
import { clearInterval } from 'timers';

export default {
    data() {
      return {
        demonstratieModus: false,
        demonstratieModusStatus: "off",
        timer: ''
      }
    },
    methods: {
      click() {
        if(this.demonstratieModusStatus == "off") {
          this.demonstratieModusStatus = "on"
          this.timer=(setInterval(this.cycleThroughComponents, 4000))
          this.setDemoModeOn()

        } else if(this.demonstratieModusStatus == "on") {
          this.demonstratieModusStatus = "off"
          window.clearInterval(this.timer)
          this.setDemoModeOff()
        }
      },
      setDemoModeOn() {
        this.$root.$emit('clicked', 'on')
        
      },
      setDemoModeOff() {
        this.$root.$emit('clicked', 'off')
      },
      cycleThroughComponents() {
        const path = this.$route.path
        if(path == '/home') {
          this.$router.push('netatmo')
        } else if(path == '/netatmo') {
          this.$router.push('nanoleaf')
        } else if(path == '/nanoleaf') {
          this.$router.push('lametric') 
        } else if(path == '/lametric') {
          this.$router.push('about')
        } else if(path == '/about') {
          this.$router.push('home')
        }
      },
    }
}

</script>
<style>
.navbar {
  position: relative;
}

.router-link-active {
  color: #42b983 !important;
}

.brand {
  width: 50px;
}

.button {
  margin-top: 2%;
}
</style>