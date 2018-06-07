<template>
<div>
  <products-table></products-table>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import ProductsTable from './ProductCards' // './ProductsTable'

export default {
  name: 'Products',
  props: {
  },
  data () {
    return {
    }
  },
  created () {
    this.keepConnection()
    if (this.user[0] === null) {
      this.$root.$router.push({ path: '/login' })
    } else {
      this.getUserProducts(this.user[0].token)
    }
  },
  methods: {
    ...mapActions('products', ['getUserProducts']),
    ...mapActions('login', ['keepConnection'])
  },
  computed: {
    ...mapGetters('login', ['user'])
  },
  components: {
    ProductsTable: ProductsTable
  }
}
</script>

<style scoped>
</style>
