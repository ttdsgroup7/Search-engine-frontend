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
          <h4>The search time: xxxxx s</h4>
          <v-card>

          </v-card>
          <v-col
              v-for="(item, index) in visiblePages"
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
                    {{ item.new_abstract }}
                  </v-card-text>
                  <v-divider class="mx-4"></v-divider>
                  <v-card-text>
                    <v-chip-group
                        active-class="deep-purple accent-4 white--text"
                        column
                    >
                      <v-chip>{{ capitalizeFirstLetter(item.theme) }}</v-chip>

                      <v-chip v-if="item.country !== ''">{{ countryCodes(item.country)[0] }}</v-chip>

                      <v-chip v-if="countryCodes(item.country)[1] != null">{{ countryCodes(item.country)[1] }}</v-chip>


                    </v-chip-group>
                  </v-card-text>
                  <v-card-actions>
                    <v-btn
                        class="ml-2 "
                        outlined
                        rounded
                        small
                        :href="item.url"
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

       <related-reading-component></related-reading-component>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import {getSearch} from "@/api";
import HeaderComponent from "@/views/component/HeaderComponent";
import RelatedReadingComponent from "@/views/component/RelatedReadingComponent";

export default {
  name: "resultComponent",
  components: {
    HeaderComponent,
    RelatedReadingComponent
  },
  data: () => ({
    isAdvanceSearch: null,
    drop_one:['Foo', 'Bar', 'Fizz', 'Buzz'],
    isLoading: false,
    items: [],
    src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
    model: null,
    search: null,
    tab: 0,
    drawer: false,
    advSearch: false,
    group: null,
    today: '',
    page: 1,
    totalPages: null,
    PageSize: 10,
    ifCounty: false,
  }),
  created() {
    console.log(this.$route.query.search_phase);
    this.model = this.$route.query.search_phase;
    this.getQuerySet(this.model);
  },
  computed: {
    // analyseListItem() {
    //   let new_list = [];
    //   // if (this.tab === 0){
    //   //   new_list = this.items.filter(i => i.type === 'news');
    //   // } else
    //   if (this.tab === 1){
    //     // let today = new Date().toJSON().slice(0,10).replace(/-/g,'/');
    //     new_list = this.items.filter(i => this.timestampConvert(i.publish_date) === '01/01/2022');
    //   } else {
    //     return this.items;
    //   }
    //   // else {
    //   //   new_list = this.items.filter(i => i.type === 'blog');
    //   // }
    //   return new_list
    // }
    visiblePages() {
      return this.items.slice((this.page - 1) * this.PageSize, this.page * this.PageSize);
    }
  },
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
  methods: {
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    countryCodes(string){
      let countryName, continentName;
      if (string.includes('-')){
        countryName = string.split('-')[0];
        if(countryName === 'uk'){
          countryName = 'UK';
        }
        if (string.includes('_')) {
          this.ifCounty = true;
          continentName = string.split('-')[1].replaceAll('_', ' ');
          continentName = this.capitalizeFirstLetter(continentName);
          return [countryName, continentName];
        }
        continentName = null;
        return [countryName];
      } else {
        return [string];
      }
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
        month = '0' + month;
      }
      return day + '/' + month + '/' + year
    },
    getQuerySet(term) {
      getSearch(term)
          .then((response) => {
            // console.log(response.data.data);
            this.items = response.data.data['newsarray'];
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
