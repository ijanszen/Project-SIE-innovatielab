<template>
    <b-container fluid>
      <b-row>
        <b-col cols="8">Grafiek
          <button v-on:click="switchResource('Co2')">Co2</button>
          <button v-on:click="switchResource('Noise')">Noise</button>
          <button v-on:click="switchResource('Pressure')">Pressure</button>
          <button v-on:click="switchResource('WiFi_stat')">Wifi stat</button>
          <button v-on:click="switchResource('Humidity')">Humidity</button>
          <button v-on:click="switchResource('Temperature')">Temperature</button>
          <LineChart :API="this.Resource" />
        </b-col>
         
        <b-col>
           <netatmo-description />
        </b-col>
      </b-row>
    </b-container>
</template>

<script>
import NetatmoDescription from '../common/DeviceDescriptions/NetatmoDescription.vue'
import LineChart from '../common/Graph'

var Co2 = "Co2"

export default {
  components: {
    NetatmoDescription,
    LineChart
  },
  data() {
    return {
      Resource: "Co2"
    }
  },
  methods: {
    switchResource(value) {
      if(this.Resource != value) {
        this.Resource = value;
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.img {
  max-width: 100%;
  height: auto;
}
</style>
