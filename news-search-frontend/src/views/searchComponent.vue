<template>
  <v-main>
    <v-container>
      <v-row class="text-center">
        <v-col cols="12">
          <v-img
              :src="require('../assets/logon.png')"
              class="mt-16 mb-5"
              contain
              height="400"
          />
        </v-col>
        <v-col
            cols="6"
            offset-md="3"
            :align-self="alignment"
            :align="alignment">
          <v-text-field
              v-model="model"
              chips
              clearable
              item-text="name"
              item-value="symbol"
              label="Search for a news..."
              solo
          ></v-text-field>
        </v-col>
        <v-col
            cols="12"
            :align-self="alignment"
            :align="alignment">
          <v-btn
              @click="searchTerm"
              class="ma-4"

              raised
          >
            Search
          </v-btn>

          <v-btn
              @click="searchTerm"
              class="ma-4"

              raised
          >
            Check the map!
          </v-btn>
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
    model: null,
  }),
  methods:{
    searchTerm(){
      console.log(this.model);
      this.$router.push({path:'/search', query:{search_phase: this.model}});
    }
  }
}
</script>

<style scoped>

</style>
