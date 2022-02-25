<template>
  <div>
    <v-btn @click="overlay = true">
      show overlay
    </v-btn>
    <v-overlay :value="overlay">
      <v-card class=""
              outlined>
        <v-card-title>
        <span class="headline">
          <v-icon>mdi-star</v-icon>
          <span>Rating!</span>
        </span>
        </v-card-title>

        <v-card-text>
          <div class="text--primary red">
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
          <v-btn text @click="overlay = false">
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-overlay>
  </div>
</template>

<script>
export default {
  name: "RatingComponent",
  data: () => ({
    rating: 3,
    overlay: false

  }),
  methods: {

  },
  watch: {
    rating(val) {
      console.log(val)
    },
  }
}
</script>

<style scoped>

</style>
