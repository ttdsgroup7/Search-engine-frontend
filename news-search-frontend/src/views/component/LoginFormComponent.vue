<template>
  <v-row
      class="ma-7 pa-3"
      no-gutters>
    <v-col
        md="6"
        offset-md="3">
      <v-form
          ref="form"
          lazy-validation
      >
        <v-text-field
            v-model="name"
            :counter="10"
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
  }),

  methods: {
    toLogin() {
      console.log(this.name, this.password);
      let userPass = this.password;
      login({
        password: this.password,
        username: this.name,
      }).then((res) => {
        console.log(res);
        console.log(userPass);
        this.$store.commit('setUser', {
          username: this.name,
          password: userPass,
        });
        this.$router.push({path:'/search', query:{search_phase: 'world'}});
      });
    },
    register() {
      this.$router.push('/register');
    },

  },
}
</script>

<style scoped>

</style>
