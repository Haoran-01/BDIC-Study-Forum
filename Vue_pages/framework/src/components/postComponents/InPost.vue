<template>
  <div class="FrameWork" v-show="!pdf">
    <div class="ContentCenter" v-show="!pdf">
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
            <button type="button" class="postButton" @click="pdfBtn">Convert</button>
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
  <div class="FrameWork3" v-show="pdf">
    <div class="ContentCenter" v-show="pdf" id="pdfDom">

      <div class="postEntranceFrame" v-bind="{item, index}" >
        <div class="topBar1">
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
        <div class="postContent" :id="'postContent' + this.index" v-html="this.item.content"></div>

      </div>


<!--      <post-entrance v-bind="{item, index}" width="1000" @send-share-info="handleShare"></post-entrance>-->


      <div class="commentArea">
        <div class="postBar2">
          <div class="ButtonFrame"></div>
          <div class="ButtonArea">
            <button type="button" class="postButton" @click="print">PDF</button>
            <button type="button" class="postButton" @click="pdfBtn">Return</button>
          </div>
        </div>
        <div class="commentDetail">
          <div class="comments" v-for="(item, index) in commentData" :key="index" >

            <div class="FrameWork2">
              <div class="topBar2">
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

            </div>

<!--            <CommentPost v-bind="{item, index}" @send-reply="handleReply"></CommentPost>-->

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
import html2canvas from "html2canvas";
import jsPDF  from "jspdf";
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
        axios.post('/forum/publish/comment', {
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
    },
    pdfBtn(){
      this.pdf = !this.pdf;
    },
    print() {
      const downPdf = document.getElementById("pdfDom");
      html2canvas(downPdf).then((canvas) => {
        var contentWidth = canvas.width;
        var contentHeight = canvas.height;
        var pageHeight = (contentWidth / 592.28) * 841.89;
        var leftHeight = contentHeight;
        var position = 0;
        var imgWidth = 595.28;
        var imgHeight = (592.28 / contentWidth) * contentHeight;
        var pageData = canvas.toDataURL("image/jpeg", 1.0);
        var pdf = new jsPDF("", "pt", "a4");
        if (leftHeight < pageHeight) {
          pdf.addImage(pageData, "JPEG", 0, 0, imgWidth, imgHeight);
        } else {
          while (leftHeight > 0) {
            pdf.addImage(pageData, "JPEG", 0, position, imgWidth, imgHeight);
            leftHeight -= pageHeight;
            position -= 841.89;
            if (leftHeight > 0) {
              pdf.addPage();
            }
          }
        }
        pdf.save("CyanPine_pdf_" + new Date().getTime() + ".pdf");
      });
    }

  },
  data(){
    return{
      item: [],
      commentData:[],
      index:this.$route.query.postId,
      content: {},
      pdf:false,
    }
  },
  created() {
    // /forum/post
    axios.get('/forum/post',{
      params:{
        post_id:this.$route.query.postId
      }
    }).then((response) => {
      this.$data.item=response.data.data;
      this.item = this.item[0]
      this.item.post_id=this.$route.query.postId
    }).catch(function (error) {
      console.log(error);
    });

    // /forum/post/comments
    axios.get('/forum/post/comments',{
      params:{
        post_id:this.$route.query.postId
      }
    }).then((response) => {
      this.commentData=response.data.comments;
    }).catch(function (error) {
      console.log(error);
    });
  }
}
</script>

<style scoped>
a{
  color: black;
  text-decoration-line: none;
}

.postEntranceFrame {
  width:800px;
  display: grid;
  grid-template-columns: 30px 1fr 30px;
  grid-template-rows: 36px auto auto 36px;
  grid-column-gap: 0px;
  grid-row-gap: 15px;


  background-color: #FFFFFF;
  border-radius: 4px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  margin-bottom: 20px;
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.10);
}

.topBar1 {
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
.postContent {
  grid-area: 3 / 2 / 4 / 3;
  text-align: left;
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

.FrameWork2{
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: repeat(3, 1fr);
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  width:1000px
}

.topBar2{
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
  padding: 2px 30px;
  text-align: left;
  width: 1000px;
}

.FrameWork3{
  display: grid;
  grid-template-columns: 1fr 800px 1fr;
  grid-template-rows: 1fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
}



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
    margin-top: 60px;
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
  .postBar2{
    display: grid;
    grid-template-columns: 600px 1fr;
    grid-template-rows: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    margin-top: 10px;
  }
  .commentArea{
    margin: 5px 0;
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