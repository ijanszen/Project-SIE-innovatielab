<template>
  <b-table striped :fields="fields" :items="items">
    <template slot="id" slot-scope="data">{{ data.item.id}}</template>
    <template slot="Kleurcode" slot-scope="data">
      <b-form-input v-model="data.item.colorcode" id="type-color" type="color"></b-form-input>
    </template>
    <template slot="Ingeschakeld" slot-scope="data">
      <b-form-checkbox v-model="data.item.on" name="check-button" switch></b-form-checkbox>
    </template>
  </b-table>
</template>

<script>
export default {
  data() {
    return {
      fields: [{ key: "id", label: "Leaf #" }, "Kleurcode", "Ingeschakeld"],
      items: [
        { id: 1, colorcode: "#FF2000", on: true },
        { id: 2, colorcode: "#208CC2", on: false },
        { id: 3, colorcode: "#FF5733", on: true },
        { id: 4, colorcode: "#E4B822", on: true }
      ]
    };
  }
};
</script>