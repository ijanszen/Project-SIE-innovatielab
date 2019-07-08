<template>
  <DeviceDescription>
    <template #header>NanoLeaf</template>
    <template #default>
      Op de buitenste twee panelen wordt de health-status afgebeeld.
      Bij de middelste zeven panelen is de ‘percentage-balk’ hier worden de overige Netatmo-statussen weergegeven in percentage. <br/>
      Health-status is een getal van 0 t/m 4 de mogelijke kleuren en de bijbehorende statussen staan weergegeven in de kleurentabel hieronder.

    </template>
    <template #photo>
      <img class="img" src="../../../assets/devices/Nanoleaf.jpg">
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
.img{
  width: 60%;
}
</style>
