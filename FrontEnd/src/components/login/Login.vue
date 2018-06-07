<template>
<body class="loginBody">
	<form class="loginForm">
		<div class="container">
			<a style="cursor: default">
				<img src="../../assets/remuse-upload.png" alt="Auth" width="80%" >
        <br>
			</a>
			<div style="font-weight: bold; display: -webkit-box; margin-top: 10px;">Email</div>
			<el-input type="text" v-model="email" placeholder="email@domínio.com" auto-complete="off"></el-input>
			<div style="font-weight: bold; display: -webkit-box; margin-top: 8px;">Senha</div>
			<el-input type="password" v-model="password" auto-complete="off"></el-input>
		</div>
		<div style="margin-top: 20px; width: 100%;">
			<el-button @click="submitLogin" type="primary">LOGIN</el-button>
		</div>
	</form>
</body>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Login',
  props: {
  },
  data () {
    return {
      email: '',
      password: ''
    }
  },
  created () {
  },
  methods: {
    ...mapActions('login', ['login']),
    submitLogin () {
      this.login({email: this.email, password: this.password})
        .then(() => {
          if (this.user[0] !== null) {
            this.$root.$router.push({ path: '/' })
          }
        })
    }
  },
  computed: {
    ...mapGetters('login', ['user'])
  },
  components: {
  }
}
</script>

<style scoped>
.loginForm {
    position: relative;
    z-index: 1;
    background: #FFFFFF;
    max-width: 300px;
    margin: 5% auto 100px;
    padding: 45px;
    text-align: center;
    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}

.loginBody {
		/* background: linear-gradient(to left, #2f93f9, #409eff); */
    background: linear-gradient(to left, #8e8e8e, #737272);
    font-family: "Roboto", sans-serif;
    -webkit-font-smoothing: antialiased
}

html, body {
    top:0;
    bottom:0;
    left:0;
    right:0;
    position:fixed;
		margin: auto;
}

.el-button--primary {
		width: 100%;
    /* color: #fff;
    background-color: #ee5626;
    border-color: #ee5626; */
}
</style>
