<template>
  <v-main>
    <v-container>
      <v-row class="text-center">
        <v-col cols="12">
          <v-img
              :src="require('../assets/logo.svg')"
              class="mt-16 mb-5"
              contain
              height="200"
          />
        </v-col>
        <v-col
            cols="6"
            offset-md="3"
            :align-self="alignment"
            :align="alignment">
          <v-autocomplete
              clearable
              rounded
              solo
              v-model="searchText"
          ></v-autocomplete>
        </v-col>
        <v-col
            cols="6"
            offset-md="3"
            :align-self="alignment"
            :align="alignment">
          <v-btn
              elevation="2"
              plain
              raised
              @click="searchTerm"
          > Search</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
export default {
  name: "searchComponent",
  data: () =>({
    alignment: 'center',
    searchText:''
  }),
  methods:{
    searchTerm(){
      this.$router.push({name:'result', query:{search_phase: this.searchText}})
    }
  }
}
</script>

<style scoped>

</style>
