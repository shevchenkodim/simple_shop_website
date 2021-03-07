import categories from '@/api/categories'

export default {
  namespaced: true,
  state: {
    categoriesLoading: false,
    categoriesError: undefined,
    categories: [],
    categoryLoading: false,
    categoryError: undefined,
    category: {}
  },
  getters: {
    getAllCategories (state) {
      return state.categories
    },
    isCategoriesLoading (state) {
      return state.categoriesLoading
    },
    getCategory (state) {
      return state.category
    },
    isCategoryLoading (state) {
      return state.categoryLoading
    }
  },
  mutations: {
    updateCategoriesLoading (state, value = false) {
      state.categoriesLoading = value
    },
    updateCategories (state, categories) {
      state.categories = categories
    },
    updateCategoriesError (state, error) {
      state.categoriesError = error
    },
    updateCategoryLoading (state, value = false) {
      state.categoryLoading = value
    },
    updateCategory (state, category) {
      state.category = category
    },
    updateCategoryError (state, error) {
      state.categoriesError = error
    }
  },
  actions: {
    async fetchAllCategories ({ commit }) {
      commit('updateCategoriesLoading', true)

      await categories.getCategories()
        .then(({ data }) => {
          commit('updateCategories', data)
        })
        .catch(({ response }) => {
          commit('updateCategoriesError', response.data.detail)
        })
        .finally(() => {
          commit('updateCategoriesLoading')
        })
    },
    async fetchCategory ({ commit }, categoryID) {
      commit('updateCategoryLoading', true)

      await categories.getCategory(categoryID)
        .then(({ data }) => {
          commit('updateCategory', data)
        })
        .catch(({ response }) => {
          commit('updateCategoryError', response.data.detail)
        })
        .finally(() => {
          commit('updateCategoryLoading')
        })
    }
  }
}
