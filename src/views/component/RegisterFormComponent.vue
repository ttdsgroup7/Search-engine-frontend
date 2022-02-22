<template>
  <v-row
      class="ma-7 pa-3"
      no-gutters>
    <v-col
        md="6"
        offset-md="3">
      <v-form
          ref="form"
          v-model="valid"
          lazy-validation
      >
        <v-text-field
            v-model="username"
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
            label="Enter your password"
            hint="At least 8 characters"
            value="12345678"
            class="input-group--focused"
            @click:append="show2 = !show2"
        ></v-text-field>


        <v-btn
            color="success"
            class="mr-4"
            @click="registerAccount"
        >
          Register
        </v-btn>
        <v-btn
            color="warning"
            class="mr-4"
            @click="goBack"
        >
          Back
        </v-btn>

      </v-form>
    </v-col>
  </v-row>
</template>

<script>
import {register} from "@/api";

export default {
  name: "RegisterFormComponent",
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
    registerAccount() {
      register({
        password: this.password,
        username: this.username,
      })
          .then(response => {
            console.log(response);
            this.$store.commit('setUser', this.username, this.password);
          })
          .catch(error => {
            console.log(error);
          })
          .finally(() => {
            console.log('finally');
          });
    },
    goBack() {
      this.$router.go(-1);
    }
  },
}
</script>

<style scoped>

</style>
