<template>
  <div class="postCreator">
    <div class="postCreatorFrame">
      <div class="headPoster">
        <span class="posterSlogan">Create Post</span>
      </div>
      <div class="sectionSelectorFrame">
        <div class="sectionSelector" id="sectionSelector" @click="handleMenu" @blur="deleteMenu">
          <span class="sectionSelected">{{ sectionTitle }}</span>
          <div class="sectionSelectArrow"></div>
        </div>
        <transition>
          <section-select-menu class="sectionSelectMenu" v-if="sectionSelectMenuVisibility" @click="deleteMenu" @get-section-info="changeSectionTitle"></section-select-menu>
        </transition>
      </div>
      <div class="postInputArea">
        <input class="postTitleInputArea" placeholder="Title" v-model="title">
        <div class="postContent">
          <MdEditor editorClass="postContentEditor" v-model="text" :toolbars="toolbarOption" @onHtmlChanged="saveHtml"></MdEditor>
        </div>
        <button class="postButton" @click="sendPost">
          <span class="postButtonText">Post</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import MdEditor from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
import {ref} from 'vue';
import SectionSelectMenu from "@/components/CreatePostPageComponents/SectionSelectMenu";
import axios from "axios";
import {useToast} from "vue-toastification";
import "vue-toastification/dist/index.css";

export default {
  setup(){
    const postTip = useToast();
    return {postTip};
  },
  name: "CreatePostView",
  components: {MdEditor, SectionSelectMenu},
  data(){
    return{
      sectionId:'',
      title:'',
      text: '',
      html: '',
      sectionSelectMenuVisibility: false,
      sectionTitle: 'Choose Section',
      toolbarOption: ['bold',
        'underline',
        'italic',
        '-',
        'strikeThrough',
        'sub',
        'sup',
        'quote',
        'unorderedList',
        'orderedList',
        '-',
        'codeRow',
        'code',
        'link',
        'image',
        'table',
        'mermaid',
        'katex',
        '-',
        'revoke',
        'next',
        '=',
        'pageFullscreen',
        'preview',
        'catalog',]
    };
  },
  methods:{
    handleMenu(){
      this.$data.sectionSelectMenuVisibility = !this.$data.sectionSelectMenuVisibility;
    },
    deleteMenu(){
      this.$data.sectionSelectMenuVisibility = false;
    },
    changeSectionTitle(newTitle, sectionId){
      this.$data.sectionTitle = ref(newTitle);
      this.$data.sectionId = ref(sectionId);
    },
    saveHtml(h){
      this.$data.html = h;
    },
    sendPost(){
      axios.post('/forum/publish/post', {
        section: this.sectionId,
        title: this.title,
        content: this.html
      })
      .then((response) =>{
        const code = response.status;
        if (code === 200){
          this.postTip.info('Post successfully.')
        }
      })
    }
  },
}
</script>

<style scoped>
.v-enter-from{
  opacity: 0;
}
.v-enter-active{
  transition: opacity 0.2s ease-out;
}
.v-enter-to{
  opacity: 1;
}
.v-leave-from{
  opacity: 1;
}
.v-leave-active{
  transition: opacity 0.2s ease-in;
}
.v-leave-to{
  opacity: 0;
}
.postCreatorFrame {
  display: grid;
  grid-template-columns: 1fr 1000px 1fr;
  grid-template-rows: 135px 50px 500px;
  grid-column-gap: 0px;
  grid-row-gap: 30px;
}

.headPoster{
  grid-area: 1 / 2 / 2 / 3;
  width: 1000px;
  height: 135px;
  background-image: url("../../../../templates/dist/images/create_post_cover.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  border-radius: 0 0 5px 5px;
  position: relative;
}
.posterSlogan{
  font-family: "Noto Sans", sans-serif;
  font-weight: bold;
  font-size: 36px;
  color: #ffffff;
  position: relative;
  right: 390px;
  top: 75px;
  z-index: 2;
}
.headPoster::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  background-color: rgba(0, 0, 0, .3);
  z-index: 1;
  border-radius: 0 0 5px 5px;
}
.sectionSelectorFrame{
  grid-area: 2 / 2 / 3 / 3;
  position: relative;
}
.sectionSelector {
  width: 300px;
  height: 40px;
  background-color: white;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  z-index: 1;
}
.sectionSelected{
  color: #727272;
  font-family: "Noto Sans", sans-serif;
  margin-left: 20px;
}
.sectionSelectArrow{
  background-image: url("../../../../templates/dist/images/menu_arrow_down.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  width: 20px;
  height: 20px;
  margin: 10px;
}
.sectionSelectMenu{
  position: absolute;
  top: 41px;
  z-index: 1;
}
.postInputArea {
  grid-area: 3 / 2 / 4 / 3;
  width: 1000px;
  height: 500px;
  background-color: #FFF;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 5px;

  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 80px 1fr 80px;
}
.postTitleInputArea {
  grid-area: 1 / 1 / 2 / 2;
  margin: 20px;
  width: 960px;
  height: 40px;
  background-color: #EEEEEE;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 5px;
  display: flex;
  align-items: center;

  box-sizing: border-box;
  padding-left: 10px;
  font-weight: bold;
  font-family: "Noto Sans", sans-serif;
  outline: rgba(0, 0, 0, 0.2) 1px;
  transition: .2s ease-out;
}
.postTitleInputArea ::placeholder{
  color: #727272;
}
.postTitleInputArea:hover{
  transition: .2s ease-in;
  box-shadow: 2px 3px 5px 1px #bdbdbd;
}
.postTitleInputArea:focus{
  transition: .2s ease-in;
  box-shadow: 2px 3px 5px 1px #bdbdbd;
}
.postContent {
  grid-area: 2 / 1 / 3 / 2;
  height: 340px;
  width: 960px;
  margin-left: 20px;
  margin-right: 20px;
  background-color: #EEEEEE;
}
.postContentEditor{
  height: 340px;
  width: 960px;
  border-radius: 5px;
}
.postButton {
  transition: .3s ease-in;
  grid-area: 3 / 1 / 4 / 2;
  margin: 20px;
  width: 80px;
  height: 40px;
  background-color: #00B8FF;
  border-radius: 100px;
  justify-self: end;
  border: none;
  cursor: pointer;
}
.postButton:hover{
  transition: .3s ease-out;
  box-shadow: 0 0 0 3px #8ab5ff;
}
.postButtonText{
  font-family: "Noto Sans", sans-serif;
  font-weight: bold;
  color: #FFFFFF;
  font-size: 18px;
}

</style>