import Vue from 'vue'
import Vuex from 'vuex'
import { login} from "@/api";


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: '',
    isLogin: false,
    password: '',
    relatedNews: [],
  },
  mutations: {
    setUser(state, userInfo) {
      state.username = userInfo.username;
      state.password = userInfo.password;
      state.isLogin = true;
    },
    logout(state) {
      state.username = '';
      state.isLogin = false;
      localStorage.removeItem('user_id');
    },
    setRelatedNews(state, relatedNews) {
      state.relatedNews = relatedNews;
    },
  },
  actions: {
    getRelatedNews({ commit }) {
      // console.log('getRelatedNews');
      login({
        username: this.state.username,
        password: this.state.password,
      }).then(res => {
        // console.log(res);
        // console.log(res.data.data.newsarray);
        commit('setRelatedNews', res.data.data.newsarray);
      })
    }
  },
  modules: {
  }
})
