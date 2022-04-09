<template>
  <div class="home">
    <div class="headSpace"></div>
    <div class="homeFrame">
      <div class="mainFunctions" id="mainFunctions">
        <main-function-entrance></main-function-entrance>
      </div>
      <div class="main">
        <div class="postList">
          <post-entrance></post-entrance>
          <post-entrance></post-entrance>
        </div>
        <div class="sideBar">
          <top-section-list></top-section-list>
        </div>
      </div>
    </div>
    <transition>
    <cookie-window  class="cookies" v-if="cookieVisibility" @remove-cookie-window="removeCookieWindow"></cookie-window>
    </transition>
  </div>
</template>

<script>
import CookieWindow from "@/components/HomePageComponents/CookieWindow";
import MainFunctionEntrance from "@/components/HomePageComponents/MainFunctionEntrance";
import PostEntrance from "@/components/generalComponents/PostEntrance";
import TopSectionList from "@/components/HomePageComponents/TopSectionList";

/*import {onMounted, onUnmounted} from "vue";
onMounted(() =>{
  console.log("yes")
  window.addEventListener('scroll', this.checkMainFunctionsPosition, true)
});

onUnmounted(() =>{
  console.log("no")
  window.removeEventListener('scroll', this.checkMainFunctionsPosition, true)
});*/

export default {
  components: {TopSectionList, PostEntrance, MainFunctionEntrance, CookieWindow},
  data() {
    return {
      cookieVisibility: true
    }
  },
  methods:{
    removeCookieWindow(){
      this.$data.cookieVisibility = false;
    },
    checkMainFunctionsPosition() {
      const mainFunctions = document.getElementById("mainFunctions");
      console.log(mainFunctions.getBoundingClientRect().bottom);
      if (mainFunctions.getBoundingClientRect().bottom > 0){
        console.log(">0")
        this.$store.commit("changeMainFunctionsVisible");
      }else {
        console.log("<0")
        this.$store.commit("changeMainFunctionsInvisible");
      }
    }
  },
  mounted() {
    window.addEventListener('scroll', this.checkMainFunctionsPosition, true)
  },
  unmounted() {
    window.removeEventListener('scroll', this.checkMainFunctionsPosition, true)
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
.headSpace{
  height: 30px;
}
.homeFrame{
  display: grid;
  grid-template-columns: 1fr 1000px 1fr;
  grid-template-rows: 144px 1fr;
  grid-column-gap: 0px;
  grid-row-gap: 30px;
}

.mainFunctions{
  grid-area: 1 / 2 / 2 / 3;
}

.main{
  grid-area: 2 / 2 / 3 / 3;
}

.postList{
  float: left;
  width: 694px;
}

.sideBar{
  float: right;
  margin-left: 8px;
}

.cookies{
  position: fixed;
  top: calc(100vh - 90px);
  left: calc(50vw - 500px);
}

</style>