<template>
    <el-menu role="menubar"
             :default-active="activeIndex2"
             class="el-menu--horizontal"
             mode="horizontal"
             background-color="#545c64"
             text-color="#fff"
             active-text-color="#ffd04b"
             style="padding-left: 40px; padding-right: 40px"
    >
      <el-menu-item>
        <router-link :to="{ path: '/' }" style="text-decoration: none;">
          Simple Shop
        </router-link>
      </el-menu-item>
      <el-menu-item index="1">
        Home
      </el-menu-item>
    </el-menu>
</template>

<script>
export default {
  name: 'Navbar',
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    }
  },
  methods: {}
}
</script>

<style scoped>

</style>
