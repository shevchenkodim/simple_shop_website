import Vue from 'vue'
import Vuex from 'vuex'
import products from './products/index'
import categories from './categories/index'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    products,
    categories
  }
})
