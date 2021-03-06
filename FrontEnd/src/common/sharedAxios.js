
import axios from 'axios'
import { Loading } from 'element-ui'

let axiosInstance = axios.create({
  baseUrl: 'http://localhost:8888/img/',
  timeout: 100000,
  headers: {
    'Content-Type': 'application/json'
  }
})
let loading
axiosInstance.interceptors.request.use(function (config) {
  loading = Loading.service({
    lock: true,
    text: 'Carregando',
    spinner: 'el-icon-loading',
    background: 'rgba(0, 0, 0, 0.7)'
  })
  return config
}, function (error) {
  loading.close()
  return Promise.reject(error)
})

axiosInstance.interceptors.response.use(function (response) {
  loading.close()
  return response
}, function (error) {
  loading.close()
  return Promise.reject(error)
})

export default axiosInstance
