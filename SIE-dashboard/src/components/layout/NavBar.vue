<template>
    <b-navbar variant="light" style="background-color: #e3f2fd;" type="light">
    <b-navbar-nav > 
      <b-link to="home" router-tag="b-nav-item">Home</b-link>
      <b-link to="netatmo" router-tag="b-nav-item">Netatmo</b-link>
      <b-link to="nanoleaf" router-tag="b-nav-item">Nanoleaf</b-link>
      <b-link to="flowerpot" router-tag="b-nav-item">Parrot Flower Pot</b-link>
    </b-navbar-nav>

    <b-navbar-nav class="ml-auto">
       <toggle-button class= "button" 
          :value="false"
          :color="{checked: '#75a175', unchecked: '#CCCCCC'}"
          :sync="true"
          :width="230"
          :height="40"
          :font-size="15"
          :labels="{checked: 'Demonstratiemodus: Aan', unchecked: 'Demonstratiemodus: Uit'}"/>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>


export default {
    data() {
      return {
        myToggle: false
      }
    }
}

</script>
<style>
.navbar {
  position: relative;
}

.button {
  margin-top: 2%;
}
</style>