<template>
  <div class="home">

    <square v-if="isCategoriesLoading" v-bind:loading=isCategoriesLoading></square>

    <div v-if="!isCategoriesLoading">
      <div v-for="(category, items) in getAllCategories"
           :key="category.code_name"
      >
        <hr v-if="items >= 1">
        <el-row style="height: 340px;">
          <el-col :span="5" id="card-category">
            <CategoryCard :category="category"/>
          </el-col>
          <el-col :span="19" class="padding-left">
            <el-row>
              <el-col :span="24" class="padding-left">
                <h3>Popular products in {{ category.name }}</h3>
              </el-col>
            </el-row>
            <el-row v-if="getShortCategoryProducts(category.pk).length > 0">
              <el-col :span="8"
                      class="padding-left padding-right"
                      v-for="product in getShortCategoryProducts(category.pk)"
                      :key="product.id"
              >
                <ProductCard :product="product"/>
              </el-col>
            </el-row>
            <el-row v-else type="flex" justify="center" align="middle">
              <h3>
                <span class="text-danger" style="color: #8cc5ff;">
                  This category has no products
                  <i class="el-icon-search"></i>
                </span>
              </h3>
            </el-row>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import CategoryCard from '@/components/CategoryCard'
import ProductCard from '@/components/ProductCard'

export default {
  name: 'Home',
  components: { CategoryCard, ProductCard },
  computed: {
    ...mapGetters('categories', ['getAllCategories', 'isCategoriesLoading']),
    ...mapGetters('products', ['isProductsLoading', 'getShortCategoryProducts'])
  },
  methods: {
    doLoadProducts () {
      this.$store.dispatch('products/cleanAllProducts')
      // eslint-disable-next-line no-unused-vars
      for (const category of this.getAllCategories) {
        // eslint-disable-next-line no-use-before-define
        this.$store.dispatch('products/fetchProducts', {
          category: category.pk,
          limit: 3,
          offset: 0
        })
      }
    }
  },
  mounted () {
    this.$store.dispatch('categories/fetchAllCategories')
      .then(() => {
        this.doLoadProducts()
      })
  }
}
</script>
