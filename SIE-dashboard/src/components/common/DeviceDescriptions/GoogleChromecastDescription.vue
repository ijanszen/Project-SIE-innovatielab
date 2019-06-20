<template>
   <DeviceDescription>
        <template #header>Google Chromecast</template>
        <template #default>
         Velen gebruiken de chromecast al voor het bekijken van Films, Foto's etc. Maar je kunt ook apps maken om je eigen content ermee te tonen.
          <b-link href="https://developers.google.com/cast/"> Een voorbeeld. </b-link>   
        </template>
        <template #photo><img class="img" src="../../../assets/devices/googlechromecast.jpg"></template>     
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
