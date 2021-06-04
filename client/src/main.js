// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'

//引入websocket库
import VueSocketIO from 'vue-socket.io'
import socketIO from 'socket.io-client'

// 引入element-ui的js文件
import ElementUI from 'element-ui'
// 引入element-ui的css文件
import 'element-ui/lib/theme-chalk/index.css'

// 引入axios库
import axios from 'axios'

import './assets/css/iconfont.css'

Vue.use(new VueSocketIO({
  debug: true,
  connection: socketIO('http://127.0.0.1:5000/test', {
	  autoConnect:false
    })
}))

Vue.prototype.$axios = axios

Vue.use(ElementUI)
Vue.config.productionTip = false

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
