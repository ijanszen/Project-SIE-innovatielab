<template>
  <DeviceDescription>
            <template #header>Netatmo - Smart Indoor Air Quality Monitor</template>
            <template #default>
              Dit device is bedoeld om de luchtkwaliteit te meten. Via hun 
               <b-link href="https://dev.netatmo.com/resources/technical/reference"> api</b-link> 
               kun je de volgende informatie opvragen:
              <ul>
                <li>Temperatuur</li>
                <li>Luchtvochtigheid</li>
                <li>CO2</li>
                <li>Geluidsniveau</li>
                <li>luchtkwaliteit</li>
              </ul>
            </template>
            <template #photo>
              <img class="img" src="../../../assets/devices/Netatmo.jpg">
            </template>
    </DeviceDescription>
</template>

<script>
import DeviceDescription from "./DeviceDescription.vue";

export default {
  components: {
    DeviceDescription
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
