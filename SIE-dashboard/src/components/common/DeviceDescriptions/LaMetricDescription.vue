<template>
  <DeviceDescription>
    <template #header>LaMetric Time</template>
    <template #default>
        De LaMetric Time is meer dan alleen een klok. Voor dit bij o.a. veel YouTubers populaire device is op het internet goede 
        <b-link href="https://lametric-documentation.readthedocs.io/en/latest/reference-docs/lametric-time-reference.html"> API </b-link>
        documentatie beschikbaar.
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
