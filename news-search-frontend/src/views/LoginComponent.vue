<template>
  <div>
    <header-component></header-component>
    <login-form-component></login-form-component>
  </div>
</template>

<script>
import LoginFormComponent from "@/views/component/LoginFormComponent";
import HeaderComponent from "@/views/component/HeaderComponent";
export default {
  name: "LoginComponent",
  components: {
    LoginFormComponent,
    HeaderComponent
  },
}
</script>

<style scoped>

</style>
