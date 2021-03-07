<template>
  <el-card :body-style="{ padding: '0px' }">
    <img :src="product.image"
         class="image"
         height="170"
    >
    <div style="padding: 14px;">
      <el-row type="flex" class="row-bg" justify="space-between" align="middle">
        <span>{{ product.name }}</span>
        <el-button round
                   type="success"
                   icon="el-icon-check"
                   size="mini"
                   v-if="product.is_available"
        >
          Availability
        </el-button>
        <el-button v-else
                   round
                   type="danger"
                   icon="el-icon-close"
                   size="mini"
        >
          Availability
        </el-button>
      </el-row>
      <div class="bottom clearfix">
        <span>{{ product.description }}</span>
      </div>
      <el-row type="flex" class="row-bg" justify="space-between" align="middle">
        <span><b>{{ product.price }}$</b></span>
        <div>
          <el-button type="warning" icon="el-icon-star-off" size="mini" circle></el-button>
          <el-button type="brand" icon="el-icon-shopping-bag-1" size="mini" circle></el-button>
        </div>
      </el-row>
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'Product',
  props: {
    product: Object
  }
}
</script>

<style scoped>
</style>
