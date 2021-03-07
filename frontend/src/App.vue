<template>
  <div id="app">

    <Navbar/>

    <Breadcrumb/>

    <div id="content-main">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'
import Breadcrumb from '@/components/Breadcrumb'

export default {
  components: { Navbar, Breadcrumb }
}
</script>

<style>
#app {
  padding: 0px;
  margin: 0px;
}

body {
  padding: 0px;
  margin: 0px;
}

#content-main {
  padding: 20px;
  padding-right: 40px;
  padding-left: 40px;
}

.padding-left {
  padding-left: 50px;
}

.padding-right {
  padding-right: 50px;
}

.padding-pagination {
  padding: 20px 20px;
}

#card-category {
  max-height: 200px;
}

.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
    display: table;
    content: "";
}

.clearfix:after {
    clear: both
}
</style>
