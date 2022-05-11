<template>
  <div id="app">
    <h1>MY TODOS</h1>
    <h2>전체: {{ allTodosCount }}</h2>
    <h2>끝난거: {{ completedTodosCount }}</h2>
    <h2>남은거: {{ uncompletedTodosCount }}</h2>
    <todo-form></todo-form>
    <todo-list></todo-list>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList.vue'
import TodoForm from '@/components/TodoForm.vue'

import { mapGetters } from 'vuex'
// import { mapMutations } from 'vuex'

export default {
  name: 'App',
  components: {
    TodoList, TodoForm
  },
  computed: {
    ...mapGetters([
      'allTodosCount',
      'completedTodosCount',
      'uncompletedTodosCount',
    ])
  },
  // methods: {
  //   ...mapMutations(['LOAD_TODOS', ])
  // },
  // created() {
  //   this.LOAD_TODOS()
  // }
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
