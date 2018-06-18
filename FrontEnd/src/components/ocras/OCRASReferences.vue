<template>
  <div>
    <!-- v-model="activeNames" @change="handleChange" -->
    <div v-if="references !== undefined">
      <el-collapse >
          <el-collapse-item :title="reference.title" v-for="(reference, index) in references.result" v-if="index < 8" :key="reference.title">
            <div> <a style="font-weight: bold;">Autor:</a> {{reference.author}}</div>
            <div> <a style="font-weight: bold;">Descrição:</a> {{reference.description}}</div>
            <div> <a style="font-weight: bold;">Fonte:</a> {{reference.source}}</div>
            <a :href="reference.url"> {{reference.url}}</a>
          </el-collapse-item>
      </el-collapse>
      <el-row style="margin-top: 109px;">
        <el-button type="primary" @click="getReferences" >Buscar Referências</el-button>
      </el-row>
    </div>
    <div v-else style="font-weight: bold; color: white"> Referências não encontradas!
        <el-row style="margin-top: 502px;">
          <el-button type="primary" @click="getReferences" >Buscar Referências</el-button>
        </el-row>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  data () {
    return {
    }
  },
  computed: {
    ...mapGetters('ocras', ['extractedData', 'references'])
  },
  methods: {
    ...mapActions('ocras', ['getReferencesFromText']),
    getReferences () {
      this.getReferencesFromText({text: this.extractedData.result})
    }
  }
}
</script>

<style>
.el-switch__label {
  color: white;
}
</style>
