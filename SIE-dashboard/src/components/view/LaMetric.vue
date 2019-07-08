<template>
    <b-container fluid>
      <b-row>
        <b-col>
          <la-metric-description/>
        </b-col>
      </b-row>
    </b-container>
</template>

<script>
import LaMetricDescription from "../common/DeviceDescriptions/LaMetricDescription.vue";

export default {
  components: {
    LaMetricDescription
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
