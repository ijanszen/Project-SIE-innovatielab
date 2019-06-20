<template>
   <DeviceDescription>
        <template #header>Sphero - Bolt</template>
        <template #default>
          Deze rollende ball, beschikt behalve over een display ook over enkele sensoren en kan via JavaScript geprogrammeerd worden. 
          Voor meer info zie de <b-link href="https://sdk.sphero.com/community-apis/javascript-sdk/"> website.</b-link>   
        </template>
        <template #photo><img class="img" src="../../../assets/devices/spherobolt.jpg"></template>     
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
