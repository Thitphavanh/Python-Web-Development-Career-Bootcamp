<script setup>
import { ref } from 'vue'
import { useTaskStore } from '@/stores/task'
import TaskList from '@/components/TaskList.vue'

const store = useTaskStore()
const taskPlaceholder = ref('Add your Task here')
</script>

<template>
  <div class="offset-4 col-6">
    <form @submit.prevent="store.submitTask">
      <div class="form-group mb-3">
        <label for="task" class="form-label">Task</label>
        <input
          v-model="store.task.title"
          type="text"
          class="form-control"
          :placeholder="taskPlaceholder"
        />
      </div>
      <div class="form-group">
        <textarea v-model="store.task.description" rows="3" class="form-control"></textarea>
      </div>
      <button class="btn btn-dark mt-3 w-100">Submit</button>
    </form>
  </div>
  <TaskList />
</template>
<style scoped></style>
