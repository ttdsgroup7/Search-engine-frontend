<template>
  <v-col
      cols="6"
      md="4"
  >
    <h1 class="ma-4">
      Related reading
    </h1>
    <v-list two-line>
      <v-list-item-group
          active-class="yellow--text"
          multiple
      >
        <template v-for="(item, index) in relatedNewsUser">
          <v-list-item :key="item.id" :href="item.url" @click="visitRecords">
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
        You've got <strong>5</strong> new updates on your timeline!.
      </v-alert>
    </div>
  </v-col>
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
    console.log('RelatedReadingComponent beforeCreate');
    this.$store.dispatch('getRelatedNews');
  },
  computed: {
    relatedNewsUser() {
      console.log(this.$store.state.relatedNews);
      return this.$store.state.relatedNews;
    },
  },
  methods: {
    visitRecords() {
      updateRecords({
        news_id: this.items.id,
        user_id: localStorage.getItem('user_id'),
        prefer_degree: 1,
      }).then((response) => {
        console.log(response);
        this.alert = true;
      });
    },
  },
}
</script>

<style scoped>

</style>
