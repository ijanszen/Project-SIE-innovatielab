<template>
  <b-card header-tag="header" img src="../../../assets/logo.png" >
    <b-card-header class="display-4">
      <slot name="header">Apparaatnaam</slot>
    </b-card-header>
    <b-card-text>
      <slot>Apparaatbeschrijving</slot>
    </b-card-text>
    <slot align="bottom" name="photo"></slot>
  </b-card>
  
</template>

<script>
export default {
  props: {
    msg: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.img {
  max-width: 100%;
  height: auto;
}
</style>
