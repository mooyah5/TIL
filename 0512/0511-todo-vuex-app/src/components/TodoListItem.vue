<template>
  <div>
    <!-- 특수 문법 deleteTodo 실행할 때, todo 같이 넘겨주셔야 함! -->
    <span 
      @click="updateTodoStatus(todo)"
      :class="{'is-completed': todo.isCompleted}"  
    >
      {{ todo.title }}
    </span>
    <button @click="deleteTodo(todo)">[x]</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    ...mapActions(['deleteTodo', 'updateTodoStatus']),
    prevUpdateTodo() {
      this.$store.dispatch('deleteTodo', this.todo)
    },
  }
}
</script>

<style scoped>
.is-completed {
  text-decoration: line-through;
}

div {
  border: 2px solid black;
  margin: 2px;
  padding: 2px;
}

span {
  cursor: pointer;
}
</style>
