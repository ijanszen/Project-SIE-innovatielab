<template>
  <DeviceDescription>
    <template #header>NanoLeaf</template>
    <template #default>
      Op de buitenste twee panelen wordt de health-status afgebeeld.
      Health-status is een getal van 0 t/m 4 de mogelijke kleuren en de bijbehorende statussen staan weergegeven in Tabel 1.
      Bij de middelste zeven panelen is de ‘percentage-balk’ hier worden de overige Netatmo-statussen weergegeven in percentage.
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
</style>
