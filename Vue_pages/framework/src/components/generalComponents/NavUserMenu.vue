<template>
<div class="menuMain">
  <router-link class="menuItem" to="/create_post">
    <div class="menuItemIcon" id="createPostIcon"></div>
    <div class="menuItemText"> New Post </div>
  </router-link>
  <router-link class="menuItem" :to="{path:'profile',query:{email:this.emailId}}">
    <div class="menuItemIcon" id="profileIcon"></div>
    <div class="menuItemText"> Profile </div>
  </router-link>
  <div class="menuItem" @click="logOut">
    <div class="menuItemIcon" id="logoutIcon"></div>
    <div class="menuItemText">Log Out</div>
  </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: "NavUserMenu",
  data(){
    return{
      emailId:''
    }
  },
  methods:{
    logOut(){
      axios.get('/logout')
      window.location.assign(window.location.origin + '/user/login');
    }
  },
  created() {
    axios.get('/get_session')
      .then((response) => {
        this.emailId=response.data.message;
      })
      .catch(function (error){
        console.log(error)
      })
  }
}
</script>

<style scoped>
.menuMain{
  width: 160px;
  height: auto;
  background-color: #FFFFFF;
  border-radius: 4px;
  border: 1px solid rgba(0, 0, 0, 0.2);
}
.menuItem{
  transition: .3s;
  display: flex;
  width: 100%;
  height: 40px;
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
.menuItem:hover #createPostIcon{
  background-image: url("../../../../../templates/dist/images/add_post_active.png");
}
.menuItem:hover #profileIcon{
  background-image: url("../../../../../templates/dist/images/profile_active.png");
}
.menuItem:hover #logoutIcon{
  background-image: url("../../../../../templates/dist/images/door_out_active.png");
}
a{
  text-decoration: none;
}
.menuItemIcon{
  width: 30px;
  height: 30px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: right;
}
#createPostIcon{
  background-image: url("../../../../../templates/dist/images/add_post.png");
}
#profileIcon{
  background-image: url("../../../../../templates/dist/images/profile.png");
}
#logoutIcon{
  background-image: url("../../../../../templates/dist/images/door_out.png");
}
.menuItemText, .menuItemText:visited{
  font-family: "Noto Sans", sans-serif;
  font-weight: normal;
  font-size: 18px;
  margin-left: 20px;
  text-decoration: none;
  color: black;
}
</style>