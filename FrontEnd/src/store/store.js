import Vue from 'vue'
import Vuex from 'vuex'
import { Notification } from 'element-ui'
import { parseError } from './errorHandler'
import { LoginModule } from './modules/login'
import { OCRAS } from './modules/ocras'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state () {
    return {
      baseUrl: 'http://localhost:8888/img/'
    }
  },
  modules: {
    login: LoginModule,
    ocras: OCRAS
  }
})

export function notificationMessage (typeMessage, message) {
  if (typeMessage === 'success') {
    Notification.success({ message: message })
  } else if (typeMessage === 'error') {
    Notification.error({ message: message })
  } else {
    Notification.warning({ message: message })
  }
}

export function notifyError (err) {
  return parseError(err)
    .then(errorMessage =>
      notificationMessage('error', errorMessage))
}

export function sliceDataTable (state, page) {
  return (page) => {
    let max = 0
    if (state.tableData.length > page * 10) {
      max = page * 10
    } else {
      max = state.tableData.length
    }
    const min = page - 1
    return state.tableData.slice(min * 10, max)
  }
}
