import sharedAxios from '../../common/sharedAxios'
// import { notifyError } from '../store'
import { Notification } from 'element-ui'

export const OCRAS = {
  namespaced: true,
  state () {
    return {
      extractedData: {result: '', time: null},
      references: []
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
      sharedAxios.get(rootState.baseUrl + 'textFromImage', image)
        .then(response => {
          commit('setExtractedData', response.data)
        })
        .catch(err => {
          Notification.error({ message: err.message })
        })
    },
    getReferencesFromText ({ commit, rootState }, textInfo) {
      sharedAxios.get(rootState.baseUrl + 'referencesFromText', textInfo)
        .then(response => {
          commit('setReferences', response.data)
        })
        .catch(err => {
          Notification.error({ message: err.message })
        })
    }
  }
}
