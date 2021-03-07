import { axiosGet } from '@/utils'

export default {
  namespaced: true,
  state: {
    productsLoading: false,
    productsError: undefined,
    products: [],
    paginator: {
      limit: 2,
      current: 1,
      count: 0,
      next: null,
      previous: null
    }
  },
  getters: {
    // eslint-disable-next-line camelcase
    getAllProducts (state) {
      return state.products
    },
    isProductsLoading (state) {
      return state.productsLoading
    },
    getShortCategoryProducts: state => categoryId => {
      return state.products.filter(product => product.category_id === categoryId)
    },
    getProductsPaginator (state) {
      return {
        next: state.paginator.next,
        count: state.paginator.count,
        limit: state.paginator.limit,
        current: state.paginator.current,
        previous: state.paginator.previous
      }
    }
  },
  mutations: {
    updateProductsLoading (state, value = false) {
      state.productsLoading = value
    },
    updateProducts (state, data) {
      // eslint-disable-next-line no-unused-vars
      const products = data.results
      for (const product of products) {
        state.products.push(product)
      }
      state.paginator.count = data.count
      state.paginator.next = data.next
      state.paginator.previous = data.previous
    },
    updateProductsError (state, error) {
      state.productsError = error
    },
    cleanProducts (state) {
      state.products = []
    },
    updatePaginatorCurrent (state, current) {
      state.paginator.current = current
    }
  },
  actions: {
    async fetchProducts ({ commit }, { category = null, limit = 3, offset = 0 }) {
      commit('updateProductsLoading', true)
      await axiosGet(`/api/v1/products?${category ? `category_id=${category}&` : ''}limit=${limit}&offset=${offset}`)
        .then(({ data }) => {
          commit('updateProducts', data)
        })
        .catch(({ response }) => {
          commit('updateProductsError', response)
        })
        .finally(() => {
          commit('updateProductsLoading')
        })
    },
    cleanAllProducts ({ commit }) {
      commit('cleanProducts')
    }
  }
}
