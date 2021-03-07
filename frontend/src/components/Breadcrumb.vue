<template>
  <div id="breadcrumb">
    <el-container>
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/' }"><i class="el-icon-s-home"></i> Home</el-breadcrumb-item>
<!--        <el-breadcrumb-item><a href="/">category</a></el-breadcrumb-item>-->
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
