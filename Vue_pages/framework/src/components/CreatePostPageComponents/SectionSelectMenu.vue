<template>
<div class="menuMain">
  <div class="postListLogic" v-for="(item, index) in sectionData" :key="index">
    <div class="menuItem" @click="sendSectionTitle(item.sectionTitle)">
      <img class="menuItemIcon" :src=item.sectionCoverImageURL height="40" width="40"/>
      <div class="menuItemText"> {{ item.sectionTitle }} </div>
    </div>
  </div>
</div>
</template>

<script>
// import axios from 'axios';
export default {
  name: "NavUserMenu",
  emits: ['getSectionTitle'],
  methods: {
    sendSectionTitle(title){
      this.$emit('getSectionTitle', title);
    }
  },
  data(){
    return{
      sectionData: [
        {
          sectionCoverImageURL: require('../../../../../templates/dist/images/R&Q.jpeg'),
          sectionTitle: 'Campus News'
        },
        {
          sectionCoverImageURL: require('../../../../../templates/dist/images/Lost&Found.jpeg'),
          sectionTitle: 'Lost & Found'
        },
      ]
    }
  },
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