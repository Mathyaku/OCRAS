<template>
  <div id="app">
    <el-container class="loginBody" style="height: 100vh;" v-if="$route.name !== 'Login'">
      <el-header>
        <app-navigation-bar></app-navigation-bar>
      </el-header>
      <el-main>
        <router-view/>
      </el-main>
    </el-container>
    <div v-else>
      <router-view/>
    </div>
  </div>
</template>

<script>
import NavigationBar from './common/appHeader/NavigationBar'

export default {
  name: 'App',
  computed: {
  },
  methods: {
  },
  components: {
    appNavigationBar: NavigationBar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* color: #2c3e50; */
}

.loginBody {
		background: linear-gradient(to left, #8e8e8e, #8e8e8e);
    font-family: "Roboto", sans-serif;
    -webkit-font-smoothing: antialiased
}

html, body {
    left:0;
    right:0;
		margin: auto;
}

.el-header {
  padding: 0 0 0 0 !important;
}

</style>
