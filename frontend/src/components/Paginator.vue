<template>
  <div class="el-pagination is-background">
    <button type="button"
            :disabled="!paginator.previous"
            class="btn-prev"
            @click="doLoadPage(paginator.current - 1)"
    >
      <i class="el-icon el-icon-arrow-left"></i>
    </button>

    <ul class="el-pager">
      <li v-for="item in Math.ceil(paginator.count / paginator.limit)"
          :key="item"
          class="number"
          :class="{'active': item === paginator.current}"
          v-show="paginator.current - 3 <= item <= paginator.current + 3"
          @click="doLoadPage(item)"
      >
        {{ item }}
      </li>
      <span v-if="Math.ceil(paginator.count / paginator.limit) <= 0">
        Товарів немає
      </span>
    </ul>

    <button type="button"
            class="btn-next"
            :disabled="!paginator.next"
            @click="doLoadPage(paginator.current + 1)"
    >
      <i class="el-icon el-icon-arrow-right"></i>
    </button>
  </div>
</template>

<script>
export default {
  name: 'Paginator',
  props: {
    paginator: Object
  },
  methods: {
    doLoadPage (page) {
      this.$emit('doLoadPaginatorData', page)
    }
  }
}
</script>

<style scoped>

</style>
