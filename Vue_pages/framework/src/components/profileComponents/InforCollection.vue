<template>
  <div class="Shorten">
    <div class="header">
      <div class="Username">{{currentName}}</div>
      <div class="title">Introduction</div>
      <div class="line"></div>
    </div>
    <div class="content">
      <div class="e-mail contentText">
        <span>E-mail:</span>
        <span>{{currentEmail}}</span>
      </div>
    </div>
  </div>


</template>

<script>
import axios from "axios";

export default {
  name: "InforCollection",
  data(){
    return{
      currentEmail:'',
      currentName:''
    }
  },
  created() {
    this.currentEmail=this.$route.query.email;

    axios.get('/profile', {
      params:{
        user_email:this.currentEmail
      }
    })
    .catch(function (error) {
      console.log(error);
    });
  }
}
</script>

<style scoped>
  .Username{
    font-size: 23px;
    display: flex;
    margin: 30px 0;
  }

  .title{
    font-size: 13px;
    display: flex;
    color: #929497;
    margin: 5px 0;

  }

  .line{
    display: flex;
    width: 100px;
    height: 0.5px;
    margin: 5px 0;
    padding: 0;
    background-color: #929497;
  }

  .content{
    margin: 10px 0;
  }


  .contentText{
    display: flex;
    margin: 13px 0 5px;
    font-size: 15px;
  }


</style>