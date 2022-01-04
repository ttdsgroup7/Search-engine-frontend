<template>
  <v-main id="inspire">
    <v-toolbar color="orange accent-1" >
      <v-app-bar-nav-icon class="hidden-sm-and-down" @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-h6 mr-6 hidden-sm-and-down">
        News search
      </v-toolbar-title>
      <v-autocomplete
          v-model="model"
          :items="items"
          :loading="isLoading"
          :search-input.sync="search"
          chips
          clearable
          hide-details
          hide-selected
          item-text="name"
          item-value="symbol"
          label="Search for a news..."
          solo
      >
        <template v-slot:no-data>
          <v-list-item>
            <v-list-item-title>
              Search for your daily
              <strong>Covid news</strong>
            </v-list-item-title>
          </v-list-item>
        </template>
        <template v-slot:selection="{ attr, on, item, selected }">
          <v-chip
              v-bind="attr"
              :input-value="selected"
              color="blue-grey"
              class="white--text"
              v-on="on"
          >
            <v-icon left>
              mdi-bitcoin
            </v-icon>
            <span v-text="item.name"></span>
          </v-chip>
        </template>
        <template v-slot:item="{ item }">
          <v-list-item-avatar
              color="indigo"
              class="text-h5 font-weight-light white--text"
          >
            {{ item.name.charAt(0) }}
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title v-text="item.name"></v-list-item-title>
            <v-list-item-subtitle v-text="item.symbol"></v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-icon>mdi-bitcoin</v-icon>
          </v-list-item-action>
        </template>
      </v-autocomplete>
      <template v-slot:extension>
        <v-tabs
            v-model="tab"
            :hide-slider="!model"
            color="blue-grey"
            slider-color="blue-grey"
        >
          <v-tab :disabled="!model">
            News
          </v-tab>
          <v-tab :disabled="!model">
            Trading
          </v-tab>
          <v-tab :disabled="!model">
            Blog
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>
    <v-navigation-drawer
        v-model="drawer"
        absolute
        temporary
    >

    </v-navigation-drawer>
    <v-col
      v-for="(item, index) in items"
      :key="index"
      cols="12"
    >
      <v-card
          :color="item.color"

      >
        <div class="d-flex flex-no-wrap justify-space-between">
          <div>
            <v-card-title
                class="text-h5"
                v-text="item.head_line"
            ></v-card-title>

            <v-card-subtitle v-text="timestampConvert(item.publish_date)"></v-card-subtitle>

            <v-card-actions>
              <v-btn

                  class="ml-2 mt-5"
                  outlined
                  rounded
                  small
                  :href="item.tag"
              >
                Read More
              </v-btn>
            </v-card-actions>
          </div>

          <v-avatar
              class="ma-3"
              size="125"
              tile
          >
            <v-img :src="item.src"></v-img>
          </v-avatar>
        </div>
      </v-card>
    </v-col>

  </v-main>
</template>

<script>
import  axios from "axios";
export default {
  name: "resultComponent",
  data: () => ({
    links: [
      'Dashboard',
      'Messages',
      'Profile',
      'Updates',
    ],
    isLoading: false,
    items_test: [{"publish_date":"2022-01-02T10:56:53.000Z","head_line":"Vaccination centre relocates to new site","tag":"https://bbc.co.uk/news/uk-england-cumbria-59852247"},{"publish_date":"2022-01-01T12:04:40.000Z","head_line":"Muted celebrations as Hogmanay curtailed by Covid","tag":"https://bbc.co.uk/news/uk-scotland-59846640"},{"publish_date":"2022-01-01T13:17:27.000Z","head_line":"Pubs 'exceptionally quiet' as Wales marks new year","tag":"https://bbc.co.uk/news/uk-wales-59846561"},{"publish_date":"2022-01-01T15:00:19.000Z","head_line":"Fireworks mark subdued UK new year","tag":"https://bbc.co.uk/news/uk-59844031"},{"publish_date":"2022-01-01T16:17:08.000Z","head_line":"Antarctic station hit by Covid-19 outbreak","tag":"https://bbc.co.uk/news/world-europe-59848160"}],
    items:[],
    model: null,
    search: null,
    tab: null,
    drawer: false
  }),
  watch:{
    model (val) {
      if (val != null) this.tab = 0
      else this.tab = null
    },
    search(term){
      if (this.items.length < 0 || this.items.length == null){
        this.items = []
        return
      }

      this.isLoading = true

      axios
          .get(`http://gc.caohongchuan.top:8080/search/querynews?query=${term}`)
          .then((response)=>{
            console.log(response.data)
            this.items = response.data['newsarray']
          })
          .catch((err)=>{
            console.error(err)
            this.items = []
            return
          })
          .finally(() =>{
            this.isLoading = false;
          })
    }
  },
  methods:{
    timestampConvert(timeStamp){
      let date = new Date(timeStamp);
      let year = date.getFullYear();
      let month = date.getMonth();
      let day = date.getDate();
      if (day < 10) {
        day = '0' + day;
      }
      if (month < 10) {
        month += 1;
        month = '0' + month;
      }
      return day + '/' + month +'/' + year
    },
  }
}
</script>

<style scoped>

</style>
