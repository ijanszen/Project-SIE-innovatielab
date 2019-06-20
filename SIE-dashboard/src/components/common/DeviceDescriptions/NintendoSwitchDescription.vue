<template>
   <DeviceDescription>
        <template #header>Nintendo Switch</template>
        <template #default>
          Behalve games erop spelen zou je ook games ervoor kunnen programmeren. 
          Meer info omtrent het ontwikkelen van games voor o.a. deze  console vind je op de          
          <b-link href="https://developer.nintendo.com/"> website. </b-link>   
        </template>
        <template #photo><img class="img" src="../../../assets/devices/nintendoswitch.jpg"></template>     
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
