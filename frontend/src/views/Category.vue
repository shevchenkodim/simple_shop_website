<template>
  <div class="about">

    <square v-if="isCategoryLoading" v-bind:loading=isCategoryLoading></square>

    <div v-if="!isCategoryLoading">
      <el-row>
        <el-col :span="6">
          <el-image class="image"
                    :src="getCategory.image"
                    style="height: 200px; width: auto;"
          >
          </el-image>
        </el-col>
        <el-col :span="18" class="padding-left padding-right">
          <h2>{{ getCategory.name }}</h2>
          <p>{{ getCategory.description }}</p>
        </el-col>
      </el-row>
    </div>

    <square v-if="isProductsLoading" v-bind:loading=isProductsLoading></square>

    <div v-if="!isProductsLoading">
      <el-row class="padding-pagination" type="flex" align="middle" justify="center">
        <Paginator :paginator="getProductsPaginator"
                   @doLoadPaginatorData="doLoadProductsPaginator"
        />
      </el-row>

      <el-row v-if="getAllProducts.length > 0">
        <el-col :span="6"
                class="padding-left padding-right"
                v-for="product in getAllProducts"
                :key="product.id"
        >
          <ProductCard :product="product"/>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import ProductCard from '@/components/ProductCard'
import Paginator from '@/components/Paginator'

export default {
  name: 'Category',
  props: ['category_code'],
  components: { ProductCard, Paginator },
  computed: {
    ...mapGetters('categories', ['getCategory', 'isCategoryLoading']),
    ...mapGetters('products', [
      'getAllProducts',
      'isProductsLoading',
      'getProductsPaginator'
    ])
  },
  methods: {
    doLoadProducts (page = 0) {
      this.$store.dispatch('products/fetchProducts', {
        category: this.$store.getters['categories/getCategory'].pk,
        limit: this.getProductsPaginator.limit,
        offset: page * this.getProductsPaginator.limit - this.getProductsPaginator.limit
      })
    },
    doLoadProductsPaginator (page) {
      this.$store.commit('products/updatePaginatorCurrent', page)
      this.$store.dispatch('products/cleanAllProducts')
      this.doLoadProducts(page)
    }
  },
  mounted () {
    this.$store.commit('products/updatePaginatorCurrent', 1)
    this.$store.dispatch('products/cleanAllProducts')
    this.$store.dispatch('categories/fetchCategory', this.category_code)
      .then(() => {
        this.doLoadProducts()
      })
  }
}
</script>
