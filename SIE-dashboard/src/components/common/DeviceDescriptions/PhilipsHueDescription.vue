<template>
   <DeviceDescription>
        <template #header>Bluetooth / Eddystone Beacons</template>
        <template #default>
          Het slimme verlichtingsysteem van Philips. Voor meer info zie de
          <b-link href="https://developers.meethue.com/ "> website. </b-link>   
        </template>
        <template #photo><img class="img" src="../../../assets/devices/philipshue.jpg"></template>     
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
