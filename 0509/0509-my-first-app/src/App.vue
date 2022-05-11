<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 보여주기 (print) -->
    <!-- 카멜 케이스 -->
    <!-- <TheAbout my-message="parentData"/> -->
    <!-- 케밥 케이스 -->
    <the-about 
      :my-message="parentData" 
      @child-input-change="parentGetChange"
    ></the-about>
  </div>
</template>

<script>
// 1. 불러오기 (import)
import TheAbout from './components/TheAbout.vue'

export default {
  name: 'App',
  // 2. 등록하기 (register)
  components: {
    TheAbout,
  },
  data: function () {
    return {
      parentData: 'This is parent data to child component'
    }
  },
  methods: {
    parentGetChange: function (inputData) {
      console.log('Boss: 들리는군..', inputData)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
