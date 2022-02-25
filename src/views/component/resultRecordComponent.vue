<template>
  <v-container fluid>
    <v-row no-gutters>
      <v-col
          cols="12"
          sm="6"
          md="8"
      >
        <v-card>

        </v-card>
        <v-col
            v-for="(item, index) in visiblePages"
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
            v-model="page"
            :length="totalPages"
            circle
            total-visible="7"
            next-icon="mdi-menu-right"
            prev-icon="mdi-menu-left"
        ></v-pagination>
      </v-col>
      <rating-component v-if="showRating" :news-id="news_id" :show-rating="showRating"></rating-component>
      <related-reading-component v-show="this.$store.state.isLogin !== false"></related-reading-component>
    </v-row>
  </v-container>
</template>

<script>
import RatingComponent from "@/views/component/RatingComponent";
export default {
  name: "resultRecordComponent",
  components: {
    RatingComponent
  },
  props: {
    newsId: {
      type: Number,
      required: true
    },
    showRating: {
      type: Boolean,
      required: true
    }
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
    showRating: false,
  }),
  computed: {


    visiblePages() {
      return this.items.slice((this.page - 1) * this.PageSize, this.page * this.PageSize);
    }
  }
  ,
  beforeCreate() {

  }
  ,
  watch: {}
  ,
  methods: {
    visitNews(news){
      console.log(news);
      // window.open(news.url, '_blank');
      this.news_id = news.id;
      this.showRating = true;
    },
    getItems(item) {
      this.items = item;
      this.totalPages = Math.ceil(this.items.length / this.PageSize);
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
