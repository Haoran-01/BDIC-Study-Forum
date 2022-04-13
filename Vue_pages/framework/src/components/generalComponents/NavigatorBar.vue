<template>
<div class="navigatorMain">
  <div class="logo"></div>
  <div class="navOptions" id="navOptions">
    <nav>
      <router-link class="home" to="/" Style="cursor: pointer;"> Home </router-link>
      <router-link class="forum" to="/forum" Style="cursor: pointer;">Forum</router-link>
    </nav>
  </div>
  <button class="userMenuButton" id="userMenuButton" @click="handleUserMenu" @blur="deleteUserMenu"></button>
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
export default {
    name: "NavigatorBar",
  components: {NavUserMenu},
  data() {
    return {
      userMenuVisibility: false
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
    }
  },
  watch:{
    $route(to,from){
      to.path;
      from.path;
      this.changeOptionsVisibility();
    }
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
  z-index: 1;
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
  background-image: url("../../../../../static/images/logo_full.png");
  grid-area: 1 / 1 / 2 / 2;
  background-size: contain;
  background-repeat: no-repeat;
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

.userMenuButton:hover{
  transition: 0.2s;
  box-shadow: 0 0 4px #727272;
}

.userMenuButton{
  transition: 0.2s;
  z-index: 10;
  background-image: url("../../../../../static/images/user_menu_temp.png");
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