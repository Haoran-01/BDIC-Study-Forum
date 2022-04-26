<template>
  <div class="FrameWork">
    <div class="topBar">
      <router-link :to="{path:'/profile',query:{email:item.user_email}}">
        <img :src=item.user_image class="headImage">
      </router-link>
      <router-link :to="{path:'/profile',query:{email:item.user_email}}">
        <span class="userName">{{item.user_name}}</span>
      </router-link>
      <span class="point">·</span>
      <span class="Time">{{item.time}}</span>
    </div>
    <div class="CommentContent">
      {{item.content}}
    </div>
    <div class="bottomBar">
      <div class="choiceLike">
        <button type="button" class="Like" :id="setLikeId" @click="handleLike">Like {{like}}</button>
      </div>
      <div class="choiceReply">
        <button type="button" class="Reply" :id="setReplyId" @click="handleReply">Reply</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommentPost",
  props:[
      "item",
      "index"
  ],
  emits:['sendReply'],
  data(){
    return {like: null}
  },
  methods:{
    handleLike(){
      const likeId = 'like' + this.$props.index;
      const likeButton = document.getElementById(likeId);
      if (likeButton.getAttribute('class') === 'Like'){
        likeButton.setAttribute('class', 'LikeActivated');
        this.like = this.like + 1;
        /*axios.post('')
        .then()*/
      }else {
        likeButton.setAttribute('class', 'Like');
        this.like = this.like - 1;
      }
    },
    handleReply(){
      this.$emit('sendReply', this.item.user_name);
    }
  },
  computed:{
    setLikeId(){
      return 'like' + this.index;
    },
    setReplyId(){
      return 'reply' + this.index;
    }
  },
  created() {
    this.like = this.item.like;
  }
}
</script>

<style scoped>
button{
  font-family: "Noto Sans", sans-serif;
}
a{
  color: black;
  text-decoration-line: none;
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

.FrameWork{
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: repeat(3, 1fr);
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  width:1000px
}

.topBar{
  grid-area: 1 / 1 / 2 / 2;
  display: flex;
  align-items: center;
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

.Time{
  font-family: "Noto Sans", sans-serif;
  font-weight: bold;
}

.CommentContent{
  grid-area: 2 / 1 / 3 / 2;
  padding: 10px 30px;
  text-align: left;
  width: 1000px;
}

.bottomBar{
  grid-area: 3 / 1 / 4 / 2;
  display: flex;
  padding: 10px 30px;
}

.choiceLike{
  margin: 0 10px 0 0;
}

.choiceReply{
  margin: 0 5px;
}

.Like{
  transition: ease-in .2s;
  padding: 5px 10px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 15px;
  cursor: pointer;
  background-color: #FFFFFF;
  font-weight: bold;
}

.Like:hover{
  transition: ease-out .2s;
  background-color: #00B8FF;
  color: #FFFFFF;
  border: 1px solid #00B8FF;
}
.LikeActivated{
  transition: ease-out .2s;
  padding: 5px 10px;
  border-radius: 15px;
  cursor: pointer;
  font-weight: bold;
  background-color: #00B8FF;
  color: #FFFFFF;
  border: 1px solid #00B8FF;
}

.Reply{
  transition: ease-in .2s;
  padding: 5px 10px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 15px;
  cursor: pointer;
  background-color: #FFFFFF;
  font-weight: bold;
}

.Reply:hover{
  transition: ease-out .2s;
  background-color: #00B8FF;
  color: #FFFFFF;
  border: 1px solid #00B8FF;
}
</style>