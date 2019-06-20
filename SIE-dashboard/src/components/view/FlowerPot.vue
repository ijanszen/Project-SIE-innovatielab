<template>
    <b-container fluid>
      <b-row>
        <b-col cols="8">Grafiek</b-col>
        <b-col>
          <flower-pot-description/>
        </b-col>
      </b-row>
    </b-container>
</template>

<script>
import FlowerPotDescription from "../common/DeviceDescriptions/FlowerPotDescription.vue";

export default {
  components: {
    FlowerPotDescription
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
