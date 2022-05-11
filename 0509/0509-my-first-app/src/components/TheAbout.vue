<template>
  <!-- template 안에는 반드시 하나의 Element만 있어야 한다..  -->

  <div>
    <h1>{{ myMessage }}</h1>
    <p>아하! div는 하나구나</p>
    <input 
      type="text"
      v-model="childInputData"
      @keyup.enter="childInputChange"
    >
  </div>

</template>

<script>
export default {
  name: 'TheAbout',
  props: {
    myMessage: String,
  },
  data: function () {
    return {
      childInputData: ''
    }
  },
  methods: {
    childInputChange: function () {
      console.log('Child!!', this.childInputData)
      // 부모 컴포넌트에게 1번인자 라는 이름의 이벤트를 발생 + 2번인자 데이터를 보냄
      this.$emit('child-input-change', this.childInputData)
    }
  },
}
</script>

<style>

</style>
