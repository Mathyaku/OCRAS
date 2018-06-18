import sharedAxios from '../../common/sharedAxios'
// import { notifyError } from '../store'
import { Notification } from 'element-ui'

export const OCRAS = {
  namespaced: true,
  state () {
    return {
      extractedData: {},
      references: undefined
    }
  },
  getters: {
    extractedData: state => state.extractedData,
    references: state => state.references
  },
  mutations: {
    setExtractedData (state, imageData) {
      state.extractedData = imageData
    },
    setReferences (state, referenceList) {
      state.references = referenceList
    }
  },
  actions: {
    getTextFromImage ({ commit, rootState }, image) {
      sharedAxios.post(rootState.baseUrl + 'extractText', image, { headers: { 'content-Type': 'application/x-www-form-urlencoded' } })
        .then(response => {
          commit('setExtractedData', response.data)
          commit('setReferences', undefined)
        })
        .catch(err => {
          Notification.error({ message: err.message })
        })
    },
    getReferencesFromText ({ commit, rootState }, textInfo) {
      debugger
      sharedAxios.post(rootState.baseUrl + 'extractReferences', textInfo, { headers: { 'content-Type': 'application/x-www-form-urlencoded' } })
        .then(response => {
          console.log(response.data)
          commit('setReferences', response.data)
        })
        .catch(err => {
          Notification.error({ message: err.message })
        })
    }
  }
}
