<template>
  <b-container fluid>
    <b-row>
      <b-col>
        <NanoLeafDescription/>
      </b-col>
      <b-col>
        <nano-leaf-table/>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import NanoLeafDescription from "../common/DeviceDescriptions/NanoLeafDescription.vue";
import NanoLeafTable from "../common//NanoLeafTable.vue";

export default {
  components: {
    NanoLeafDescription,
    NanoLeafTable
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
