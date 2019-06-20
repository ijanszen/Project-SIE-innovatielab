<template>
   <DeviceDescription>
        <template #header>Ikea Trådfri - Smart Lightning</template>
        <template #default>
          Er zijn meerdere projecten online te vinden die een library voor deze lampen beschikbaar stellen, opdat je ze met je eigen app kunt ontsluiten.
          <b-link href="https://github.com/ggravlingen/pytradfri"> Een voorbeeld. </b-link>   
        </template>
        <template #photo><img class="img" src="../../../assets/devices/ikeatradfri.jpg"></template>     
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
