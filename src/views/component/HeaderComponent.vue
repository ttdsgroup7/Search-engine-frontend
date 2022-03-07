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
          <v-list-item :href="toMap">
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
          v-model="model"
          :items="search_correction"
          :loading="isLoading"
          :search-input.sync="search"
          clearable
          hide-details
          hide-selected
          item-text="name"
          label="Search for a news..."
          solo
      >
        <template v-slot:no-data>
          <v-list-item>
            <v-list-item-title>
              Search for your daily
              <strong>news</strong>
            </v-list-item-title>
          </v-list-item>
        </template>
        <template v-slot:item="{ item }">
          <v-list-item-content>
            <v-list-item-title v-text="item"></v-list-item-title>
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
          <v-tab
              v-for="item in themes"
              :key="item.value"
              :value="tab"
          >
            {{ item.text }}
          </v-tab>
        </v-tabs>
        <v-btn @click="showAdvance">
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
        <v-chip class="ma-3"  text-color="black">
          {{ $store.state.username }}
        </v-chip>

        <v-btn
            class="ml-2"
            @click="toLogout">
          Logout
        </v-btn>
      </div>
    </v-app-bar>
    <div class="mt-6 pa-3" v-if="isAdvanceSearch">
      <v-toolbar
          flat
      >
        <v-select
            class="ma-2"
            v-model="selected_country"
            :items="countries"
            label="Select a country"
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
    <div class="ma-6" v-if="queryFix">
      <p>Your query should be <span class="fixed_term">{{ fixedTerm }}</span></p>
      <p>You are trying to search <span class="search_term" @click="wrongSearch(fixedTerm)">{{ wrongTerm }}</span></p>
    </div>
  </div>
</template>

<script>
import {getAllCountries, getAllTheme, getNewsByTheme, getSearch, getWordCorrection} from "@/api";
import {forEach} from "core-js/internals/array-iteration";

export default {
  name: "HeaderComponent",
  props: ['pageSize', 'pageNumb', 'totalPages'],
  data: () => ({
    drawer: false,
    group: null,
    newItems: [],
    countries: [],
    themes: [],
    isLoading: false,
    search: null,
    tab: null,
    queryFix: false,
    fixedTerm: "",
    wrongTerm: "",
    isAdvanceSearch: false,
    selected_theme: '',
    selected_country: '',
    selected_type: '',
    search_correction: [],
    model:null,
    selectType: [
      {text: 'OR', value: 'OR'},
      {text: 'AND', value: 'AND'},
    ],
    toMap: 'http://data-map-d3.herokuapp.com/index.html',
  }),
  computed: {
  },
  watch: {
    async tab(val) {
      if (val !== 0) {
        let selected = this.themes[val - 1].value;
        // console.log(selected);
        await getNewsByTheme(selected, this.$props.pageNumb, this.$props.pageSize)
            .then((response) => {
              console.log(response.data)
              this.newItems = response.data.data;
              this.$emit('update:items', this.newItems);
              const searchQuery = JSON.parse((JSON.stringify(this.$route.query)));
              searchQuery.search_phase = selected;
              this.$router.push({query: searchQuery});
            })
      } else {
        // console.log(this.$route.query);
        await this.getQuerySet(this.$route.query.search_phase, this.$props.pageNumb, this.$props.pageSize);
      }
    },
    async pageNumb(val){
      await this.getQuerySet(this.$route.query.search_phase, val, this.$props.pageSize);
    },
    async search(term) {
      if (this.newItems.length < 0 || this.newItems.length == null) {
        //console.log(term);
        this.newItems = [];
        return
      }
      await getWordCorrection(term)
          .then((response) => {
            // console.log(response.data.data);
            this.search_correction = response.data.data;
          })

      this.isLoading = true;
      // console.log(term);

      await this.getQuerySet(term, this.$props.pageNumb, this.$props.pageSize);
      const searchQuery = JSON.parse((JSON.stringify(this.$route.query)));
      searchQuery.search_phase = term;
      await this.$router.push({query: searchQuery});
    }
  },
  async beforeMount() {
    //console.log(this.$route.query.search_phase);
    await this.getQuerySet(this.$route.query.search_phase, this.$props.pageNumb, this.$props.pageSize);

    await getAllCountries().then(res => {
      forEach(res.data.data, (item) => {
        this.countries.push({
          text: item.country,
          value: item.country
        });
      });
    });
    await getAllTheme().then(res => {
      forEach(res.data.data, (item) => {
        if (item.theme === "world") {
          this.themes.splice(0, 0, {
            text: this.capitalizeFirstLetter(item.theme),
            value: item.theme
          })
        } else {
          this.themes.push({
            text: this.capitalizeFirstLetter(item.theme),
            value: item.theme
          });
        }
        // console.log(this.themes);
      });
    });
  },
  methods: {
    showAdvance() {
      this.isAdvanceSearch = !this.isAdvanceSearch;
      window.scrollTo(0, 0);
    },
    wrongSearch(term) {
      console.log(term)
      this.getQuerySet(term, this.$props.pageNumb, this.$props.pageSize);
      this.queryFix = false;
    },
    searchTerm() {
      let search_term;
      if (this.selected_country && this.selected_theme && this.selected_type) {
        this.selected_country = this.selected_country.toLowerCase();
        this.selected_theme = this.selected_theme.toLowerCase();
        search_term = this.selected_country + ' ' + this.selected_type + ' ' + this.selected_theme;
      } else if (this.selected_country) {
        search_term = this.selected_country;
        search_term = search_term.toLowerCase();
      } else if (this.selected_theme) {
        search_term = this.selected_theme;
        search_term = search_term.toLowerCase();
      } else {
        search_term = this.search;
      }
      this.getQuerySet(search_term);
    },
    toNews(url) {
      window.location = url;
    },
    sortByDate() {
      return this.newItems.sort((a, b) => {
        return new Date(b.publish_date) - new Date(a.publish_date);
      });
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    getQuerySet(term, pageNumb, pageSize) {
      getSearch(term, pageNumb, pageSize)
          .then((response) => {
            console.log(response.data.data['newsarray']);
            this.newItems = response.data.data['newsarray'];
            this.$emit('update:items', this.newItems);
            this.$route.query.search_phase = term;
            if (response.data.data.rightQueryString) {
              this.wrongTerm = term
              this.queryFix = true;
              this.fixedTerm = response.data.data.rightQueryString;
            } else {
              this.queryFix = false;
            }
            // console.log(this.items);
            // console.log(this.items[0]);
          })
          .catch((err) => {
            console.error(err);
            this.newItems = [];
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
/*.fixed_term{*/
/*  text-decoration: underline;*/
/*  color: red;*/
/*}*/
/*.fixed_term:hover{*/
/*  cursor: pointer;*/
/*  color: rgba(255, 60, 0, 0.78);*/
/*}*/
.search_term {
  text-decoration: underline;
  color: red;
}

.search_term:hover {
  cursor: pointer;
  color: rgba(255, 60, 0, 0.78);
}
</style>
