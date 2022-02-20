<template>
  <div>
    <header-component></header-component>
    <v-container fluid>
      <v-row no-gutters>
        <v-col
            cols="12"
            sm="6"
            md="8"
        >

        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import HeaderComponent from "@/views/component/HeaderComponent";
// import {updateRecommends} from "@/api";

export default {
  name: "SearchRecordsComponent",
  component: {HeaderComponent},
  data() {
    return {
      //
    };
  },
  methods: {
    //
  },
  beforeCreate() {
    // updateRecommends().then((res) => {
    //   console.log(res);
    // });
  }
}
</script>

<style scoped>

</style>
