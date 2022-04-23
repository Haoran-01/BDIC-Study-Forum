<template>
  <div class="FrameWork">
    <div class="ContentCenter">
      <div class="PostShow">
<!--        post显示区域-->
      </div>
      <div class="commentArea">
        <div class="EditArea">

        </div>
        <div class="postBar">
          <div class="ButtonFrame"></div>
          <div class="ButtonArea">
            <button type="button" class="postButton">POST</button>
          </div>
        </div>
        <div class="commentDetail">
          <div class="comments" v-for="(item, index) in commentData" :key="index">
            <CommentPost v-bind="item"></CommentPost>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CommentPost from "@/components/postComponents/CommentPost";
export default {
  name: "InPost",
  components:{CommentPost},
  data(){
    return{
      postData:[],
      commentData:[]
    }
  },
  created() {
    axios.get('http://127.0.0.1:4523/mock/831624/forum/post',{
      post_id:this.$route.params.postId
    }).then((response) => {
      this.postData=response.data.data;
    }).catch(function (error) {
      console.log(error);
    });

    axios.get('http://127.0.0.1:4523/mock/831624/forum/post/comments',{
      post_id:this.$route.params.postId
    }).then((response) => {
      this.commentData=response.data.comments;
    }).catch(function (error) {
      console.log(error);
    });
  }
}
</script>

<style scoped>
  .FrameWork{
    display: grid;
    grid-template-columns: 1fr 1000px 1fr;
    grid-template-rows: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
  }

  .ContentCenter{
    grid-area: 1 / 2 / 2 / 3;
  }

  .postBar{
    display: grid;
    grid-template-columns: 800px 1fr;
    grid-template-rows: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
  }

  .ButtonFrame{
    grid-area: 1 / 1 / 2 / 2;
  }

  .ButtonArea{
    grid-area: 1 / 2 / 2 / 3;
  }

  .commentArea{
    margin: 15px 0;
    background: #FFFFFF;
    border-radius: 4px;
  }

  .postButton{
    background-color: #929497;
    border-style: none;
    cursor: pointer;
    color: #FFFFFF;
    border-radius: 15px;
    padding: 4px 8px;
    font-weight: bold;
  }

  .postButton:hover{
    background-color: #00B8FF;
    color: #FFFFFF;
    font-weight: bold;
  }
</style>