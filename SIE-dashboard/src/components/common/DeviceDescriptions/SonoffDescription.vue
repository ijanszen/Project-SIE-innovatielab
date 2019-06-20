<template>
   <DeviceDescription>
        <template #header>Sonoff</template>
        <template #default>
          Een heel populaire (goedkope) wifi gebaseerde klik-aan/uit schakelaar. 
          Voor meer info zie de 
          <b-link href="https://blog.ipsumdomus.com/sonoff-switch-complete-hack-without-firmware-upgrade-1b2d6632c01"> website. </b-link>   
        </template>
        <template #photo><img class="img" src="../../../assets/devices/sonoff.jpg"></template>     
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
