<template>
    <b-container fluid>
      <b-row>
        <b-col cols="8">Grafiek</b-col>
        <b-col>
          <DeviceDescription>
            <template #header>Parrot Flower Pot</template>
            <template #default>Abi smart bloemenpot wat wil je nog meer weten</template>
            <template #photo></template>
          </DeviceDescription>
        </b-col>
      </b-row>
    </b-container>
</template>

<script>
import DeviceDescription from "../common/DeviceDescription.vue";

export default {
  components: {
    DeviceDescription
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
