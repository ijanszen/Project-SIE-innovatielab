<template>
  <div>
    <b-container fluid>   
      <b-row>
        <b-col cols="8">Grafiek
          <LineChart  />
        </b-col>

        <b-col> Detailbeschrijving
          <DeviceDescription> 
            <template #header>Netatmo</template>
            <template #default>
              De Netatmo is een klein weerstation waarmee onder andere de luchtkwaliteit gemeten kan worden van een kamer.

              Met de netatmo kunnen de volgende waardes gemeten worden:
              <ul>
                 <li> Temperatuur   </li>
                 <li> Luchtvochtigheid</li>
                 <li> CO2</li>
                 <li> Geluidsniveau</li>
                 <li> luchtkwaliteit</li>
              </ul>
              
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
import LineChart from '../common/Graph'

export default {
  components: {
    DeviceDescription,
    LineChart
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
