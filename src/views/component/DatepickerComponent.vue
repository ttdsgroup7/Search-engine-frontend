<template>
  <v-menu
      v-model="dateMenu"
      :close-on-content-click="false"
      :nudge-right="40"
      transition="scale-transition"
      offset-y
      min-width="290px"
      max-width="290px"
  >
    <template v-slot:activator="{ on }">
      <v-text-field
          :label="label"
          readonly
          hide-details
          :value="dateValue"
          v-on="on"
          @focus="focusDate"
          @blur="blurDate"
      ></v-text-field>
    </template>
    <v-date-picker locale="en-in" v-model="dateValue" no-title @input="dateMenu = false"></v-date-picker>
  </v-menu>
</template>
<script>
export default {
  name: "DatepickerComponent",
  data() {
    return {
      dateMenu: false,
      dateValue: null
    };
  },
  props: {
    label: {
      type: String,
      required: true
    }
  },
  watch: {
    dateValue(val){
      this.$emit('clicked', val)
    }
  },
  methods: {
    focusDate() {
      setTimeout(() => {
        if (!this.dateMenu) {
          this.dateMenu = true;
        }
      }, 200);
    },
    blurDate() {
      setTimeout(() => {
        if (this.dateMenu) {
          this.dateMenu = false;
        }
      }, 200);
    }
  }
};
</script>
