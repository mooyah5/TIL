<template>
  <div>
    <h1>user profile</h1>
    <p>
      당신의 id는 {{ user.userId }}
      당신의 이름은 {{ user.username }}
      전공은 {{ user.major }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'UserProfile',
  data: function () {
    return {
      user: this.$route.params,
    }
  }
}
</script>

<style>

</style>
