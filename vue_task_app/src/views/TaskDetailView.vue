<script setup>
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const handlepreviouspage = () => {
  router.back()
}

const handleHomepage = () => {
  router.push({ name: 'home' })
}
</script>

<template>
  <div class="row">
    <h1 class="text-center">Hello Task Page</h1>
    <h2>Task ID: {{ route.params.id }}</h2>
    <div class="col-md-4 d-flex justify-content-between mt-5">
      <button @click="handlepreviouspage" class="btn btn-info">back</button>
      <button @click="handleHomepage" class="btn btn-danger">Go Home</button>
    </div>
  </div>
</template>
<style scoped></style>
