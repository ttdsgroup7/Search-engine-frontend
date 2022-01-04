<template>
  <v-container>
    <search-component></search-component>
  </v-container>
</template>

<script>
  import searchComponent from "@/views/searchComponent";
  import HelloWorld from "@/components/HelloWorld";

  export default {
    name: 'Home',

    components: {
      searchComponent,
      HelloWorld
    },
  }
</script>
