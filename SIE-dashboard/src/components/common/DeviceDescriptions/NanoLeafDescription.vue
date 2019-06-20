<template>
  <DeviceDescription>
    <template #header>NanoLeaf</template>
    <template #default>
      Een interessante slimme verlichting waarvan de OpenAPI echter op dit moment alleen via een inschrijving voor het Beta Program beschikbaar is. 
      Voor meer info zie de <b-link href="https://nanoleaf.me/en/consumer-led-lighting/join-beta-program/"> website. </b-link>
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
