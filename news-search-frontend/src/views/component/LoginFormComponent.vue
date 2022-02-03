<template>
  <v-form
      ref="form"
      v-model="valid"
      lazy-validation
  >
    <v-text-field
        v-model="name"
        :counter="10"
        :rules="nameRules"
        label="Username"
        required
    ></v-text-field>

    <v-text-field
        v-model="email"
        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
        :type="show2 ? 'text' : 'password'"
        name="input-10-2"
        label="Visible"
        hint="At least 8 characters"
        value="12345678"
        class="input-group--focused"
        @click:append="show2 = !show2"
    ></v-text-field>

    <v-text-field
        v-model="email"
        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
        :type="show2 ? 'text' : 'password'"
        name="input-10-2"
        label="Visible"
        hint="At least 8 characters"
        value="12345678"
        class="input-group--focused"
        @click:append="show2 = !show2"
    ></v-text-field>

    <v-select
        v-model="select"
        :items="items"
        :rules="[v => !!v || 'Item is required']"
        label="Item"
        required
    ></v-select>


    <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        @click="validate"
    >
      Validate
    </v-btn>

    <v-btn
        color="error"
        class="mr-4"
        @click="reset"
    >
      Reset Form
    </v-btn>

  </v-form>
</template>

<script>
export default {
  name: "LoginFormComponent",
  data: () => ({
    valid: true,
    name: '',
    show2: false,
    nameRules: [
      v => !!v || 'Name is required',
      v => (v && v.length <= 10) || 'Name must be less than 10 characters',
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
    select: null,
    items: [
      'Item 1',
      'Item 2',
      'Item 3',
      'Item 4',
    ],
    checkbox: false,
  }),

  methods: {
    validate() {
      this.$refs.form.validate()
    },
    reset() {
      this.$refs.form.reset()
    },
  },
}
</script>

<style scoped>

</style>
