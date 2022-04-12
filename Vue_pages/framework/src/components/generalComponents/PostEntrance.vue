<template>
<div class="postEntranceFrame">
  <div class="topBar">
    <div class="headImage"></div>
    <span class="userName">name</span>
    <span class="point">·</span>
    <span class="section">section</span>
  </div>
  <div class="postTitle">TitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitle</div>
  <div class="postImage">TitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitle</div>
  <div class="postToolBar">
    <div class="comment">
      <div class="postIcon" id="commentIcon"></div>
      <span class="toolText" id="commentNumber">13 Comments</span>
    </div>
    <div class="share">
      <div class="postIcon" id="shareIcon"></div>
      <span class="toolText" id="shareText">Share</span>
    </div>
    <div class="favorite">
      <div class="postIcon" id="favoriteIcon"></div>
      <span class="toolText" id="favoriteText">Favorite</span>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "PostEntrance"
}
</script>

<style scoped>
.postEntranceFrame {
  display: grid;
  grid-template-columns: 30px 622px 30px;
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
.postImage { grid-area: 3 / 2 / 4 / 3; }
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

.postIcon{
  width: 30px;
  height: 30px;
  background-color: #00B8FF;
  display: inline-block;
  margin-right: 10px;
  margin-left: 10px;
}

.toolText{
  font-family: "Noto Sans", sans-serif;
  margin-right: 10px;
  margin-left: 10px;
}
</style>