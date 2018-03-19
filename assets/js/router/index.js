import Vue from 'vue';
import Router from 'vue-router';

import store from '../store';

import HomePage from '../pages/HomePage.vue';
import LoginPage from '../pages/LoginPage.vue';
import AllPostsPage from '../pages/AllPostsPage.vue';
import ViewPostPage from '../pages/ViewPostPage.vue';
import CreatePostPage from '../pages/CreatePostPage.vue';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    },
    {
      path: '/posts',
      name: 'all-posts',
      component: AllPostsPage
    },
    {
      path: '/posts/create',
      name: 'create-post',
      component: CreatePostPage,
      meta: {
        requiresLogin: true
      }
    },
    {
      path: '/posts/:id',
      name: 'view-post',
      component: ViewPostPage
    }
  ]
});

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresLogin)) {

    if(store.state.loggedIn) {
      next()
    } else {
      next({ name: 'login' })
    }
  } else {
    next();
  }
});

export default router;
