<template>
  <div>
    <header-component></header-component>
    <register-form-component></register-form-component>
  </div>
</template>

<script>
import HeaderComponent from "@/views/component/HeaderComponent";
import RegisterFormComponent from "@/views/component/RegisterFormComponent";

export default {
  name: "RegisterComponent",
  components: {RegisterFormComponent, HeaderComponent},
}
</script>

<style scoped>

</style>
