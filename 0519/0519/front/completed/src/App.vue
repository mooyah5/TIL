<template>
  <div id="app" class="container">
    <nav-bar class="navbar navbar-expand-lg bg-light" ></nav-bar>
    <hr />
    <router-view></router-view>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar },
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>

<style>
* {
  font-family: 'Do Hyeon', sans-serif;
}
</style>
