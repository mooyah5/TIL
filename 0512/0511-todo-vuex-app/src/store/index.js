import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {  // data
    todos: [],
  },
  getters: {  // computed
    // 현재 끝난 일의 개수
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === true
      }).length
    },
    uncompletedTodosCount(state) {
      return state.todos.filter(todo => {
        return !todo.isCompleted
      }).length
    },
    
  },
  mutations: {  // methods => change
    // LOAD_TODOS(state) {
    //   const todosString = localStorage.getItem('todos')
    //   state.todos = JSON.parse(todosString)
    // },
    CREATE_TODO(state, newTodo) {
      state.todos.push(newTodo)
    },
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      state.todos = state.todos.map(todo => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        } 
        return todo
      })
    }
  },
  actions: {  // methods => !change
    saveTodos({ state }) {
      const jsonData = JSON.stringify(state.todos)
      localStorage.setItem('todos', jsonData)
    },
    createTodo(context, newTodo) {
      // context => 맥가이버 칼
      context.commit('CREATE_TODO', newTodo)
      // context.dispatch('saveTodos')
    },
    deleteTodo({ commit }, todoItem) {
      if (confirm('진짜 삭제하실?')) {
        commit('DELETE_TODO', todoItem)
        // dispatch('saveTodos')
      }
    },
    updateTodoStatus({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
      // dispatch('saveTodos')
    }
  },
})
