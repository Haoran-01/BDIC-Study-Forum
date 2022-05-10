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
      :preventCollision="true"
    >

    <grid-item v-for="item in layout"
       :x="item.x"
       :y="item.y"
       :w="item.w"
       :h="item.h"
       :i="item.i"
       :key="item.i"
       :maxW="1"
       @moved="moveEvent"
    >
      <course-card class="courseCard" v-bind="{cid:item.i}"></course-card> <!--把你的标签写这里-->
      <div class="remove" @click="removeItem(item.i)">

      </div>
    </grid-item>
    </grid-layout>
  </div>

  <n-button class="uploadButton" @click="openUploadModal" color="#00B8FF">Upload Course Table</n-button>
  <n-modal v-model:show="showModal" title="Upload Course Table" transform-origin="center">
    <n-upload
        action="/course/excel_recognition"
        accept=".xls,.xlsx"
        show-file-list="true"
        class="uploader"
        file-list-style="width: 350px;"
        max="1"
    >
      <n-upload-dragger class="uploadDragger">
        <n-text style="font-size: 16px">
          Click or drag a file to this area to upload
        </n-text>
      </n-upload-dragger>
    </n-upload>
  </n-modal>
  <n-button class="addItem" @click="addItem" color="#00B8FF">Add a course</n-button>
</template>

<script>
import {GridLayout, GridItem} from 'vue3-grid-layout'
import courseCard from "@/components/courseScheduleComponents/courseCard";
import axios from "axios";
import {useToast} from "vue-toastification";
import "vue-toastification/dist/index.css";
import {shallowRef} from "@vue/reactivity";
import {ref} from "vue";

export default {
  setup(){
    const tip = useToast();
    return {tip};
  },
  name: "CourseBoard",
  components:{GridLayout, GridItem, courseCard},
  data(){
    return{
      rawData:[],
      layout: [],
      showModal: ref(false),
      id_list: []
    }
  },
  mounted() {
    // this.$gridlayout.load();
    this.index = this.layout.length;
  },
  created() {
    axios.get('/course/get_all_courses')
    .then((response)=>{
      const code = response.status;
      if (code === 200){
        this.rawData = shallowRef(response.data);
        this.layout = (this.setLayout());
      }
    })
    axios.get('/course/front_id_list')
    .then((response)=>{
      const code = response.status;
      if (code === 200){
        this.id_list= shallowRef(response.data.data);
      }
    })
  },
  methods: {
    addItem: function () {
      console.log(this.id_list)
      // Add a new item. It must have a unique key!
      if (this.id_list[0] !== null){
        this.layout.push({
          x: -1,
          y: -1, // puts it at the bottom
          w: 1,
          h: 1,
          i: this.id_list.sort().reverse()[0] + 1,
        });
        // Increment the counter to ensure key is always unique.
        this.id_list.push(this.id_list.sort().reverse()[0] + 1);
      }else {
        this.layout.push({
          x: -1,
          y: -1, // puts it at the bottom
          w: 1,
          h: 1,
          i: 0,
        });
        // Increment the counter to ensure key is always unique.
        this.id_list.push(0);
      }

    },
    removeItem: function (val) {
      const index = this.layout.map(item => item.i).indexOf(val);
      this.layout.splice(index, 1);
      axios.post('/course/delete', {
        course_id: val
      })
      .then((response)=>{
        const code = response.status;
        if (code === 200){
          this.tip.info('Delete successfully.');
        }
      })
    },
    moveEvent(i, newX, newY){
      console.log(i);
      axios.post('/course/move', {
        course_id: i,
        x: newX,
        y: newY
      })
      .then((response)=>{
        const code = response.status;
        if (code === 200){
          this.tip.info('Change saved successfully.');
        }
      })
    },
    setLayout(){
      let newAllData = [];
      let length = this.rawData.data.length;
      for (let i = 0; i < length; i++){
        let newData = {
          "x": this.rawData.data[i].x,
          "y": this.rawData.data[i].y,
          "w": 1,
          "h": 1,
          "i": this.rawData.data[i].course_id
        }
        newAllData.push(newData);
      }
      return newAllData;
    },
    openUploadModal(){
      this.showModal = true;
    }
  },
  computed:{

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
.uploadButton{
  /*transition: .2s ease-in;*/
  position: relative;
  bottom: 875px;
  left: 345px;/*
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
  cursor: pointer;*/
}
.uploader{
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  height: 200px;
  width: 400px;
  background-color: #FFFFFF;
}
.uploadDragger{
  position: relative;
  top: 30px;
  width: 350px;
}
.addItem{
  /*transition: .2s ease-in;*/
  position: relative;
  bottom: 875px;
  left: 395px;/*
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
  cursor: pointer;*/
}/*
.addItem:hover{
  transition: .2s ease-out;
  box-shadow: 0 0 0 3px #8ab5ff;
}*/
</style>
<style>
.content .vue-grid-item.vue-grid-placeholder {
  background: #8ab5ff !important;
  transition: .5s;
  border-radius: 10px;
}
</style>
