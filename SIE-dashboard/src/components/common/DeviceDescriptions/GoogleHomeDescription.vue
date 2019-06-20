<template>
   <DeviceDescription>
        <template #header>Google Home</template>
        <template #default>
         Spraak is de nieuwe User Interface.  Maar hoe ontwikkel je een conversational design interface? 
         Meer info hierover is te vinden op de volgende 
          <b-link href="https://developers.google.com/actions/"> website.</b-link>   
        </template>
        <template #photo><img class="img" src="../../../assets/devices/googlehome.png"></template>     
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
