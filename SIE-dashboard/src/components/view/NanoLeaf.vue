<template>
  <b-container fluid>
    <b-row>
      <b-col>
        <NanoLeafDescription/>
      </b-col>
      <b-col>
        <nano-leaf-table/>
      </b-col>
      <b-col>
        <b-button-group vertical>
          <b-button v-on:click="switchResource('Co2')">Co2</b-button>
          <b-button  v-on:click="switchResource('Noise')">Noise</b-button>
          <b-button  v-on:click="switchResource('Pressure')">Pressure</b-button>
          <b-button v-on:click="switchResource('WiFi_stat')">Wifi stat</b-button>
          <b-button v-on:click="switchResource('Humidity')">Humidity</b-button>
          <b-button  v-on:click="switchResource('Temperature')">Temperature</b-button>
        </b-button-group>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import NanoLeafDescription from "../common/DeviceDescriptions/NanoLeafDescription.vue";
import NanoLeafTable from "../common//NanoLeafTable.vue";
import $ from 'jquery'

export default {
  components: {
    NanoLeafDescription,
    NanoLeafTable
  }, methods: {
    switchResource(value) {
      console.log(value.toLowerCase());

      $.ajax({
                "async": true,
                "crossDomain": true,
                "url": "http://192.168.3.157:1880/dashboard?display=" + value,
                "method": "GET",
                "headers": {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "cache-control": "no-cache"
                },
                "processData": false,
                "data": ""
            }).done(function (response) {
                console.log(response);
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
