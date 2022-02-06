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
                    <template v-for="(item, index) in items">
                      <v-list-item :key="item.head_line" :href="item.tag">
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
  </v-col>
</template>

<script>
import {setRecommends} from "@/api";
export default {
  name: "RelatedReadingComponent",
  data (){
    return {
      items:[],
      username: 'test',
    }
  },
  created(){
    // this.username = this.$store.state.username;
    this.getRelated();
  },
  methods: {
    getRelated(){
      setRecommends(this.username).then(res => {
        this.items = res.data.data;
      })
    }
  }
}
</script>

<style scoped>

</style>
