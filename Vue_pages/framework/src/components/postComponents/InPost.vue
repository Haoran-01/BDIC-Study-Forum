<template>
  <div class="FrameWork">
    <div class="ContentCenter">
      <post-entrance v-bind="{item, index}" width="1000" @send-share-info="handleShare"></post-entrance>
      <div class="commentArea">
        <div class="EditArea">
          <quill-editor
              ref="editor"
              v-model:content="content"
              :toolbar="[['bold', 'italic', 'underline'],[{ 'list': 'ordered'}, { 'list': 'bullet' }], [{ 'indent': '-1'}, { 'indent': '+1' }], ['link', 'image']]"
              theme="snow"
          ></quill-editor>
        </div>
        <div class="postBar">
          <div class="ButtonFrame"></div>
          <div class="ButtonArea">
            <button type="button" class="postButton" @click="handlePost">POST</button>
          </div>
        </div>
        <div class="commentDetail">
          <div class="comments" v-for="(item, index) in commentData" :key="index">
            <CommentPost v-bind="{item, index}" @send-reply="handleReply"></CommentPost>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CommentPost from "@/components/postComponents/CommentPost";
import PostEntrance from "@/components/generalComponents/PostEntrance";
import {useToast} from "vue-toastification";
import "vue-toastification/dist/index.css";
import {QuillEditor} from "@vueup/vue-quill";
import '@vueup/vue-quill/dist/vue-quill.snow.css';
export default {
  setup(){
    const tip = useToast();
    return {tip};
  },
  name: "InPost",
  components:{CommentPost, PostEntrance, QuillEditor},
  methods:{
    handleShare(){
      this.tip.info("Link Copied Successfully");
    },
    handlePost(){
      if (this.$refs.editor.getText() === '\n' || this.$refs.editor.getText() === ''){
        this.tip.error("Comment cannot be blank")
      }else {
        axios.post('http://127.0.0.1:4523/mock/831624/forum/publish/post', {
          content: this.content,
          post_id: this.item.post_id
        })
            .then((response)=>{
              const code = response.status;
              if (code === 200){
                this.$refs.editor.setText('');
                this.tip.info("Post Successfully");
              }
            })
      }
    },
    handleReply(email){
      this.$refs.editor.setText('@' + email + ': ');
    }
  },
  data(){
    return{
      item: [],
      commentData:[],
      index:this.$route.params.postId,
      content: {}
    }
  },
  created() {
    axios.get('http://127.0.0.1:4523/mock/831624/forum/post',{
      post_id:this.$route.params.postId
    }).then((response) => {
      this.$data.item=response.data.data;
      this.item = this.item[0]
      this.item.post_id=this.$route.params.postId
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
    justify-self: flex-end;
  }
  .EditArea{
    margin: 15px;
    padding-top: 15px;
    height: 150px;
  }
  .postBar{
    margin-top: 60px;
  }
  .commentArea{
    margin: 15px 0;
    background: #FFFFFF;
    border-radius: 4px;
  }

  .postButton{
    transition: .2s ease-in;
    background-color: rgba(142, 124, 124, 0);
    border: 1px solid #00B8FF;
    cursor: pointer;
    color: #00B8FF;
    border-radius: 15px;
    height: 30px;
    width: 60px;
    margin-right: 15px;
    font-weight: bold;

  }

  .postButton:hover{
    transition: .2s ease-out;
    background-color: #00B8FF;
    color: #FFFFFF;
    font-weight: bold;
  }
</style>