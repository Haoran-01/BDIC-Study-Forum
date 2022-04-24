<template>
  <div class="courseCard">
    <div class="colorBar" :style="{ backgroundColor: colors.hex,}"> </div>
    <div class="subjectTitle"> {{ subject }}
     <div class="changeSection">
       <button type="button" class="changeButton" @click="showModal=true">
       </button>
       <Modal v-model="showModal" title="Change Detail" :modalStyle="'max-width: 600px'">
         <div class="modalFrame">
           <div class="subjectArea">
             <label class="modalInputText">Subject</label>
             <input class="modalInput" v-model="subject"/>
           </div>
           <div class="classRoomArea">
             <label class="modalInputText">ClassRoom</label>
             <input class="modalInput" v-model="classroom"/>
           </div>
           <div class="lecturerArea">
             <label class="modalInputText">Lecturer</label>
             <input class="modalInput" v-model="lecturer"/>
           </div>
           <Sketch class="colorSelector" v-model="colors"/>
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
      subject: "Subject",
      classroom: "",
      lecturer: "",
      colors: ''
    }
  }
}
</script>

<style scoped>
input{
  font-family: "Noto Sans", sans-serif;
}
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
  font-family: "Noto Sans", sans-serif;

  text-align:left;
}
.courseCard:hover .changeButton{
  transition: .2s ease-out;
  opacity: 1;
}
.changeSection {
  width: 20px;
  height: 20px;
  position: absolute;
  right: 20px;
  top: 95px;
  background-color: white;
}
.changeButton{
  transition: .2s ease-in;
  opacity: 0;
  background-image: url("../../../../../templates/dist/images/setting.png");
  height: 100%;
  width: 100%;
  background-repeat: no-repeat;
  background-size: contain;
  background-color: white;
  border: none;
  cursor: pointer;
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
.modalFrame {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(3, 1fr);
  grid-column-gap: 0px;
  grid-row-gap: 0px;

  align-items: center;
  justify-content: center;
}
.modalInputText{
  display: block;
  margin: 5px 0;
  font-size: 20px;
  font-family: "Noto Sans", sans-serif;
  font-weight: bold;
}
.modalInput{
  transition: .2s ease-out;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 100px;
  outline: rgba(0, 0, 0, 0.2) 1px;
  width: 200px;
  height: 25px;
  padding-left: 10px;
}
.modalInput:hover{
  transition: .2s ease-in;
  box-shadow: 0 0 0 3px #8ab5ff;
}
.modalInput:focus{
  transition: .2s ease-in;
  box-shadow: 0 0 0 3px #8ab5ff;
}

.subjectArea { grid-area: 1 / 1 / 2 / 2; }
.classRoomArea { grid-area: 2 / 1 / 3 / 2; }
.lecturerArea { grid-area: 3 / 1 / 4 / 2; }
.colorSelector {
  grid-area: 1 / 2 / 4 / 3;
  justify-self: center;
}
</style>