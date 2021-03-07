<template>
  <div id="breadcrumb">
    <el-container>
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/' }">
          <i class="el-icon-s-home"></i>
          Home
        </el-breadcrumb-item>

        <el-breadcrumb-item v-if="this.$route.name === 'Category'"
                            :to="{ path: `/${this.$route.params.category_code}` }"
        >
          {{ this.$route.params.category_code }}
        </el-breadcrumb-item>
      </el-breadcrumb>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'Breadcrumb'
}
</script>

<style scoped>
  #breadcrumb {
    padding: 20px 40px;
  }
</style>
