<template>
  <nav>
    <div class="container-fluid">
      <a class="navbar-brand" href="c@\App.vue">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    </div>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0 ">
        <li class="nav-item ">
          <router-link class="nav-link ms-2" :to="{ name: 'articles' }">Home</router-link>
        </li>

        <li class="nav-item" v-if="!isLoggedIn">
          <router-link class="nav-link ms-2" :to="{ name: 'login' }">Login</router-link>
        </li>
        <li class="nav-item" v-if="!isLoggedIn">
          <router-link class="nav-link ms-2" :to="{ name: 'signup' }">Signup</router-link>
        </li>

        <li class="nav-item" v-if="isLoggedIn">
          <router-link class="nav-link ms-2" :to="{ name: 'articleNew' }">New</router-link>
        </li>

        <li class="nav-item" v-if="isLoggedIn">
          <router-link class="nav-link ms-2" :to="{ name: 'profile', params: { username } }">
           <span id="username">{{ currentUser.username }}</span><span>'s page</span>
          </router-link>
        </li>
        <li class="nav-item" v-if="isLoggedIn" >
          <router-link class="nav-link ms-2" :to="{ name: 'logout' }">Logout</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style>
#username{
  color:rgb(78, 78, 0)
}
</style>
