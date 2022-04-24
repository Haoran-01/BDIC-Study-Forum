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
      <course-card></course-card> <!--把你的标签写这里-->
      <div class="remove" @click="removeItem(item.i)">

      </div>
    </grid-item>
    </grid-layout>
  </div>
  <button class="addItem" @click="addItem">Add an item dynamically</button>
</template>

<script>
import {GridLayout, GridItem} from 'vue3-grid-layout'
import courseCard from "@/components/courseScheduleComponents/courseCard";

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
    },
    removeItem: function (val) {
      const index = this.layout.map(item => item.i).indexOf(val);
      this.layout.splice(index, 1);
    },
  }
}
</script>

<style scoped>
.content{
  height: 100%;
  width: 100%;
}
.remove{
  width: 10px;
  height: 10px;
  background-color: #00B8FF;
  position: relative;
  right: 20px;
  top: 15px;
}
.vue-grid-item{
  /*一块课程的样式写这里*/
  display: flex;
}
.vue-grid-layout{
  /*  整个课程表样式写这里*/
  /*  更多样式看这里：https://github.com/jbaysolutions/vue-grid-layout/blob/master/website/docs/.vuepress/components/ExampleStylingPlaceholder.vue*/
}

.vue-grid-item.vue-grid-placeholder {
  background: green !important;
}
.addItem{
  position: relative;
  bottom: 875px;
  left: 455px;
}
</style>
