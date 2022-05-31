import { createRouter, createWebHistory } from 'vue-router'
import ArticlesView from '../views/ArticlesView.vue';
import CategoriesView from '../views/CategoriesView.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ArticlesView
    },
    {
      path: '/categories',
      name: 'categories',
      component: CategoriesView
    },

  ]
})

export default router
