<template>
  <el-card :body-style="{ padding: '0px'}">
    <img :src="category.image"
         class="image"
         height="275"
         width="auto"
    >
    <div class="block-title-categories">
      <span>
        <h3 type="flex"
            justify="space-between"
            align="middle"
        >
          <router-link :to="{path: `/${category.code_name}`}"
                       style=" text-decoration: none;"
          >
            {{ category.name }}
            <i class="el-icon-view" style="padding-top: 2px;"></i>
          </router-link>
        </h3>
      </span>
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'CategoryCard',
  props: {
    category: Object
  }
}
</script>

<style scoped>
.block-title-categories {
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 3px
}
</style>
