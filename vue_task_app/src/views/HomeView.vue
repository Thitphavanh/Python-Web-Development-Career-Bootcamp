<script setup>
import { ref } from 'vue'

const myName = ref('Hery')
const bgColor = ref('text-bg-dark')
const textColor = ref('text-dark')
const favoriteFood = ref('')
const count = ref(0)
const favPlaceHolder = ref('Input your Favorite food here')
const foodList = ref([])

const increment = () => {
  count.value++
}

const decrement = () => {
  count.value--
}

const alertMyName = () => {
  alert('My name is ${myName.value}')
}

const submitForm = () => {
  foodList.value.push(favoriteFood.value)
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
    <br />
    <div class="row" v-if="count > 5">
      <div class="alert alert-danger">Your Count Number more than the limit!</div>
    </div>
    <hr />
    <div class="row text-center">
      <div class="offset-md-4 col-md-3">
        <h3>Food List</h3>
        <form @submit.prevent="submitForm">
          <input
            type="text"
            v-model="favoriteFood"
            class="form-control"
            :placeholder="favPlaceHolder"
          />
          <br />
          <button type="submit" class="btn btn-dark">Submit</button>
        </form>
        <hr />
        <url>
          <li v-for="(food, index) in foodList" :key="index">
            {{ food }}
          </li>
        </url>
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
