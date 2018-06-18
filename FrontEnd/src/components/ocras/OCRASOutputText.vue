<template>
  <div>
    <el-row>
      <el-input
        type="textarea"
        :autosize="{ minRows: 15, maxRows: 15}"
        placeholder="Texto extraído"
        disabled
        v-model="extractedData.result">
      </el-input>
    </el-row>
    <!-- <el-row>
      <el-input
        type="textarea"
        :autosize="{ minRows: 2, maxRows: 2}"
        placeholder="Sugestão de correção"
        v-model="correctText">
      </el-input>
    </el-row> -->
    <el-row style="margin-top: 192px;">
      <el-button type="primary" @click="generatePDF" >Exportar Resultado</el-button>
    </el-row>
  </div>
</template>
<script>

import jsPDF from 'jspdf'
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      outputText: '',
      correctText: ''
    }
  },
  computed: {
    ...mapGetters('ocras', ['extractedData'])
  },
  methods: {
    generatePDF () {
      // eslint-disable-next-line
      var doc = new jsPDF('p', 'mm', [297, 235]);
      debugger
      doc.text(this.extractedData.result, 10, 10)
      doc.save('Relatório.pdf')
    }
  }
}
</script>

<style>
.el-switch__label {
  color: white;
}
</style>
