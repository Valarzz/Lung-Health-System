// api调用代码
// 进一步封装axios get和post方法，加入前处理和后处理
import axios from 'axios';
import Config from '../config/url.js';
import store from '../store';
import router from '../router';

axios.defaults.timeout = 1800000;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
axios.defaults.withCredentials = true;

// 用来拼接url
function buildApiUrl (url) {
    return `${Config.apiUrl}/${Config.apiPrefix}/${url}`;
}

// axios请求拦截器，在发送请求前进行相关处理
axios.interceptors.request.use((config) => {
    // 自动添加请求头token
    if (store.state.token) {
        config.headers.common['Authorization'] = 'JWT ' + store.state.token;
    }
    return config;
}, (error) => {
    return Promise.reject(error);
}
);

// axios响应拦截器，在收到响应时对响应进行相关处理
axios.interceptors.response.use((res) => {
    return res;
}, (error) => {
    if (error.response) {
        switch (error.response.status) {
            // 返回401错误状态码清空token
            case 401:
                // 通过commit方法修改state里存储的内容
                store.commit('del_token');
                sessionStorage.removeItem('token');
                router.replace({
                    path: '/login',
                    query: {redirect: router.currentRoute.fullPath}
                })
        }
    }
    return Promise.reject(error);
})

// 发送get请求
export function fetchGet (url, param) {
    let apiUrl = buildApiUrl(url);
    return new Promise((resolve, reject) => {
        axios.get(apiUrl, param)
            .then(response => {
                resolve(response)
            }, err => {
                reject(err)
            })
            .catch((error) => {
                reject(error)
            })
    })
}

// 发送post请求
export function fetchPost (url, params) {
    let apiUrl = buildApiUrl(url);
    return new Promise((resolve, reject) => {
        axios.post(apiUrl, params)
            .then(response => {
                resolve(response);
            }, err => {
                reject(err);
            })
            .catch((error) => {
                reject(error)
            })
    });
}

export default {
    fetchGet,
    fetchPost
}
