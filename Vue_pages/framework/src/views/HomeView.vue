<template>
  <div class="home">
    <div class="headSpace"></div>
    <div class="homeFrame">
      <div class="mainFunctions" id="mainFunctions">
        <MainFunctionEntrance></MainFunctionEntrance>
      </div>
      <div class="main">
        <div class="postList">
          <PostEntrance></PostEntrance>
          <PostEntrance></PostEntrance>
          <PostEntrance></PostEntrance>
          <PostEntrance></PostEntrance>
          <PostEntrance></PostEntrance>
          <PostEntrance></PostEntrance>
          <PostEntrance></PostEntrance>
          <PostEntrance></PostEntrance>
        </div>
        <div class="sideBar">
          <TopSectionList></TopSectionList>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<script>
import TopSectionList from "@/components/HomePageComponents/TopSectionList";
import PostEntrance from "@/components/generalComponents/PostEntrance";
import MainFunctionEntrance from "@/components/HomePageComponents/MainFunctionEntrance";

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
  components: {TopSectionList, PostEntrance, MainFunctionEntrance},
  methods:{
    checkMainFunctionsPosition() {
      const mainFunctions = document.getElementById("mainFunctions");
      console.log(mainFunctions.getBoundingClientRect().bottom);
      if (mainFunctions.getBoundingClientRect().bottom > 0){
        console.log(">0")
        this.$store.commit("changeMainFunctionsInvisible");
      }else {
        console.log("<0")
        this.$store.commit("changeMainFunctionsVisible");
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

</style>