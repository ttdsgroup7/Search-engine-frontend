<template>
  <v-form
      ref="form"
      v-model="valid"
      lazy-validation
  >
    <v-text-field
        v-model="username"
        :counter="10"
        :rules="usernameRules"
        label="Username"
        required
    ></v-text-field>

    <v-text-field
        v-model="password"
        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
        :type="show2 ? 'text' : 'password'"
        :rules="passwordRules"
        name="input-10-2"
        label="Visible"
        hint="At least 8 characters"
        value="12345678"
        class="input-group--focused"
        @click:append="show2 = !show2"
    ></v-text-field>


    <v-btn
        color="success"
        class="mr-4"
        @click="register"
    >
      Register
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
import {register} from "@/api";

export default {
  name: "RegisterComponent",
  data: () => ({
    valid: true,
    username: '',
    show2: false,
    usernameRules: [
      v => !!v || 'Name is required',
      v => (v && v.length <= 10) || 'Name must be less than 10 characters',
    ],
    password: '',
    passwordRules: [
      v => !!v || 'Password is required',
    ],
    select: null,
    checkbox: false,
  }),

  methods: {
    reset() {
      this.$refs.form.reset()
    },
    registerAccount(){
      register({
        password: this.password,
        username: this.username,
      })
      .then(response => {
        console.log(response);
        this.$store.commit('setUser', this.username);
      })
      .catch(error => {
        console.log(error);
      })
      .finally(() => {
        console.log('finally');
      });
    }
  },
}
</script>

<style scoped>

</style>
