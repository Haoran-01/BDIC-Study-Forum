<template> <!--一块的宽度是根据外部容器宽度等分的--> <!--改一下一块的高度-->
  <div class="content">
    <grid-layout
      :layout="layout"
      :col-num="5"
      :row-height="130"
      :maxRows="6"
      :is-draggable="true"
      :is-resizable="false"
      :is-mirrored="false"
      :vertical-compact="false"
      :margin="[0, 0]"
      :use-css-transforms="true"
      preventCollision="false"
    >
    <grid-item v-for="item in layout"
       :x="item.x"
       :y="item.y"
       :w="item.w"
       :h="item.h"
       :i="item.i"
       :key="item.i"
       :maxW="1"
    >
      <course-card class="courseCard"></course-card> <!--把你的标签写这里-->
      <div class="remove" @click="removeItem(item.i)">

      </div>
    </grid-item>
    </grid-layout>
  </div>
  <button class="addItem" @click="addItem">Add a course</button>
</template>

<script>
import {GridLayout, GridItem} from 'vue3-grid-layout'
import courseCard from "@/components/courseScheduleComponents/courseCard";
// import axios from "axios";

export default {
  name: "CourseBoard",
  components:{GridLayout, GridItem, courseCard},
  data(){
    return{
      layout: [

      ]
    }
  },
  mounted() {
    // this.$gridlayout.load();
    this.index = this.layout.length;
  },
  methods: {
    addItem: function () {
      // Add a new item. It must have a unique key!
      this.layout.push({
        x: -1,
        y: -1, // puts it at the bottom
        w: 1,
        h: 1,
        i: this.index,
      });
      // Increment the counter to ensure key is always unique.
      this.index++;

      console.log(this.layout);
    },
    removeItem: function (val) {
      const index = this.layout.map(item => item.i).indexOf(val);
      this.layout.splice(index, 1);

      console.log(this.layout);
    },
/*    moveEvent(){
      axios.post('', {
        x:
      })
    }*/
  }
}
</script>

<style scoped>
.content{
  height: 100%;
  width: 100%;
}
.courseCard:hover + .remove{
  transition: .2s ease-out;
  opacity: 1;
}
.remove{
  transition: .2s ease-in;
  opacity: 0;
  background-image: url("../../../../../templates/dist/images/cancel.png");
  width: 20px;
  height: 20px;
  background-color: #FFFFFF;
  position: relative;
  right: 20px;
  top: 15px;
  background-repeat: no-repeat;
  background-size: contain;
  cursor: pointer;
}
.remove:hover{
  transition: .2s ease-out;
  opacity: 1;
}
.vue-grid-item{
  /*一块课程的样式写这里*/
  display: flex;
}
.vue-grid-layout{
  /*  整个课程表样式写这里*/
  /*  更多样式看这里：https://github.com/jbaysolutions/vue-grid-layout/blob/master/website/docs/.vuepress/components/ExampleStylingPlaceholder.vue*/
}
.addItem{
  transition: .2s ease-in;
  position: relative;
  bottom: 875px;
  left: 455px;
  width: 150px;
  height: 30px;
  font-family: "Noto Sans", sans-serif;
  font-weight: bold;
  font-size: 18px;
  background-color: #00B8FF;
  color: #FFFFFF;
  border: none;
  border-radius: 100px;
  outline: none;
  cursor: pointer;
}
.addItem:hover{
  transition: .2s ease-out;
  box-shadow: 0 0 0 3px #8ab5ff;
}
</style>
<style>
.content .vue-grid-item.vue-grid-placeholder {
  background: #8ab5ff !important;
  transition: .5s;
  border-radius: 10px;
}
</style>
