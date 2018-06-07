<template>
    <div>
      <el-menu mode="horizontal" :default-active="getRoutPath" :router="true"
      background-color="#0273d4"
      active-text-color="#8e8e8e">
        <el-menu-item :index="activeIndex" style="border-bottom-color: transparent; cursor: default;
          width: 150px;">
          <a style="cursor: default">
            <img src="../../assets/hands-write.png" alt="icon" width="100%" height="50px" >
          </a>
        </el-menu-item>
        <el-menu-item index='/' @click="activeIndex = getRoutPath" class="navtext">
          Inicio
        </el-menu-item>
        <!-- <el-menu-item index='/products' @click="activeIndex = getRoutPath" class="navtext">
          Meus Produtos
        </el-menu-item> -->
        <!-- <div v-if="$route.name === 'Products'">
          <el-button type="primary" v-if="$route.name === 'Products'"
            @click="openAddForm" class="navtext" style="margin-top: 10px; margin-left:40%">Adicionar Produto</el-button>
          <el-button type="primary"
            @click="logoutAndRedirect" class="navtext" style="margin-top: 10px; margin-left:10%">Logout</el-button>
        </div> -->
        <div>
          <el-dropdown @command="logoutAndRedirect" style="margin-top: 10px; float: right">
              <el-button type="info" style="border-radius: 50%;padding: 12px;" icon="el-icon-setting"></el-button>
              <i class="el-icon-arrow-down el-icon--right"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="logout">Logout</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-menu>
    </div>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'

export default {
  data () {
    return {
      activeIndex: '/'
    }
  },
  computed: {
    getRoutPath () {
      return this.$route.path
    }
  },
  methods: {
    ...mapActions('login', ['logout']),
    ...mapMutations('modal', ['setAddProductModalVisible']),
    logoutAndRedirect () {
      this.logout().then(() => {
        this.$confirm('Você deseja efetuar o logout?', 'Informação', {
          confirmButtonText: 'Confirmar',
          cancelButtonText: 'Cancelar',
          type: 'info'
        }).then(() => {
          this.$root.$router.push({ path: '/login' })
        })
      })
    },
    openAddForm () {
      this.setAddProductModalVisible(true)
    }
  }
}
</script>

<style scoped>
  .navtext {
    font-weight:bold !important;
    color:white !important;
  }
</style>
