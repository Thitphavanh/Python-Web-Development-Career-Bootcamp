import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useTaskStore = defineStore('task', () => {
  const apiServer = 'http://157.245.152.237:8009/api/task/'

  const tasks = ref([])

  axios.get(apiServer).then((response) => {
    tasks.value = response.data
  })

  const task = ref({
    title: '',
    description: ''
  })

  const submitTask = () => {
    axios
      .post(apiServer, task.value)
      .then((response) => {
        tasks.value.push(response.data)
      })
      .catch((err) => {
        console.log(err)
      })

    task.value.title = ''
    task.value.description = ''
  }
  const deleteTask = (id) => {
    axios.delete(apiServer + id).then(() => {
      tasks.value = tasks.value.filter((task) => task.id !== id)
    })
  }
  const tasksReverse = computed(() => {
    return tasks.value.slice().reverse()
  })
  return { tasks, task, submitTask, tasksReverse, deleteTask }
})
