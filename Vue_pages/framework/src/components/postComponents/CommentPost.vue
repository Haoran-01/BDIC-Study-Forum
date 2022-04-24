<template>
  <div class="FrameWork">
    <div class="topBar">
      <img :src=user_image class="headImage">
      <span class="userName">{{user_email}}</span>
      <span class="point">·</span>
      <span class="Time">{{time}}</span>
    </div>
    <div class="CommentContent">
      {{content}}
    </div>
    <div class="bottomBar">
      <div class="choiceLike">
        <button type="button" class="Like">Like</button>
      </div>
      <div class="choiceReply">
        <button type="button" class="Reply">Reply</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommentPost",
  props:[
      "user_email",
      "content",
      "time",
      "user_image"
  ]
}
</script>

<style scoped>
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
  padding: 5px 10px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 15px;
  cursor: pointer;
  background-color: #FFFFFF;
  font-weight: bold;
}

.Like:hover{
  background-color: #00B8FF;
  color: #FFFFFF;
}


.Reply{
  padding: 5px 10px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 15px;
  cursor: pointer;
  background-color: #FFFFFF;
  font-weight: bold;
}

.Reply:hover{
  background-color: #00B8FF;
  color: #FFFFFF;
}
</style>