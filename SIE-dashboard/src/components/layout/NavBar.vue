<template>
  <div>
    <b-navbar variant="light" style="background-color: #e3f2fd;" type="light">
    <b-navbar-nav > 
      <b-link to="home" router-tag="b-nav-item">Home</b-link>
      <b-link to="netatmo" router-tag="b-nav-item">Netatmo</b-link>
      <b-link to="nanoleaf" router-tag="b-nav-item">Nanoleaf</b-link>
      <b-link to="flowerpot" router-tag="b-nav-item">Parrot Flower Pot</b-link>
    </b-navbar-nav>

    <b-navbar-nav class="ml-auto">
       <b-button :pressed.sync="myToggle" variant="outline-info"> Demo modus</b-button>
    </b-navbar-nav>
  </b-navbar>
  </div>
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
</style>