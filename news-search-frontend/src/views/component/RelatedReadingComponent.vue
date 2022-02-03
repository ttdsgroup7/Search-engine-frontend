<template>
  <v-col
      cols="6"
      md="4"
  >
    <h1 class="ma-4">
      Related reading
    </h1>
    <v-list two-line>
      <!--            <v-list-item-group-->
      <!--                v-model="selected"-->
      <!--                active-class="yellow&#45;&#45;text"-->
      <!--                multiple-->
      <!--            >-->
      <!--              <template v-for="(item, index) in items">-->
      <!--                <v-list-item :key="item.head_line" :href="item.tag">-->
      <!--                  <template v-slot:default>-->
      <!--                    <v-list-item-content>-->
      <!--                      <v-list-item-title v-text="item.head_line"></v-list-item-title>-->

      <!--                      <v-list-item-subtitle-->
      <!--                          class="text&#45;&#45;primary"-->
      <!--                          v-text="item.head_line"-->
      <!--                      ></v-list-item-subtitle>-->

      <!--                      <v-list-item-subtitle v-text="item.publish_date"></v-list-item-subtitle>-->
      <!--                    </v-list-item-content>-->
      <!--                  </template>-->
      <!--                </v-list-item>-->

      <!--                <v-divider-->
      <!--                    v-if="index < items.length - 1"-->
      <!--                    :key="index"-->
      <!--                ></v-divider>-->
      <!--              </template>-->
      <!--            </v-list-item-group>-->
    </v-list>
  </v-col>
</template>

<script>
export default {
  name: "RelatedReadingComponent"
}
</script>

<style scoped>

</style>
