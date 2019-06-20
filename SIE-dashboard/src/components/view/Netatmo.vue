<template>
  <b-container fluid>
    <b-row>
      <b-col>
        <b-button-group vertical>
          <b-button :pressed.sync="myToggle" variant="outline-primary" v-on:click="switchResource('Co2')">Co2</b-button>
          <b-button variant="outline-primary" v-on:click="switchResource('Noise')">Noise</b-button>
          <b-button variant="outline-primary" v-on:click="switchResource('Pressure')">Pressure</b-button>
          <b-button variant="outline-primary" v-on:click="switchResource('WiFi_stat')">Wifi stat</b-button>
          <b-button variant="outline-primary" v-on:click="switchResource('Humidity')">Humidity</b-button>
          <b-button variant="outline-primary" v-on:click="switchResource('Temperature')">Temperature</b-button>
        </b-button-group>
      </b-col>

      <b-col cols="6">
        <LineChart :API="this.Resource"/>
      </b-col>

      <b-col>
        <netatmo-description/>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import NetatmoDescription from "../common/DeviceDescriptions/NetatmoDescription.vue";
import LineChart from "../common/Graph";

export default {
  components: {
    NetatmoDescription,
    LineChart
  },
  data() {
    return {
      Resource: "Co2"
    };
  },
  methods: {
    switchResource(value) {
      if (this.Resource != value) {
        this.Resource = value;
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
