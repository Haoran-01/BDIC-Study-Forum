<template>
<div class="activityCard">
  <div class="activityCardFrame">
    <div class="activityCardSlogan">Glad to see your interaction!</div>
    <div class="activityCardDataFrame">
      <div class="activityNumber" id="postNumber">{{ post_number }}</div>
      <div class="activityNumber" id="commentNumber">{{ comment_number }}</div>
      <div class="activityNumber" id="agreeNumber">{{ agree_number }}</div>
      <div class="activityText" id="postText">your<br/>posts</div>
      <div class="activityText" id="commentText">your<br/>comments</div>
      <div class="activityText" id="agreeText">your<br/>agrees</div>
      <div class="line" id="leftLine"></div>
      <div class="line" id="rightLine"></div>
    </div>
    <router-link class="createPostButton" to="/create_post">
      <span class="createPostButtonText">Create Post</span>
    </router-link>
  </div>
</div>
</template>

<script>
import axios from "axios";

export default {
  name: "userActivityCard",
  data(){
    return {
      post_number: 0,
      comment_number: 0,
      agree_number: 0
    }
  },
  created() {
    axios.get('http://127.0.0.1:4523/mock/831624/index/get_information')
    .then((response)=>{
      if (response.status === 200){
        this.$data.post_number = response.data.post_number;
        this.$data.comment_number = response.data.comment_number;
      }
    })
  }
}
</script>

<style scoped>
a{
  text-decoration-line: none;
}
.activityCard{
  margin-top: 20px;
  width: 296px;
  height: 220px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 4px;
  background-color: #FFFFFF;
}
.activityCardFrame {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 30px 1fr 40px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;

  margin: 20px;
}

.activityCardSlogan {
  grid-area: 1 / 1 / 2 / 2;
  font-family: "Noto Sans", sans-serif;
  font-weight: bolder;
  font-size: 17px;
}
.activityCardDataFrame {
  grid-area: 2 / 1 / 3 / 2;
  display: grid;
  grid-template-columns: 1fr 1px 1fr 1px 1fr;
  grid-template-rows: repeat(2, 1fr);
  grid-column-gap: 0px;
}
.activityNumber{
  font-size: 40px;
  font-family: "Noto Sans", sans-serif;
  font-weight: bolder;
}
.activityText{

}
.line{
  background-color: rgba(0, 0, 0, 0.2);
  height: 65px;
  width: 1px;
  margin-top: 8px;
}
#postNumber { grid-area: 1 / 1 / 2 / 2; }
#commentNumber { grid-area: 1 / 3 / 2 / 4; }
#agreeNumber { grid-area: 1 / 5 / 2 / 6; }
#postText { grid-area: 2 / 1 / 3 / 2; }
#commentText { grid-area: 2 / 3 / 3 / 4; }
#agreeText { grid-area: 2 / 5 / 3 / 6; }
#leftLine { grid-area: 1 / 2 / 3 / 3; }
#rightLine { grid-area: 1 / 4 / 3 / 5; }
.createPostButton {
  transition: .3s ease-in;
  grid-area: 3 / 1 / 4 / 2;
  width: 100%;
  height: 100%;
  border-radius: 100px;
  background-color: #00B8FF;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.createPostButton:hover{
  transition: .3s ease-out;
  box-shadow: 0 0 0 3px #8ab5ff;
}
.createPostButtonText{
  font-family: "Noto Sans", sans-serif;
  font-weight: bold;
  font-size: 18px;
  color: #FFFFFF;
}
</style>