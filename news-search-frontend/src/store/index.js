import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
   username: '',
  },
  mutations: {
    setUser(state, username) {
      state.username = username;
    },
  },
  actions: {

  },
  modules: {
  }
})
