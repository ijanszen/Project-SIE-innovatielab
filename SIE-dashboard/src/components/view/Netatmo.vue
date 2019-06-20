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
          <DeviceDescription>
            <template #header>Netatmo</template>
            <template #default>
              De Netatmo is een klein weerstation waarmee onder andere de luchtkwaliteit gemeten kan worden van een kamer.
              Met de netatmo kunnen de volgende waardes gemeten worden:
              <ul>
                <li>Temperatuur</li>
                <li>Luchtvochtigheid</li>
                <li>CO2</li>
                <li>Geluidsniveau</li>
                <li>luchtkwaliteit</li>
              </ul>
            </template>
            <template #photo>
              <img class="img" src="../../assets/devices/Netatmo.jpg">
            </template>
          </DeviceDescription>
        </b-col>
      </b-row>
    </b-container>
</template>

<script>
import DeviceDescription from '../common/DeviceDescription.vue'
import LineChart from '../common/Graph'

var Co2 = "Co2"

export default {
  components: {
    DeviceDescription,
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
