<template>
    <el-menu role="menubar"
             :default-active="'1'"
             class="el-menu--horizontal"
             mode="horizontal"
             background-color="#545c64"
             text-color="#fff"
             active-text-color="#ffd04b"
             style="padding-left: 40px; padding-right: 40px"
    >
      <el-menu-item index="0" style="color: #f0f0f0; border-bottom-color: rgb(84, 92, 100);">
        <span class="text-info">
          <b>Simple Shop</b>
        </span>
      </el-menu-item>
      <el-menu-item index="1">
        <router-link :to="{ path: '/' }"
                     style="text-decoration: none;"
                     text-color="#303133"
        >
          Home
        </router-link>
      </el-menu-item>
    </el-menu>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>

</style>
