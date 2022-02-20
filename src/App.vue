<template>
  <v-app>
    <v-main>
      <router-view/>
    </v-main>
    <v-footer app>
      © 2020 UOE TTDS GROUP WORK NEWS SEARCH.  All rights reserved
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    links: [
      'Dashboard',
      'Messages',
      'Profile',
      'Updates',
    ],
  }),
};
</script>
