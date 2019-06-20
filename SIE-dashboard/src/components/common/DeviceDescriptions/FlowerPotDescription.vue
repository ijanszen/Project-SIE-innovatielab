<template>
   <DeviceDescription>
        <template #header>Parrot Flower Pot</template>
        <template #default>
          Een slimme bloemenpot waarvan data beschikbaar is via de
          <b-link href="https://developer.parrot.com/docs/FlowerPower/"> website. </b-link>   
        </template>
        <template #photo><img class="img" src="../../../assets/devices/Parrot Connected Flower Pot.jpg"></template>     
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
