<script setup>
import { ref } from 'vue'

const myName = ref('Hery')
const bgColor = ref('text-bg-danger')
const textColor = ref('text-danger')
const favoriteFood = ref('')
const count = ref(0)
const favPlaceHolder = ref('Input your Favorite food here')
const increment = () => {
  count.value++
}

const decrement = () => {
  count.value--
}

const alertMyName = () => {
  alert('My name is ${myName.value}')
}
</script>

<template>
  <main>
    <h1 :class="textColor" @click="alertMyName">Hello {{ myName }}</h1>
    <h2 :class="bgColor">Hello world</h2>
    <hr />
    <div class="row">
      <div class="offset-md-4 col-md-6">
        <button @click="increment" class="btn btn-primary">+</button>
        <span class="h3">{{ count }}</span>
        <button @click="decrement" class="btn btn-danger">-</button>
      </div>
    </div>
    <hr />
    <div class="row text-center">
      <div class="offset-md-4 col-md-3">
        <h3>V-Model</h3>
        <input
          type="text"
          v-model="favoriteFood"
          class="form-control"
          :placeholder="favPlaceHolder"
        />
        <span class="fav-food">
          {{ favoriteFood }}
        </span>
      </div>
    </div>
  </main>
</template>

<style>
button {
  width: 100px;
}
span {
  margin: 0px 10px;
  padding: 10px;
}
h1 {
  cursor: pointer;
}
</style>
