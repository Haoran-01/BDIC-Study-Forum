<template>
<div class="navigatorMain">
  <router-link class="logo" to="/"></router-link>
  <div class="navOptions" id="navOptions">
    <nav>
      <div class="navItem">
        <router-link class="navLink" id="home" to="/" Style="cursor: pointer;"> Home </router-link>
        <div class="navLinkDecoration"></div>
      </div>
      <div class="navItem">
        <router-link class="navLink" id="forum" to="/forum" Style="cursor: pointer;">Forum</router-link>
        <div class="navLinkDecoration"></div>
      </div>
      <div class="navItem">
        <router-link class="navLink" id="courseSchedule" :to="{name:'courseSchedule',params:{email:this.userEmail}}" Style="cursor:pointer;">Course</router-link>
        <div class="navLinkDecoration"></div>
      </div>
    </nav>
  </div>
  <div class="searchArea">
    <input type="text" class="searchInput" @keyup.enter="search" v-model="searchText">
    <div class="searchIcon"></div>
  </div>
  <button class="userMenuButton" id="userMenuButton" v-if="userLogined" @click="handleUserMenu" @blur="deleteUserMenu"></button>
  <button class="loginButton" id="loginButton" v-else @click="jumpToLogin">
    <span class="loginText">Login</span>
  </button>
  <transition>
      <NavUserMenu class="userMenu" v-if = "userMenuVisibility"></NavUserMenu>
  </transition>


</div>
  <div class="mainView">
    <router-view/>
  </div>
</template>

<!--<script setup>
import {onMounted, onUnmounted} from "vue";
onMounted(() => {
  window.addEventListener('scroll', this.changeOptionsVisibility, true)
})
onUnmounted(()=>{
    window.removeEventListener('scroll', this.changeOptionsVisibility, true)
})
</script>-->

<script>
/*import {onMounted, onUnmounted} from "vue";
onMounted(() => {
  window.addEventListener('scroll', this.changeOptionsVisibility, true)
})
onUnmounted(()=>{
  window.removeEventListener('scroll', this.changeOptionsVisibility, true)
})*/
import NavUserMenu from "@/components/generalComponents/NavUserMenu";
import axios from "axios";
export default {
    name: "NavigatorBar",
  components: {NavUserMenu},
  data() {
    return {
      userMenuVisibility: false,
      userLogined: false,
      userEmail: this.$store.state.userEmail,
      searchText:''
    }
  },
  methods: {
    changeOptionsVisibility(){
      const nav = document.getElementById("navOptions")
      if (this.$store.state.mainFunctionsVisibility === false){
        nav.style.opacity = "1";
        nav.style.pointerEvents = "auto";
      }else {
        nav.style.opacity = "0";
        nav.style.pointerEvents = "none";
      }
    },

    handleUserMenu(){
        if (this.$data.userMenuVisibility === false){
          const button = document.getElementById("userMenuButton");
          button.focus();
        }
        this.$data.userMenuVisibility = !this.$data.userMenuVisibility;
    },

    deleteUserMenu(){
      this.$data.userMenuVisibility = false;
    },
    jumpToLogin(){
      window.location.assign(window.location.origin + '/user/login');
    },
    search(){
      axios.post('', {
        content: this.searchText
      })
      .then((response)=>{
        if (response.status === 200){
          // if (this.$route.path !== '/'){
          //
          // }
        }
      })
    }
  },
  watch:{
    $route(to,from){
      to.path;
      from.path;
      this.changeOptionsVisibility();
    }
  },
  created() {
    const vue = this;
    axios.get('http://127.0.0.1:4523/mock/831624/get_session')
    .then(function (response){
      let code = response.status;
      if (code === 200){
        vue.userLogined = true;
        let email = response.data['message'];
        vue.userEmail = email;
        vue.$store.commit("userLogin", email);
      }else if (code === 400){
        vue.userLogined = false;
      }
    })
  },
  mounted() {
    window.addEventListener('scroll', this.changeOptionsVisibility, true);
  },
  unmounted() {
    window.removeEventListener('scroll', this.changeOptionsVisibility, true)
  }
}
</script>

<style scoped>
.v-enter-from{
  opacity: 0;
}
.v-enter-active{
  transition: opacity 0.2s ease-out;
}
.v-enter-to{
  opacity: 1;
}
.v-leave-from{
  opacity: 1;
}
.v-leave-active{
  transition: opacity 0.2s ease-in;
}
.v-leave-to{
  opacity: 0;
}
.navigatorMain{
  z-index: 3;
  display: grid;
  grid-template-columns: 150px auto 1fr 400px 120px;
  grid-template-rows: 50px;

  width: 100vw;
  height: 50px;
  position: fixed;
  background-color: #FFFFFF;
  box-shadow: 0 0 3px #727272;
}

.logo {
  background-image: url("../../../../../templates/dist/images/logo_full.png");
  grid-area: 1 / 1 / 2 / 2;
  background-size: contain;
  background-repeat: no-repeat;
  margin-top: 5px;
  margin-bottom: 5px;
  margin-left: 10px;
}

.navOptions{
  grid-area: 1 / 2 / 2 / 3;
  opacity: 0;
  align-items: center;
  display: flex;
  transition: 0.3s;
  pointer-events: none;
}

nav {
  display: grid;
  grid-template-rows: 100%;
  grid-template-columns: repeat(3, 100px);
  padding: 0;
  margin: 0;
  text-align: center;
  align-items: center;
  flex-basis: auto;
  font-family: "Noto Sans", sans-serif;
}
nav a:link, a:visited{
  width: 100px;
  color: #000000;
  text-decoration:none;
}
.navItem{
  position: relative;
}
.navLinkDecoration{
  transition: .3s ease-in;
  width: 0;
  height: 3px;
  position: absolute;
  left: 25px;
  background-color: #00B8FF;
}
.navLink:hover+.navLinkDecoration{
  transition: .3s ease-out;
  width: 50px;
}
.searchArea{
  grid-area: 1 / 4 / 2 / 5;
  width: 380px;
  height: 40px;
  align-self: center;
}
.searchIcon{
  transition: 0.3s;
  width: 30px;
  height: 30px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  background-image: url("../../../../../templates/dist/images/search.png");
  position: relative;
  left: 13px;
  top: -33px;
}
.searchInput:focus+.searchIcon{
  transition: 0.3s;
  background-image: url("../../../../../templates/dist/images/search_active.png");
}
.searchInput{
  transition: .3s;
  width: calc(100% - 40px);
  height: 38px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 100px;
  padding: 0 0 0 40px;
  outline: none;
}
.searchInput:hover{
  transition: .3s;
  box-shadow: 0 0 3px #8ab5ff;
  outline: none;
}
.searchInput:focus{
  border: 1px solid #00B8FF;
}
.loginButton{
  transition: 0.2s;
  z-index: 5;
  background-color: #00B8FF;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 40px;
  width: 80px;
  margin-top: 5px;
  margin-bottom: 5px;
  margin-right: 20px;
  grid-area: 1 / 5 / 2 / 6;
  border: none;
  border-radius: 4px;
  align-self: center;
}

.loginButton:hover{
  transition: 0.2s;
  box-shadow: 0 0 4px #727272;
}

.loginText{
  font-family: "Noto Sans", sans-serif;
  font-size: 16px;
  font-weight: bold;
  color: white;
}

.userMenuButton:hover{
  transition: 0.2s;
  box-shadow: 0 0 4px #727272;
}

.userMenuButton{
  transition: 0.2s;
  z-index: 10;
  background-image: url("../../../../../templates/dist/images/user_menu_temp.png");
  background-size: contain;
  background-repeat: no-repeat;
  height: 40px;
  width: 80px;
  margin-top: 5px;
  margin-bottom: 5px;
  margin-right: 20px;
  grid-area: 1 / 5 / 2 / 6;
  border: none;
  border-radius: 4px;
  align-self: center;
}

.userMenu{
  position: fixed;
  top: 55px;
  left: calc(100vw - 160px - 20px);
}

.mainView{
  padding-top: 50px;
}
</style>