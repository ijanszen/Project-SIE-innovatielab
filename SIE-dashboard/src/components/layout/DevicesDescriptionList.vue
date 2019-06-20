<template>
  <b-card-group columns>
    <EddyStoneBeaconDescription/>
    <flower-pot-description/>
    <GoogleChromecastDescription/>
    <GoogleHomeDescription/>
    <IkeaTradfriDescription/>
    <La-metric-description/>
    <NanoLeafDescription/>
    <netatmo-description/>
    <NintendoSwitchDescription/>
    <PhilipsHueDescription/>
    <SonoffDescription/>
    <MiFloraDescription/>
    <AudioVideoDescription/>
    <SpheroBoltDescription/>
  </b-card-group>
</template>

<script>
import EddyStoneBeaconDescription from "../common/DeviceDescriptions/EddyStoneBeaconDescription.vue";
import FlowerPotDescription from "../common/DeviceDescriptions/FlowerPotDescription.vue";
import GoogleChromecastDescription from "../common/DeviceDescriptions/GoogleChromecastDescription.vue";
import GoogleHomeDescription from "../common/DeviceDescriptions/GoogleHomeDescription.vue";
import IkeaTradfriDescription from "../common/DeviceDescriptions/IkeaTradfriDescription.vue";
import LaMetricDescription from "../common/DeviceDescriptions/LaMetricDescription.vue";
import NanoLeafDescription from "../common/DeviceDescriptions/NanoLeafDescription.vue";
import NetatmoDescription from "../common/DeviceDescriptions/NetatmoDescription.vue";
import NintendoSwitchDescription from "../common/DeviceDescriptions/NintendoSwitchDescription.vue";
import PhilipsHueDescription from "../common/DeviceDescriptions/PhilipsHueDescription.vue";
import SonoffDescription from "../common/DeviceDescriptions/SonoffDescription.vue";
import MiFloraDescription from "../common/DeviceDescriptions/MiFloraDescription.vue";
import AudioVideoDescription from "../common/DeviceDescriptions/AudioVideoDescription.vue";
import SpheroBoltDescription from "../common/DeviceDescriptions/SpheroBoltDescription.vue";

export default {
  components: {
    EddyStoneBeaconDescription,
    FlowerPotDescription,
    GoogleChromecastDescription,
    GoogleHomeDescription,
    IkeaTradfriDescription,
    LaMetricDescription,
    NanoLeafDescription,
    NetatmoDescription,
    NintendoSwitchDescription,
    PhilipsHueDescription,
    SonoffDescription,
    MiFloraDescription,
    AudioVideoDescription,
    SpheroBoltDescription
  }
};
</script>