<template>
<div class="menuMain">
  <div class="postListLogic" v-for="(item, index) in sectionData" :key="index">
    <div class="menuItem" @click="sendSectionInfo(item.type_name, item.type_name)">
      <img class="menuItemIcon" :src=item.section_image_url height="40" width="40"/>
      <div class="menuItemText"> {{ item.type_name }} </div>
    </div>
  </div>
</div>
</template>

<script>
// import axios from 'axios';
import axios from "axios";

export default {
  name: "NavUserMenu",
  emits: ['getSectionInfo'],
  methods: {
    sendSectionInfo(title, sectionId){
      this.$emit('getSectionInfo', title, sectionId);
    }
  },
  data(){
    return{
      sectionData: [
        {
          section_image_url: require('../../../../../templates/dist/images/R&Q.jpeg'),
          type_name: 'Campus News'
        },
        {
          section_image_url: require('../../../../../templates/dist/images/Lost&Found.jpeg'),
          type_name: 'Lost & Found'
        },
      ]
    }
  },
  created() {
    axios.get('http://127.0.0.1:4523/mock/831624/forum/sections')
    .then((response) =>{
      this.sectionData = response.data.data;
    })
  }
  /*  created() {
      axios.get('')
      .then((response) => {
        this.sectionData = response.data;
      })
      .catch(function (error){
        console.log(error)
      })
    }*/
}
</script>

<style scoped>
.menuMain{
  width: 300px;
  height: auto;
  background-color: #FFFFFF;
  border-radius: 4px;
  border: 1px solid rgba(0, 0, 0, 0.2);
}
.menuItem{
  transition: 0.3s;
  display: flex;
  width: 100%;
  height: 50px;
  box-sizing: border-box;
  padding-left: 10px;
  padding-right: 10px;
  align-items: center;
  cursor: pointer;
}
.menuItem:hover{
  transition: 0.3s;
  background-color: rgba(0, 0, 0, 0.1);
}
a{
  text-decoration: none;
}
.menuItemIcon{
  border-radius: 100px;
  border: 1px solid rgba(0, 0, 0, 0.2);
}
#profileIcon{
  background-image: url("../../../../../templates/dist/images/profile.png");
}
.menuItemText, .menuItemText:visited{
  font-family: "Noto Sans", sans-serif;
  font-weight: normal;
  font-size: 20px;
  margin-left: 20px;
  text-decoration: none;
  color: black;
}
</style>