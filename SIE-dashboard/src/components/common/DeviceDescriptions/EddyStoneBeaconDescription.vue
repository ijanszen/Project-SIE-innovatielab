<template>
   <DeviceDescription>
        <template #header>Bluetooth / Eddystone Beacons</template>
        <template #default>
          Een alternatief voor de QR codes? Voor meer info zie de 
          <b-link href="https://developers.google.com/beacons/"> website. </b-link>   
        </template>
        <template #photo><img class="img" src="../../../assets/devices/eddystone.jpg"></template>     
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
