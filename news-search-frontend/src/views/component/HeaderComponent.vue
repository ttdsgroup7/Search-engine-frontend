<template>
  <div>
    <v-navigation-drawer
        v-model="drawer"
        app
    >
      <v-list
          nav
          dense
      >
        <v-list-item-group
            v-model="group"
            active-class="deep-purple--text text--accent-4"
        >
          <v-list-item @click="toHome">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-map</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Map</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar color="orange accent-1" app>
      <v-app-bar-nav-icon class="hidden-sm-and-down" @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-h6 mr-6 hidden-sm-and-down">
        <span @click="toHome">News search</span>
      </v-toolbar-title>
      <v-autocomplete

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
        <template v-slot:selection="{ attr, on, item, selected }">
          <v-chip
              v-bind="attr"
              :input-value="selected"
              color="blue-grey"
              class="white--text"
              v-on="on"
          >
            <span v-text="item.head_line"></span>
          </v-chip>
        </template>
        <template v-slot:no-data>
          <v-list-item>
            <v-list-item-title>
              Search for your daily
              <strong>Covid news</strong>
            </v-list-item-title>
          </v-list-item>
        </template>
        <template v-slot:item="{ item }">
          <v-list-item-content @click="toNews(item.url)">
            <v-list-item-title v-text="item.head_line"></v-list-item-title>
            <v-list-item-subtitle v-text="timestampConvert(item.publish_date)"></v-list-item-subtitle>
          </v-list-item-content>
        </template>
      </v-autocomplete>
      <template v-slot:extension>
        <v-tabs
            v-model="tab"
            color="blue-grey"
            slider-color="blue-grey"
            class="mr-3"
        >
          <v-tab>
            News
          </v-tab>
          <v-tab>
            The New York Times
          </v-tab>
          <v-tab>
            Blog
          </v-tab>
        </v-tabs>
        <v-btn @click="isAdvanceSearch = !isAdvanceSearch">
          Advanced search
        </v-btn>
      </template>
      <v-btn
          v-if="$store.state.isLogin === false"
          class="ml-4"
          @click="toLogin"
      >
        Login
      </v-btn>
      <div v-if="$store.state.isLogin === true">
        {{ $store.state.username }}
        <v-btn
            class="ml-4"
            @click="toLogout">
          Logout
        </v-btn>
      </div>
    </v-app-bar>
    <div class="mt-3" v-if="isAdvanceSearch">
      <v-toolbar
          flat
      >
        <v-select
            class="ma-2"
            v-model="selected_country"
            :items="countries"
            label="Country"
        ></v-select>
        <v-select
            class="ma-2"
            v-model="selected_type"
            :items="selectType"
            label="Search type"
        ></v-select>
        <v-select
            class="ma-2"
            v-model="selected_theme"
            :items="themes"
            label="Theme"
        ></v-select>
        <v-btn
            @click="searchTerm"
            class="ma-4"

            raised
        >
          Search
        </v-btn>
        <v-btn
            class="ma-2"
            @click="sortByDate"
        >
          Sort by date
        </v-btn>
      </v-toolbar>
    </div>
  </div>
</template>

<script>
import {getAllCountries, getAllTheme, getSearch} from "@/api";
import {forEach} from "core-js/internals/array-iteration";

export default {
  name: "HeaderComponent",
  data: () => ({
    drawer: false,
    group: null,
    items: [],
    countries: [],
    themes: [],
    isLoading: false,
    search: null,
    tab: 0,
    isAdvanceSearch: false,
    selected_theme: '',
    selected_country: '',
    selected_type:'',
    selectType:[
      { text: 'OR', value: 'OR' },
      { text: 'AND', value: 'AND' },
    ],
  }),
  computed: {

  },
  watch: {
    tab(val) {
        this.$emit('tab-change', val);
    },
    async search(term) {
      if (this.items.length < 0 || this.items.length == null) {
        //console.log(term);
        this.items = [];
        return
      }

      this.isLoading = true;
      // console.log(term);

      await this.getQuerySet(term);
      const searchQuery = JSON.parse((JSON.stringify(this.$route.query)));
      searchQuery.search_phase = term;
      await this.$router.push({query: searchQuery});
    }
  },
  async created() {
    //console.log(this.$route.query.search_phase);
    await this.getQuerySet(this.$route.query.search_phase);
    await getAllCountries().then(res => {

      console.log(res.data.data);
      forEach(res.data.data, (item) => {
        this.countries.push({
          text: item.country,
          value: item.country
        });
      });
    });
    await getAllTheme().then(res => {
      forEach(res.data.data, (item) => {
        this.themes.push({
          text: this.capitalizeFirstLetter(item.theme),
          value: item.theme
        });
      });
    });
  },
  methods: {
    searchTerm() {
      let search_term;
      if (this.selected_country && this.selected_theme && this.selected_type) {
        search_term = this.selected_country + ' ' + this.selected_type + ' ' + this.selected_theme;
      } else if (this.selected_country){
        search_term = this.selected_country;
      } else if (this.selected_theme){
        search_term = this.selected_theme;
      } else {
        search_term = this.search;
      }
      this.getQuerySet(search_term);
    },
    toNews(url) {
      window.location = url;
    },
    sortByDate() {
      return this.items.sort((a, b) => {
        return new Date(b.publish_date) - new Date(a.publish_date);
      });
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    getQuerySet(term) {
      getSearch(term)
          .then((response) => {
            // console.log(response.data.data);
            this.items = response.data.data['newsarray'];
            this.$emit('update:items', this.items);
            this.totalPages = Math.ceil(this.items.length / this.PageSize);
            this.$route.query.search_phase = term;

            // console.log(this.items);
            // console.log(this.items[0]);
          })
          .catch((err) => {
            console.error(err);
            this.items = [];
          })
          .finally(() => {
            this.isLoading = false;
          })
    },
    toHome() {
      this.$router.push('/');
    },
    toLogin() {
      this.$router.push('/login');
    },
    toLogout() {
      this.$store.commit('logout');
      this.$router.push('/');
    },
    timestampConvert(timeStamp) {
      let date = new Date(timeStamp);
      let year = date.getFullYear();
      let month = date.getMonth();
      let day = date.getDate();
      if (day < 10) {
        day = '0' + day;
      }
      if (month < 10) {
        month += 1;
        if (month !== 10) {
          month = '0' + month;
        }
      }
      return day + '/' + month + '/' + year
    },
  }
}
</script>

<style scoped>

</style>
