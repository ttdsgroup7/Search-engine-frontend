<template>
  <div>
    <v-overlay :value="showRating">
      <v-card class="white"
              outlined>
        <v-card-title>
        <span class="headline text--primary">
          <v-icon color="blue">mdi-star</v-icon>
          <span>Rating!</span>
        </span>
        </v-card-title>

        <v-card-text>
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
          <v-btn class="text--primary" text @click="closeOverlay">
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-overlay>
  </div>
</template>

<script>
// import {updateRecords} from "@/api";
export default {
  name: "RatingComponent",
  data: () => ({
    rating: 3,
    overlay: false

  }),
  props: ['showRating', 'newsId'],
  methods: {
    closeOverlay: function () {
      console.log(this.newsId);
      console.log(this.rating);
      localStorage.getItem('user_id');
      console.log(localStorage.getItem('user_id'));
      this.showRating = false;
    },
  },
}
</script>

<style scoped>

</style>
