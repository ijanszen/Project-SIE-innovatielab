<template>
  <b-container fluid>
    <b-row>

      <b-col>
        <NanoLeafDescription/>
      </b-col>

      <b-col md="auto">
        <DeviceDescription>
          <template #header>Aansturen</template>
          <template #default>
            <b-row>

              <b-col class="ButtonGroup">
                <b-button-group vertical>
                  <b-button v-on:click="switchResource('Off')">Off</b-button>
                  <b-button :pressed="true" variant="success" disabled>Health</b-button>
                  <b-button v-on:click="switchResource('Co2')">Co2</b-button>
                  <b-button v-on:click="switchResource('Noise')">Noise</b-button>
                  <b-button v-on:click="switchResource('Pressure')">Pressure</b-button>
                  <b-button v-on:click="switchResource('WiFi_stat')">Wifi stat</b-button>
                  <b-button v-on:click="switchResource('Humidity')">Humidity</b-button>
                  <b-button v-on:click="switchResource('Temperature')">Temperature</b-button>
                </b-button-group>
              </b-col>

              <b-col>
                <img class="NanoleafImg" src="../../assets/Nanoleaf_Setup.svg"/>
              </b-col>

            </b-row>
          </template>
        </DeviceDescription>

      </b-col>

    </b-row>
  </b-container>
</template>

<script>
import NanoLeafDescription from "../common/DeviceDescriptions/NanoLeafDescription.vue";
import NanoLeafTable from "../common//NanoLeafTable.vue";
import DeviceDescription from "../common/DeviceDescriptions/DeviceDescription.vue";
import $ from 'jquery'

export default {
  components: {
    NanoLeafDescription,
    NanoLeafTable,
    DeviceDescription
  }, 
  methods: {
    switchResource(value) {
      $.ajax({
          "async": true,
          "crossDomain": true,
          "url": "http://192.168.3.157:1880/dashboard?display=" + value.toLowerCase(),
          "method": "GET",
          "headers": {
              "Accept": "application/json",
              "Content-Type": "application/json",
              "cache-control": "no-cache"
          },
          "processData": false,
          "data": ""
        }).done(function (response) {
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.NanoleafImg {
  width: 200px;
  height: 300px;
}
.ButtonGroup {
  padding: 20px;
}
.test:active {
  background-color: green;
}
</style>
