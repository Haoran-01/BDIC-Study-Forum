<template>
  <div class="courseCard">
    <div class="colorBar" :style="{ backgroundColor: colors.hex,}"> </div>
    <div class="subjectTitle"> Subject
     <div class="changeSection">
       <button type="button" class="changeButton" @click="showModal=true">
       </button>
       <Modal v-model="showModal" title="Change Detail" >
         <div>
           <div>
             <label>ClassRoom</label>
           </div>
           <div>
             <input v-model="classroom"/>
           </div>
         </div>
         <div>
           <div>
             <lable>Lecturer</lable>
           </div>
           <div>
             <input v-model="lecturer"/>
           </div>
           <div class="color">
             <Sketch v-model="colors"/>
           </div>
         </div>
       </Modal>
     </div>
    </div>
    <div class="classRoom">
    Classroom:<br>
      <span Style="font-weight: bold;">{{classroom}}</span>
    </div>
    <div class="lecture">
    Lecturer:<br>
      <span Style="font-weight: bold;">{{lecturer}}</span>
    </div>

  </div>
</template>

<script>
import VueModal from '@kouts/vue-modal'
import '@kouts/vue-modal/dist/vue-modal.css'
import { Sketch } from '@ckpack/vue-color';

export default {
  name: "courseCard",
  components: {
    'Modal': VueModal,
    Sketch,
  },
  data() {
    return {
      showModal: false,
      classroom: "",
      lecturer: "",
      colors: ''
    }
  }
}
</script>

<style scoped>
.courseCard {
  margin: auto;
  height: 114px;
  width: 200px;
  display: grid;
  grid-template-columns: 1fr repeat(2, 13px) 10px 170px 1fr;
  grid-template-rows: 0 5px 22px 7px 30px 12px 30px 7px 0;
  grid-column-gap: 0px;
  grid-row-gap: 0px;

  background-color: white;
  border-radius: 10px;
  box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.15);

  text-align:left;
}
.changeSection {
  background-color: #00B8FF;
  width: 20px;
  height: 20px;
  position: absolute;
  right: 20px;
  top: 95px;
}
.changeButton{
  height: 100%;
  width: 100%;
}
.colorBar {
  grid-area: 2 / 3 / 9 / 4;
  background-color: red;
}
.subjectTitle {
  grid-area: 3 / 5 / 4 / 6;

  font-family: 'Arial Rounded MT',sans-serif;
  font-style: normal;
  font-size: 20px;

  color: #000000;
}
.classRoom {
  grid-area: 5 / 5 / 6 / 6;
  font-size: 15px;
}
.lecture {
  grid-area: 7 / 5 / 8 / 6;
  font-size: 15px;
}
</style>