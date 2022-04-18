<template>
  <div class="home">
    <div class="headSpace"></div>
    <div class="homeFrame">
      <div class="mainFunctions" id="mainFunctions">
        <main-function-entrance></main-function-entrance>
      </div>
      <div class="main">
        <div class="postListFrame">
          <div class="postListLogic" v-for="(item, index) in postData" :key="index">
          <post-entrance v-bind="item"></post-entrance>
          </div>
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
import axios from "axios";

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
      cookieVisibility: true,
      postData:[
          {
            userName: 'Jerry',
            sectionName: 'Lecture Question',
            title: 'The problem about binary tree',
            introduction: 'What is the difference between a binary search tree and a binary tree?',
            commentNumber: 6,
            userImageURL: require('../../../../templates/dist/images/Jerry.jpg')
          },
          {
            userName: 'Jerry',
            sectionName: 'Lecture Question',
            title: 'About AVL tree',
            introduction: 'After inserting in the AVL tree, why will one restructuring (if necessary) be enough to rebalance the whole tree? While for deletion, we must continue checking for balance until the root of T is reached.',
            commentNumber: 4,
            userImageURL: require('../../../../templates/dist/images/Jerry.jpg')
          },
          // {
          //   userName: 'Jerry',
          //   sectionName: 'Lecture Question',
          //   title: 'Heap exercise',
          //   introduction: 'When restructuring a tree, what if the children of y have the same height, and either one can be x?',
          //   commentNumber: 4,
          //   userImageURL: require('../../../../static/images/Jerry.jpg')
          // },
          // {
          //   userName: 'Jerry',
          //   sectionName: 'Lecture Question',
          //   title: 'Movement of an external node in Splay Tree',
          //   introduction: 'In these slides, if I switch between the right(external) and left(8) child of node x(10), would it get a different result after Zig-Zig?',
          //   commentNumber: 3,
          //   userImageURL: require('../../../../static/images/Jerry.jpg')
          // },
          // {
          //   userName: 'Winfred',
          //   sectionName: 'Lecture Question',
          //   title: 'remove operation of binary tree',
          //   introduction: 'after we have removed 3, can we continue to remove 6 (the root), which will change the root of the tree to 2?',
          //   commentNumber: 3,
          //   userImageURL: require('../../../../static/images/winfred.jpg')
          //
          // },
          // {
          //   userName: 'Winfred',
          //   sectionName: 'Lost and Found',
          //   title: 'Black Watch',
          //   introduction: 'I lost a watch apple at the entry to the teaching building 4. If anyone finds it, please contact me. I will really appreciate it if you could help.',
          //   commentNumber: 2,
          //   userImageURL: require('../../../../static/images/winfred.jpg')
          // },
          // {
          //   userName: 'Grey',
          //   sectionName: 'Lost and Found',
          //   title: 'Black Watch',
          //   introduction: 'I lost a wallet with a student card (203721) in it. I will really appreciate it if you could help',
          //   commentNumber: 2,
          //   userImageURL: require('../../../../static/images/grey.jpg')
          // },
          // {
          //   userName: 'Grey',
          //   sectionName: 'Transaction',
          //   title: 'MacBook Pro',
          //   introduction: 'If you want to buy a second-hand MacBook Pro 2021 16 inches, please contact me.',
          //   commentNumber: 1,
          //   userImageURL: require('../../../../static/images/grey.jpg')
          // },
          // {
          //   userName: 'Grey',
          //   sectionName: 'Transaction',
          //   title: 'iPhone 8',
          //   introduction: 'Anyone who would like to buy a second-hand iPhone 8 could email me directly.',
          //   commentNumber: 1,
          //   userImageURL: require('../../../../static/images/grey.jpg')
          // },
          // {
          //   userName: 'Grey',
          //   sectionName: 'Transaction',
          //   title: 'Java Learning Material',
          //   introduction: 'If you want some java learning material, please contact me. I could sell them in a low price. Don’t hesitate!!!',
          //   commentNumber: 1,
          //   userImageURL: require('../../../../static/images/grey.jpg')
          // },
        ]
      }
    },
  methods:{
    removeCookieWindow(){
      this.$data.cookieVisibility = false;
    },
    checkMainFunctionsPosition() {
      const mainFunctions = document.getElementById("mainFunctions");
      if (mainFunctions.getBoundingClientRect().bottom > 0){
        this.$store.commit("changeMainFunctionsVisible");
      }else {
        this.$store.commit("changeMainFunctionsInvisible");
      }
    }
  },
  created() {
    axios.get('http://127.0.0.1:4523/mock/831624/index/get_post')
        .then((response) => {
          this.postData = response.data.data;
        })
        .catch(function (error) {
          console.log(error);
        })
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

.postListFrame{
  float: left;
  width: 682px;
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