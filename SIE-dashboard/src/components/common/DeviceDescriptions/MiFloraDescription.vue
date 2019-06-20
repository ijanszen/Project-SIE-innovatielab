<template>
  <DeviceDescription>
    <template #header>Mi Flora Flower Care</template>
    <template #default>
      Bluetooth device die meerdere sensoren bevat, om zo mensen zonder groene fingers te ondersteunen,
      er zijn meerdere API's voor deze sensor te vinden,
      zoals op deze
      <b-link href="https://github.com/vrachieru/xiaomi-flower-care-api">Website.</b-link>
    </template>
    <template #photo>
      <img class="img" src="../../../assets/devices/miflora.jpg">
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
.img {
  max-width: 100%;
  height: auto;
}
</style>
