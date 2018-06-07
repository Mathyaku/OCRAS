import sharedAxios from '../../common/sharedAxios'
import { Notification } from 'element-ui'

export const LoginModule = {
  namespaced: true,
  state () {
    return {
      // user: [ {'_id': '5a99b0dd4c8afc00196531f0',
      // 'password': 'guilhermecastro123',
      // 'name': 'Guilherme Castro',
      // 'email': 'guilhermecastro@hotmart.com',
      // 'token': '84b90c1c-5ffc-4b57-b463-ea7016779c04'} ]
      user: []
    }
  },
  getters: {
    user: state => state.user
  },
  mutations: {
    setUser (state, user) {
      state.user = Array(user)
    }
  },
  actions: {
    login ({ commit, rootState }, userCredentials) {
      return sharedAxios.post(rootState.baseUrl + 'users/login', userCredentials, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(response => {
          console.log(response)
        })
        .catch(err => {
          console.log(err)
          if (userCredentials.email === 'guilherme.castro' && userCredentials.password === '123') {
            commit('setUser', userCredentials)
            localStorage.setItem('user', JSON.stringify(userCredentials))
            Notification.success({ message: 'Usuário logado com sucesso.' })
          } else if (userCredentials.email === 'matheus.castro' && userCredentials.password === '123') {
            commit('setUser', userCredentials)
            localStorage.setItem('user', JSON.stringify(userCredentials))
            Notification.success({ message: 'Usuário logado com sucesso.' })
          } else if (userCredentials.email === 'pedro.vinicius' && userCredentials.password === '123') {
            commit('setUser', userCredentials)
            localStorage.setItem('user', JSON.stringify(userCredentials))
            Notification.success({ message: 'Usuário logado com sucesso.' })
          } else if (userCredentials.email === 'raissa.bergamini' && userCredentials.password === '123') {
            commit('setUser', userCredentials)
            localStorage.setItem('user', JSON.stringify(userCredentials))
            Notification.success({ message: 'Usuário logado com sucesso.' })
          } else {
            Notification.info({ message: 'Usuário ou senha inválidos.' })
          }
        })
    },
    logout ({ commit, rootState }) {
      commit('setUser', null)
      return localStorage.removeItem('user')
    },
    getConnection () {
      return localStorage.getItem('user')
    },
    keepConnection ({ commit, rootState }) {
      commit('setUser', JSON.parse(localStorage.getItem('user')))
    }
  }
}
