import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import TaskView from '@/views/TaskView.vue'
import TaskDetailView from '@/views/TaskDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/task',
      name: 'task',
      component: TaskView
    },
    {
      path: '/task/:id',
      name: 'task-detail',
      component: TaskDetailView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
