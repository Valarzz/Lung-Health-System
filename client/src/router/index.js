import Vue from 'vue'
import Router from 'vue-router'
import main from '@/components/main'
import login from '@/components/login'
import register from '@/components/register'
import record from '@/components/record'
import history from '@/components/history'
import store from '@/store'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: main,
      meta: {
        title: 'Main',
        required: false,
      },
    },
    {
      path: '/login',
      name: 'login',
      component: login,
      meta: {
        title: 'Login',
        required: false,
      },
    },
    {
      path: '/register',
      name: 'register',
      component: register,
      meta: {
        title: 'Register',
        required: false,
      },
    },
    {
      path: '/record',
      name: 'record',
      component: record,
      meta: {
        title: 'Record',
        required: true,
      },
    },
    {
      path: '/history',
      name: 'history',
      component: history,
      meta: {
        title: 'History',
        required: true,
      },
    },

  ]
})

// 全局前置守卫，判断用户是否登陆，未登陆跳转至登陆页面
router.beforeEach((to, from, next) => {
  // 自动添加title
  if (to.meta.title) {
      document.title = to.meta.title;
  }
  // 路由中定义的是否需要登陆权限
  // 如果前往的页面需要登录
  if (to.meta.required) {
      // 如果用户已经登录，此时token存在store里
      if (store.state.token) {
          next();
      } else {
          // 如果用户刷新页面，store里的token消失，此时token在sessionStorage里也存了
          if (sessionStorage.getItem('token')) {
              store.state.token = sessionStorage.getItem('token');
              next();
          } else {
              // 跳转到登陆页面
              next({
                  path: '/login',
                  query: { redirect: to.fullpath }
              })
          }
      }
  } else {
      // 对不需要登录的页面先查看用户是否登录，解决登录用户刷新token消失的问题
      if (sessionStorage.getItem('token')) {
          store.state.token = sessionStorage.getItem('token');
          next();
      }else{
        next();
      }
  }
})
export default router;