<template>
  <div>
    <header-component @update:items="getItems" :page-numb="this.page" :page-size="this.PageSize"></header-component>
    <v-container fluid>
      <v-row no-gutters>
        <v-col
            cols="12"
            sm="6"
            md="8"
        >
          <v-card v-if="items.length === 0">
            <v-alert
                :value="true"
                type="error"
                icon="info"
            >
                <span class="body-1">
                  No results found.
                </span>
            </v-alert>
          </v-card>
          <v-col

              v-for="(item, index) in items"
              :key="index"
              cols="12"

          >
            <v-card
                class="elevation-1"
                :class="{'elevation-1': item.isActive}"
                :style="{'background-color': item.isActive ? '#f5f5f5' : '#ffffff'}"
                @click="visitNews({url: item.url, id: item.id})"
            >
              <div class="d-flex flex-no-wrap justify-space-between">
                <div>
                  <v-card-title
                      class="text-h5"
                      v-text="item.head_line"
                  ></v-card-title>

                  <v-card-subtitle v-text="timestampConvert(item.publish_date)"></v-card-subtitle>
                  <v-card-text>
                    {{ item.news_abstract }}
                  </v-card-text>
                  <v-divider class="mx-4"></v-divider>
                  <v-card-text>
                    <v-chip-group
                        active-class="deep-purple accent-4 white--text"
                        column
                    >
                      <v-chip>{{ capitalizeFirstLetter(item.theme) }}</v-chip>

                      <v-chip v-if="item.country !== null && item.country !== 'None'">{{ item.country }}</v-chip>


                    </v-chip-group>
                  </v-card-text>
                </div>

                <v-avatar
                    class="ma-3"
                    size="210"
                    tile
                >
                  <v-img :src="item.image"></v-img>
                </v-avatar>
              </div>
            </v-card>
          </v-col>
          <v-pagination
              v-if="this.items.length !== 0"
              v-model="page"
              :length="totalPages"
              circle
              total-visible="7"
              next-icon="mdi-menu-right"
              prev-icon="mdi-menu-left"
          ></v-pagination>
        </v-col>
        <v-overlay :value="showRating" v-if="this.$store.state.isLogin">
          <v-card class="white"
                  outlined
          >
            <v-app-bar class="white">
              <v-toolbar-title class="text-h6 grey--text pl-0">
                <v-icon color="blue">mdi-star</v-icon>
                <span>Rating!</span>
              </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn
                  icon
                  class="grey"
                  @click="showRating = false"
              >
                <v-icon>mdi-close</v-icon>
              </v-btn>
            </v-app-bar>

            <v-card-text class="align-center">
              <div class="text--primary">
                How would you rate the article?
                <br>
                Please tell us your through!
              </div>
              <v-rating
                  v-model="rating"
                  :max="5"
                  :value="rating"
              ></v-rating>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn class="text--primary" text @click="sendRating">
                Submit
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-overlay>
        <v-col
            cols="6"
            md="4"
        >
          <related-reading-component v-if="this.$store.state.isLogin !== false"></related-reading-component>
          <p v-else> You have to login to load your recommendations!</p>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>

import HeaderComponent from "@/views/component/HeaderComponent";
import RelatedReadingComponent from "@/views/component/RelatedReadingComponent";
import {updateRecords} from "@/api";

export default {
  name: "resultComponent",
  components: {
    HeaderComponent,
    RelatedReadingComponent,
  },
  data: () => ({
    isLoading: false,
    items: [],
    today: '',
    page: 1,
    totalPages: null,
    PageSize: 10,
    ifCounty: false,
    countries: [],
    theme: [],
    news_id: null,
    rating: 3,
    showRating: false,
  }),
  computed: {},
  beforeCreate() {

  },
  watch: {
    page() {
      window.scrollTo(0, 0);
    }
  },
  methods: {
    visitNews(news) {
      console.log(news);
      window.open(news.url, '_blank');
      this.news_id = news.id;
      setTimeout(() => {
        this.showRating = true;
      }, 500);

    },
    sendRating() {
      updateRecords({
        newsLogsItemList: [{
          news_id: this.news_id,
          // user_id: localStorage.getItem('user_id'),
          prefer_degree: this.rating
        }],
        username: this.$store.state.username,
      }).then((response) => {
        console.log(response);
        this.showRating = false;
      });
    },
    getItems(item) {
      // console.log(item);
      this.items = item.list;
      this.totalPages = item.pages;
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
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
.elevation-1 {
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
}
</style>
