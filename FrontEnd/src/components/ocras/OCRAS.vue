<template>
<div>
  <el-row :gutter="20">
    <el-col :span="8">
      <div class="grid-content bg-purple"></div>
      <OCRAS-input-image></OCRAS-input-image>
    </el-col>
    <el-col :span="8">
      <div class="grid-content bg-purple"></div>
      <OCRAS-output-text></OCRAS-output-text>
    </el-col>
    <el-col :span="8">
      <div class="grid-content bg-purple"></div>
      <OCRAS-references></OCRAS-references>
    </el-col>
  </el-row>
</div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import OCRASInputImage from '../ocras/OCRASInputImage'
import OCRASOutputText from '../ocras/OCRASOutputText'
import OCRASReferences from '../ocras/OCRASReferences'

export default {
  name: 'OCRAS',
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
    }
    console.log(this.user[0].token)
  },
  methods: {
    // ...mapActions('market', ['getMarketProducts']),
    ...mapActions('login', ['keepConnection'])
  },
  computed: {
    ...mapGetters('login', ['user'])
  },
  components: {
    OCRASInputImage: OCRASInputImage,
    OCRASOutputText: OCRASOutputText,
    OCRASReferences: OCRASReferences
  }
}
</script>

<style>
  .el-row {
    margin-bottom: 10px;
  }
</style>
