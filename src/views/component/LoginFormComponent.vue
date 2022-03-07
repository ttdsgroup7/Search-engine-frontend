<template>

  <v-row
      class="ma-7 pa-3"
      no-gutters>
    <v-col
        md="6"
        offset-md="3">
      <v-alert
          v-if="error"
          dense
          outlined
          type="error"
          dismissible
      >
        Wrong information please try again!
      </v-alert>

      <v-form
          ref="form"
          lazy-validation
      >
        <v-text-field
            v-model="name"
            label="Username"
            required
        ></v-text-field>

        <v-text-field
            v-model="password"
            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show2 ? 'text' : 'password'"
            name="input-10-2"
            label="Password"
            class="input-group--focused"
            @click:append="show2 = !show2"
            @keydown.enter.prevent="toLogin"
        ></v-text-field>

        <v-btn
            color="success"
            class="mr-4"
            @click="toLogin"

        >
          Login
        </v-btn>

        <v-btn
            color="error"
            class="mr-4"
            @click="register"
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
import {login} from "@/api";

export default {
  name: "LoginFormComponent",
  data: () => ({
    name: '',
    show2: false,
    password: '',
    error: false
  }),

  methods: {
    toLogin() {
      // console.log(this.name, this.password);
      let userPass = this.password;
      login({
        password: this.password,
        username: this.name,
      }).then((res) => {
        // console.log(res);
        // console.log(userPass);

        if (res.code === '200') {
          this.$store.commit('setUser', {
            username: this.name,
            password: userPass,
          });
          localStorage.setItem('user_id', res.data.data.userId);
          this.$router.push({path: '/search', query: {search_phase: 'world'}});
        } else {
          this.error = true;
        }
      }).catch(error => {
        console.log(error)
      });
    },
    register() {
      this.$router.push('/register');
    },
    goBack() {
      this.$router.go(-1);
    }
  },
}
</script>

<style scoped>

</style>
