<template>
   <DeviceDescription>
        <template #header>Audio & video equipment</template>
        <template #default>
            Apparatuur ter ondersteuning van video conferenties en het maken van video's met bijvoorbeeld
            <b-link href="https://obsproject.com/"> OBS.</b-link>   
        </template>
        <template #photo><img class="img" src="../../../assets/devices/audiovideo.png"></template>     
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
