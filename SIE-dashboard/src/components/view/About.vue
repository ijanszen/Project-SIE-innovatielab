<template>
  <b-container fluid>
    <b-jumbotron>
      <template slot="header">SIE innovatielab</template>
      <template slot="lead">Welkom op het SIE innovatielab. Tot je beschikking staan een hoop nieuwe, innovatieve devices en gadgets.</template>

      <p>
        Deze website is er om jou duidelijk te maken wat er aanwezig is en welke informatie ze allemaal opleveren.
        Ook kan je sommige van de apparaten aansturen. De projectgroep die deze website maakt heeft maar beperkt de tijd.
        Hierdoor zal het waarschijnlijk voor ons niet mogelijk zijn om alle aanwezige devices in het SIE-lab te integreren.
        Daarom volgt hieronder een lijst van alle fysieke aanwezige devices.
        We hopen dat de volgende studentengroepen verder gaan waar wij gebleven zijn.
      </p>
    </b-jumbotron>
    <DevicesDescriptionList/>
  </b-container>
</template>

<script>
import DevicesDescriptionList from "../layout/DevicesDescriptionList.vue";

export default {
  components: {
    DevicesDescriptionList
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
