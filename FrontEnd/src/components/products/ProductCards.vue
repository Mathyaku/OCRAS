
<template>
  <div class="container">
    <el-row>
      <el-col :span="6" v-for="product in Products" :key="product._id">
        <el-card :body-style="{ padding: '0px' }">
          <div slot="header" style="padding: 0px 0px 0px 0px !important;">
            <img :src="product.thumb" class="image">
            <div>
              <span>{{product.title}}</span>
              <el-row class="time">
                <el-col class="time" :span="12">
                  <time>{{ product.lastModified | formatDate}}</time>
                </el-col>
                <el-col class="time" :span="12">
                  {{product.price.value}}
                  {{product.price.currency}}
                </el-col>
              </el-row>
              <el-row style="margin-bottom: -18px">
                <el-button type="text" @click="updateDescriptionDetail(product.description)" class="button">Descrição</el-button>
              </el-row>
            </div>
          </div>
          <div style="margin-top:5px;margin-bottom:5px">
            <el-button type="primary" @click="updateUserProdut(product)" v-if="product.owner === user[0]._id" plain icon="el-icon-edit"></el-button>
            <div v-if="product.owner !== user[0]._id">
              <el-button v-if="enableAffiliation(product)" @click="setProductAffiliation(product)" type="success" plain icon="el-icon-circle-plus-outline"></el-button>
              <el-button v-else @click="deleteProductAffiliation(product)" type="danger" plain icon="el-icon-remove-outline"></el-button>
            </div>
            <el-button type="danger" @click="deleteUserProduct(product)" v-if="product.owner === user[0]._id" plain icon="el-icon-delete"></el-button>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <description-modal></description-modal>
    <add-product-modal></add-product-modal>
    <update-product-modal></update-product-modal>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex'
import DescriptionModal from '../modal/DescriptionModal'
import AddProductModal from '../modal/AddProductModal'
import UpdateProductModal from '../modal/UpdateProductModal'

export default {
  name: 'ProductCards',
  props: {
  },
  data () {
    return {
      descriptionDialogVisible: false,
      description: ''
    }
  },
  created () {
  },
  computed: {
    ...mapGetters('login', ['user']),
    ...mapGetters('products', ['userProducts']),
    ...mapGetters('market', ['marketProducts']),
    Products () {
      if (this.$route.name === 'Market') {
        return this.marketProducts
      } else if (this.$route.name === 'Products') {
        return this.userProducts
      }
    }
  },
  methods: {
    ...mapActions('market', ['getMarketProducts', 'addAffiliation', 'removeAffiliation']),
    ...mapActions('products', ['getUserProducts', 'removeUserProduct']),
    ...mapMutations('modal', ['setDescriptionModalVisible', 'setDescriptionModalText',
      'setUpdateProductModalData', 'setUpdateProductModalVisible']),
    updateDescriptionDetail (productDescription) {
      this.setDescriptionModalText(productDescription)
      this.setDescriptionModalVisible(true)
    },
    enableAffiliation (product) {
      if (product.affiliates === undefined) {
        return true
      }
      if (product.affiliates.filter(c => c === this.user[0]._id).length > 0) {
        return false
      } else {
        return true
      }
    },
    setProductAffiliation (product) {
      this.addAffiliation({token: this.user[0].token, productId: product._id})
        .then(() => {
          if (this.$route.name === 'Market') {
            this.getMarketProducts(this.user[0].token)
          } else if (this.$route.name === 'Products') {
            this.getUserProducts(this.user[0].token)
          }
        })
    },
    deleteProductAffiliation (product) {
      this.removeAffiliation({token: this.user[0].token, productId: product._id})
        .then((vaue) => {
          if (this.$route.name === 'Market') {
            this.getMarketProducts(this.user[0].token)
          } else if (this.$route.name === 'Products') {
            this.getUserProducts(this.user[0].token)
          }
        })
    },
    deleteUserProduct (product) {
      this.$confirm('Você realmente deseja deletar o produto ' + product.title + '?', 'Informação', {
        confirmButtonText: 'Confirmar',
        cancelButtonText: 'Cancelar',
        type: 'info'
      }).then(() => {
        this.removeUserProduct({token: this.user[0].token, productId: product._id})
          .then(() => {
            this.getUserProducts(this.user[0].token)
          })
      })
    },
    updateUserProdut (product) {
      let data = {
        title: product.title,
        description: product.description,
        price: {
          currency: product.price.currency,
          value: product.price.value
        },
        thumb: product.thumb,
        affiliates: product.affiliates,
        _id: product._id
      }
      this.setUpdateProductModalData(data)
      this.setUpdateProductModalVisible(true)
    }
  },
  components: {
    DescriptionModal: DescriptionModal,
    AddProductModal: AddProductModal,
    UpdateProductModal: UpdateProductModal
  },
  filters: {
    formatDate (value) {
      let d = Date.parse(value)
      if (!isNaN(d)) {
        d = new Date(value)
        value = d.toLocaleString('pt-BR')
      } else {
        value = '-'
      }
      return value
    }
  }
}
</script>

<style scoped>
  .image {
    display: -webkit-inline-box;
    max-height:100px;
    width: auto;
    height: auto;
  }

  .time {
    font-size: 13px;
    color: #999;
    padding-top: 5px;
  }

  html, body {
    top:0;
    bottom:0;
    left:0;
    right:0;
    position:fixed;
		margin: auto;
  }

  .el-card {
    margin-left: 20px;
    margin-bottom: 20px;
  }
</style>
