<template>
<div class="navigatorMain">
  <router-link class="logo" to="/"></router-link>
  <div class="navOptions" id="navOptions">
    <nav>
      <router-link class="home" to="/" Style="cursor: pointer;"> Home </router-link>
      <router-link class="forum" to="/forum" Style="cursor: pointer;">Forum</router-link>
      <router-link class="courseSchedule" to="/course_schedule" Style="cursor:pointer;">Course</router-link>
    </nav>
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
      userLogined: true
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
      axios.get('/get_session')
    .then(function (response){
      let code = response.data['code'];
      if (code === 200){
        this.data().userLogined = true;
        let email = response.data['message'];
        this.$store.commit("userLogin", email);
      }else if (code === 400){
        this.data().userLogined = false;
      }
    })
  },
  mounted() {
    window.addEventListener('scroll', this.changeOptionsVisibility, true)
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
  grid-template-columns: 200px 270px 1fr 100px;
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
  display: flex;
  grid-template-rows: 100%;
  grid-template-columns: repeat(2, 100px);
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
  grid-area: 1 / 4 / 2 / 5;
  border: none;
  border-radius: 4px;
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
  grid-area: 1 / 4 / 2 / 5;
  border: none;
  border-radius: 4px;
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