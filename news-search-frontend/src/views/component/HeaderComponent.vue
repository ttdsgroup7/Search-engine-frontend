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
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Account</v-list-item-title>
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
        <template v-slot:item="{ item }">
          <v-list-item-content>
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
            Trading
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
          class="ml-4"
          @click="isAdvanceSearch = !isAdvanceSearch"
      >
        Login
      </v-btn>
    </v-app-bar>
    <div class="mt-3" v-if="isAdvanceSearch">
      <v-toolbar
          flat
      >
        <v-select
            class="ma-2"
            :items="drop_one"
            label="Area"
        ></v-select>
        <v-select
            class="ma-2"
            :items="drop_one"
            label="Time"
        ></v-select>
        <v-select
            class="ma-2"
            :items="drop_one"
            label="Precise Searching"
        ></v-select>
      </v-toolbar>
    </div>
  </div>
</template>

<script>
import {getSearch} from "@/api";

export default {
  name: "HeaderComponent",
  data: () => ({
    drawer: false,
    group: null,
    items: [],
    isLoading: false,
    model: null,
    search: null,
    tab: 0,
    isAdvanceSearch: false,
    drop_one: [
      {text: 'All', value: 'all'},
      {text: 'News', value: 'news'},
      {text: 'Trading', value: 'trading'},
      {text: 'Blog', value: 'blog'},
    ],
  }),
  watch: {
    async search(term) {
      if (this.items.length < 0 || this.items.length == null) {
        console.log(term);
        this.items = [];
        return
      }

      this.isLoading = true;
      console.log(term);
      term = term.toLowerCase();

      await this.getQuerySet(term);
    }
  },
  async created() {
    console.log(this.$route.query.search_phase);
    await this.getQuerySet(this.$route.query.search_phase);
  },
  methods: {
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
    }
  }
}
</script>

<style scoped>

</style>
