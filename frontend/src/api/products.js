import { axiosGet } from '@/utils'

export default {
  getProducts (category, limit, offset) {
    return axiosGet(`/api/v1/products?${category ? `category_id=${category}&` : ''}limit=${limit}&offset=${offset}`)
  }
}
