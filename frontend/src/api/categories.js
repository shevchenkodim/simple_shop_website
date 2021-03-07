import { axiosGet } from '@/utils'

export default {
  getCategories () {
    return axiosGet('/api/v1/categories')
  },
  getCategory (categoryID) {
    return axiosGet(`/api/v1/categories/${categoryID}`)
  }
}
