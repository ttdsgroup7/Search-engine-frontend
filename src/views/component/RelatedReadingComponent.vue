<template>
  <div>
    <v-alert
        v-model="alert"
        dismissible
        color="cyan"
        elevation="2"
        colored-border
        dark
        border="top"
        icon="mdi-home"
        transition="scale-transition"
    >
      You've submit <strong>1</strong> rating for your record!.
    </v-alert>
    <div>
      <h1 class="ma-4">
        Related reading
      </h1>
      <v-divider></v-divider>
      <div>
        <v-list two-line v-if="relatedNewsUser !== 0">
          <v-list-item-group
              active-class="yellow--text"
              multiple
          >
            <template v-for="(item, index) in relatedNewsUser">
              <v-list-item :key="item.id" @click="visitRecords(item.url)">
                <template v-slot:default>
                  <v-list-item-content>
                    <v-list-item-title v-text="item.head_line"></v-list-item-title>

                    <v-list-item-subtitle
                        class="text--primary"
                        v-text="item.news_abstract"
                    ></v-list-item-subtitle>

                    <v-list-item-subtitle v-text="timestampConvert(item.publish_date)"></v-list-item-subtitle>
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
        <h1 class="ma-4" v-else>
          You don't have any recommendations at the moment!
        </h1>
      </div>
    </div>
  </div>
</template>

<script>
import {updateRecords} from "@/api";


export default {
  name: "RelatedReadingComponent",
  data() {
    return {
      items: [],
      alert: false,
    }
  },
  beforeCreate() {
    // console.log('RelatedReadingComponent beforeCreate');
    if (this.$store.state.isLogin) {
      this.$store.dispatch('getRelatedNews');
    }
  },
  computed: {
    relatedNewsUser() {
      // console.log(this.$store.state.relatedNews);
      return this.$store.state.relatedNews.list;
    },
  },
  methods: {
    visitRecords(newsUrl) {
      updateRecords({
        news_id: this.items.id,
        user_id: localStorage.getItem('user_id'),
        prefer_degree: 1,
      }).then((response) => {
        console.log(response);
        window.open(newsUrl, '_blank');
        this.alert = true;
      });
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
  },
}
</script>

<style scoped>

</style>
