<template>
    <b-navbar type="light" variant="faded">
    <b-navbar-brand class="brand" to="home">
      <img src="../../assets/hu.jpg" width="100%" alt="HU">
    </b-navbar-brand>

    <b-navbar-nav> 
      <b-nav-item to="home">Home</b-nav-item>
      <b-nav-item to="netatmo">Netatmo</b-nav-item>
      <b-nav-item to="nanoleaf">Nanoleaf</b-nav-item>
      <b-nav-item to="flowerpot">Parrot Flower Pot</b-nav-item>
      <b-nav-item to="about">About</b-nav-item>
    </b-navbar-nav>    

    <b-navbar-nav class="ml-auto">
       <toggle-button v-model="demonstratieModus" class= "button" 
          :value="false"
          :color="{checked: '#42b983', unchecked: '#CCCCCC'}"
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
        demonstratieModus: false
      }
    }
}

</script>
<style>
.navbar {
  position: relative;
}

.router-link-active {
  color: #42b983 !important;
}

.brand {
  width: 50px;
}

.button {
  margin-top: 2%;
}
</style>