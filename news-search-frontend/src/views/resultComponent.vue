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
          :items="items_test"
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
            <span v-text="item.head_line"></span>
          </v-chip>
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
        <v-btn>
          Tools
        </v-btn>
      </template>
      <v-switch
          v-model="advSearch"
          label="Advance search"
      ></v-switch>

      <v-btn
          fab
          small

      >
        <!--        <v-icon>-->
        <!--          mdi-close-->
        <!--        </v-icon>-->
        <v-icon>
          mdi-pencil
        </v-icon>
      </v-btn>
    </v-app-bar>

    <v-container fluid>
      <v-row no-gutters>
        <v-col
            cols="12"
            sm="6"
            md="8"
        >
          <h4>The search time: xxxxx s</h4>
          <v-card>

          </v-card>
          <v-col
              v-for="(item, index) in analyseListItem"
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
                  <v-card-text>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris et condimentum nibh, in iaculis
                    velit. Praesent at urna dolor. Praesent tempor facilisis erat non aliquet. Nulla eu magna egestas
                    ante commodo tempus sit amet feugiat nibh. Nunc porttitor mauris id turpis tempus, sit amet interdum
                    risus placerat.
                  </v-card-text>
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
                    size="210"
                    tile
                >
                  <v-img :src="src"></v-img>
                </v-avatar>
              </div>
            </v-card>
          </v-col>
        </v-col>

        <v-col
            cols="6"
            md="4"
        >
          <h1 class="ma-4">
            Related reading
          </h1>
          <v-list two-line>
            <v-list-item-group
                v-model="selected"
                active-class="yellow--text"
                multiple
            >
              <template v-for="(item, index) in items_test">
                <v-list-item :key="item.head_line" :href="item.tag">
                  <template v-slot:default>
                    <v-list-item-content>
                      <v-list-item-title v-text="item.head_line"></v-list-item-title>

                      <v-list-item-subtitle
                          class="text--primary"
                          v-text="item.head_line"
                      ></v-list-item-subtitle>

                      <v-list-item-subtitle v-text="item.publish_date"></v-list-item-subtitle>
                    </v-list-item-content>
                  </template>
                </v-list-item>

                <v-divider
                    v-if="index < items.length - 1"
                    :key="index"
                ></v-divider>
              </template>
            </v-list-item-group>
          </v-list>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import {getSearch} from "@/api";

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
    items_test: [{
      "publish_date": "2022-01-02T10:56:53.000Z",
      "head_line": "Vaccination centre relocates to new site",
      "tag": "https://bbc.co.uk/news/uk-england-cumbria-59852247",
      "type": "news"
    }, {
      "publish_date": "2022-01-01T12:04:40.000Z",
      "head_line": "Muted celebrations as Hogmanay curtailed by Covid",
      "tag": "https://bbc.co.uk/news/uk-scotland-59846640",
      "type": "news"
    }, {
      "publish_date": "2022-01-01T13:17:27.000Z",
      "head_line": "Pubs 'exceptionally quiet' as Wales marks new year",
      "tag": "https://bbc.co.uk/news/uk-wales-59846561",
      "type": "news"
    }, {
      "publish_date": "2022-01-01T15:00:19.000Z",
      "head_line": "Fireworks mark subdued UK new year",
      "tag": "https://bbc.co.uk/news/uk-59844031",
      "type": "news"
    }, {
      "publish_date": "2022-01-01T16:17:08.000Z",
      "head_line": "Antarctic station hit by Covid-19 outbreak",
      "tag": "https://bbc.co.uk/news/world-europe-59848160",
      "type": "blog"
    }],
    items: [],
    src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
    model: null,
    search: null,
    tab: 0,
    drawer: false,
    advSearch: false,
    group: null,
    today: ''
  }),
  created() {
    console.log(this.$route.query.search_phase);
    this.model = this.$route.query.search_phase;
    this.getQuerySet(this.model);
  },
  computed: {
    analyseListItem() {
      let new_list = [];
      if (this.tab === 0){
        new_list = this.items_test.filter(i => i.type === 'news');
      } else if (this.tab === 1){
        // let today = new Date().toJSON().slice(0,10).replace(/-/g,'/');
        new_list = this.items_test.filter(i => this.timestampConvert(i.publish_date) === '01/01/2022');
      } else {
        new_list = this.items_test.filter(i => i.type === 'blog');
      }
      return new_list
    }
  },
  watch: {
    search(term) {
      if (this.items.length < 0 || this.items.length == null) {
        this.items = []
        return
      }

      this.isLoading = true

      this.getQuerySet(term);
    }
  },
  methods: {
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
        month = '0' + month;
      }
      return day + '/' + month + '/' + year
    },
    getQuerySet(term) {
      getSearch(term)
          .then((response) => {
            console.log(response.data)
            this.items = response.data['newsarray']
          })
          .catch((err) => {
            console.error(err)
            this.items = []
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
