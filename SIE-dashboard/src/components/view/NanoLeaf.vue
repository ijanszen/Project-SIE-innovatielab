<template>
  <div>
    <b-container fluid>   
      <b-row>
        <b-col cols="8">Grafiek</b-col>

        <b-col> Detailbeschrijving
          <DeviceDescription> 
            <template #header>NanoLeaf</template>
            <template #default>
              De nanoleaf is cool want je kan allemaal losse lampen aan elkaar aansluiten en daarom vet koele lichtjes enzo       
            </template>   
            <template #photo><img class="img" src="../../assets/devices/Netatmo.jpg"></template>     
          </DeviceDescription>
        </b-col>  
      </b-row>
      

    </b-container>
    </div>
</template>

<script>
import DeviceDescription from '../common/DeviceDescription.vue'


export default {
  components: {
    DeviceDescription,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.img {
     max-width: 50%;
     height: auto;
  }
</style>
