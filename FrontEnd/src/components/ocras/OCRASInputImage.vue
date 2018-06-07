<template>
  <div>
    <div style="height: 200px;">
      <el-row>
        <!-- action="https://jsonplaceholder.typicode.com/posts/" -->
        <!-- :http-request="handlePictureCardPreview" -->
        <el-upload
          action="https://jsonplaceholder.typicode.com/posts/"
          :auto-upload="false"
          ref="upload"
          list-type="picture-card"
          :on-preview="handlePictureCardPreview"
          :on-remove="handleRemove"
          :on-exceed="handleExceed"
          :limit="1"
          :file-list="fileList">
          <i class="el-icon-plus"></i>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible">
          <img width="100%" :src="dialogImageUrl" alt="">
        </el-dialog>
      </el-row>
      <!-- <el-row>
        <el-switch
          v-model="referenceSearch"
          active-text="Buscar por Referências">
        </el-switch>
      </el-row> -->
    </div>
    <el-row style="margin-top:300px">
      <el-button type="primary" @click="submitUpload">Extrair Texto</el-button>
    </el-row>
  </div>
</template>
<script>
export default {
  data () {
    return {
      dialogImageUrl: '',
      referenceSearch: false,
      dialogVisible: false
    }
  },
  methods: {
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePictureCardPreview (file, fileList) {
      this.dialogImageUrl = file.url
      this.dialogVisible = false
    },
    submitUpload () {
      this.$refs.upload.submit()
    },
    handleExceed (files, fileList) {
      console.log(fileList)
      this.$message.warning(`Selecione uma imagem por vez!`)
    }
  }
}
</script>

<style>
.el-switch__label {
  color: white;
}
</style>
