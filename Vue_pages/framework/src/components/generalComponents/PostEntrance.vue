<template>
<div class="postEntranceFrame" :style="setWidth">
  <div class="topBar">
    <router-link  :to="{path:'/profile',query:{email:item.user_email}}">
      <img class="headImage" :src=this.item.picture_url >
    </router-link>
    <router-link  :to="{path:'/profile',query:{email:item.user_email}}">
    <span class="userName">{{ item.user_name }}</span>
    </router-link>
    <span class="point">·</span>
    <router-link class="section" :to="{path:'/sector',query:{typeName:this.type_name}}">{{ item.post_type_name }}</router-link>
  </div>
  <router-link class="postTitle" :to="{path:'/post',query:{postId:item.post_id}}">{{item.title}}</router-link>
  <div class="postImage">{{item.content}}</div>
  <div class="postToolBar">
    <router-link class="toolButton" id="comment" :to="{path:'/post',query:{postId:item.post_id}}">
      <div class="postIcon" id="commentIcon"></div>
      <span class="toolText" id="commentNumber">{{ item.comments_number }} Comments</span>
    </router-link>
    <div class="toolButton" id="share" @click="handleShare">
      <div class="postIcon" id="shareIcon"></div>
      <span class="toolText" id="shareText">Share</span>
    </div>
    <div class="toolButton" id="favorite" @click="handleFavorite">
      <div class="favoriteIcon" :id="index"></div>
      <span class="toolText" id="favoriteText">Favorite</span>
    </div>
  </div>
</div>
</template>

<script>
// import axios from "axios";
import { toClipboard } from '@soerenmartius/vue3-clipboard'

export default {
  name: "PostEntrance",
  props: ['item', 'index', 'width'],
  emits: ['sendShareInfo'],
  data(){
    return{
      type_name: this.item.post_type_name
    }
  },
  methods:{
    handleShare(){
      toClipboard(window.location.host + '#/post/' + this.item.post_id);
      this.$emit('sendShareInfo');
    },
    handleFavorite(){
      const id = this.$props.index;
      const favoriteIcon = document.getElementById(id);
      if (favoriteIcon.getAttribute('class') === 'favoriteIcon'){
        favoriteIcon.setAttribute('class', 'favoriteIconActivated');
        /*axios.post('')
        .then()*/
      }else {
        favoriteIcon.setAttribute('class', 'favoriteIcon');
      }
    }
  },
  computed:{
    setWidth(){
      return 'width: ' + this.width + 'px';
    }
  }
}
</script>

<style scoped>
a{
  color: black;
  text-decoration-line: none;
}
.postEntranceFrame {
  display: grid;
  grid-template-columns: 30px 1fr 30px;
  grid-template-rows: 36px auto auto 36px;
  grid-column-gap: 0px;
  grid-row-gap: 15px;

  width: 682px;
  background-color: #FFFFFF;
  border-radius: 4px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  margin-bottom: 20px;
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.10);
}

.topBar {
  grid-area: 1 / 1 / 2 / 4;
  width: 100%;
  height: 100%;
  background-color: rgba(196, 196, 196, 0.2);
  display: flex;
  align-items: center;
}

.headImage{
  height: 30px;
  width: 30px;
  border-radius: 50%;
  box-shadow: 0 0 3px #727272;
  background-color: #00B8FF;
  display: inline-block;
  margin-left: 10px;
  margin-right: 10px;
}

.userName{
  font-family: "Noto Sans", sans-serif;
}
.point{
  font-family: "Noto Sans", sans-serif;
  font-weight: bold;
  margin-left: 5px;
  margin-right: 5px;
}
.section{
  font-family: "Noto Sans", sans-serif;
  font-weight: bold;
}

.postTitle {
  grid-area: 2 / 2 / 3 / 3;

  font-size: 20px;
  font-weight: bold;
  font-family: "Noto Sans", sans-serif;
  text-align: left;
}
.postImage {
  grid-area: 3 / 2 / 4 / 3;
  text-align: left;
}
.postToolBar {
  grid-area: 4 / 1 / 5 / 4;
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
}

.postToolBar *{
  display: flex;
  align-items: center;
  justify-content: space-around;
}

.toolButton {
  cursor: pointer;
}
.postIcon{
  display: inline-block;
  margin-right: 10px;
  margin-left: 10px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

#commentIcon{
  background-image: url("../../../../../templates/dist/images/message.png");
  width: 30px;
  height: 30px;
}

#shareIcon{
  background-image: url("../../../../../templates/dist/images/link.png");
  width: 30px;
  height: 30px;
}

.favoriteIcon{
  transition: .3s;
  display: inline-block;
  margin-right: 10px;
  margin-left: 10px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  background-image: url("../../../../../templates/dist/images/star.png");
  width: 35px;
  height: 35px;
}

.favoriteIconActivated{
  transition: .3s;
  background-image: url("../../../../../templates/dist/images/star_active.png");
  width: 35px;
  height: 35px;
  display: inline-block;
  margin-right: 10px;
  margin-left: 10px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

.toolText{
  font-family: "Noto Sans", sans-serif;
  margin-right: 10px;
  margin-left: 10px;
  cursor: pointer;
}

a{
  text-decoration: none;
  color: black;
}
</style>