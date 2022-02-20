<template>
  <v-container>
    <WorldMapVue
        @click="onClickMapCountry"
    >
      <template v-slot:overlay>
        // -> Your components here
      </template>
    </WorldMapVue>
  </v-container>
</template>

<script>
import Countries from "../utils/countries.js";

export default {
  name: 'Home',

  data: () => ({
    showMapOverlay: false,
    country: Countries

  }),
  methods: {
    onMouseLeaveMapCountry() {
      this.showMapOverlay = false
    },
    onClickMapCountry(data) {
      console.log('Click Country', data)
    },
  }
}
</script>
