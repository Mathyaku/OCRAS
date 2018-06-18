<template>
  <div>
    <a id="downloadImg" :href="dialogImageUrl" style="visibility:hidden" download>oii</a>
    <div style="height: 200px;">
      <el-row>
        <el-upload
          action="http://localhost:8888/img/extractText"
          :auto-upload="false"
          ref="upload"
          list-type="picture-card"
          :on-preview="handlePictureCardPreview"
          :on-success="handleAvatarSuccess"
          :on-remove="handleRemove"
          :on-exceed="handleExceed"
          :limit="1">
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
import { mapActions } from 'vuex'
export default {

  data () {
    return {
      dialogImageUrl: '',
      referenceSearch: false,
      dialogVisible: false,
      fileData: {
        type: this.type,
        id: this.id
      }
    }
  },
  methods: {
    ...mapActions('ocras', ['getTextFromImage']),
    handleAvatarSuccess (res, file) {
      this.imageUrl = URL.createObjectURL(file.raw)
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePictureCardPreview (file, fileList) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    getText () {
      let imgName = this.dialogImageUrl.split('/').slice(-1).pop() + '.png'
      this.getTextFromImage({name: imgName})
    },
    download () {
      document.getElementById('downloadImg').click()
      setTimeout(this.getText, 1500)
    },
    submitUpload () {
      if (this.$refs.upload.uploadFiles.length > 0) {
        this.dialogImageUrl = this.$refs.upload.uploadFiles[0].url
        setTimeout(this.download, 500)
      } else {
        this.$message.warning(`Selecione uma imagem!`)
      }
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
