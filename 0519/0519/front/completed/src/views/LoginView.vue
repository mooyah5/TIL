<template>
  <div id="login">
    <h1 class="text-center m-5">LOGIN</h1>
    <account-error-list v-if="authError"></account-error-list>
      <form @submit.prevent="login(credentials)" class="container ">
        <div class="row g-3 align-items-center justify-content-center mb-3">
          <div class="col-auto">
            <label for="username" class="col-form-label">Username </label>
          </div>
          <div class="col-auto" >
            <input v-model="credentials.username" placeholder="input username" class="form-control" type="text" id="username" required />
          </div>
        </div>

        <div class="row g-3 align-items-center justify-content-center mb-3">
          <div class="col-auto">
            <label for="password" class="col-form-label">Password </label>
          </div>
          <div class="col-auto">
            <input v-model="credentials.password" placeholder="input password" class="form-control" type="password" id="password" required />
          </div>
        </div>
        <div class=" row align-items-center justify-content-center">
          <button class="btn btn-outline-warning">Login</button>
        </div>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style scoped>
h1 {
  font-family: 'Black Han Sans', sans-serif;
}
#login {
  font-family: 'Do Hyeon', sans-serif;
}
::placeholder {
  font-family: 'Poor Story', cursive;
  text-align: center
}
</style>