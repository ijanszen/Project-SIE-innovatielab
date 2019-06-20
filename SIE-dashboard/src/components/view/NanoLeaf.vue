<template>
  <b-container fluid>   
    <b-row>
      <b-col cols="8">Grafiek</b-col>
      <b-col>
        <NanoLeafDescription />
      </b-col>  
    </b-row>
  </b-container>
</template>

<script>
import NanoLeafDescription from '../common/DeviceDescriptions/NanoLeafDescription.vue'


export default {
  components: {
    NanoLeafDescription,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.img {
     max-width: 100%;
     height: auto;
  }
</style>
