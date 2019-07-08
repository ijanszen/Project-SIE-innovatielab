<template>
  <DeviceDescription>
    <template #header>LaMetric</template>
    <template #default>
        De LaMetric is een matrix led display dat vaak als klok wordt gebruikt. <br/> 
        Het is makkelijk aanpasbaar en er kan aparte applicaties voor geschreven worden. <br/>
        De data uit de Netatmo wordt hierop getoond.
    </template>
    <template #photo>
      <img class="img" src="../../../assets/devices/LaMetric Time.png">
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
