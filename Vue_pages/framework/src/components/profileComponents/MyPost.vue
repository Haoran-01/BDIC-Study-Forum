<template>
  <div class="postList" v-if="postVisibility">
    <div class="postListLogic" v-for="(item, index) in postData" :key="index">
      <post-entrance v-bind="{item, index}" :width="998" @send-share-info="handleShare"></post-entrance>
    </div>
  </div>
  <div class="createPostTip" v-else>
    <div class="createPostSlogan">Glad to see your interaction!</div>
    <router-link class="createPostButton" to="/create_post">
      <div class="createPostButtonText">Create Post</div>
    </router-link>
  </div>

</template>

<script>
import axios from "axios";
import PostEntrance from "@/components/generalComponents/PostEntrance";
import {useToast} from "vue-toastification";
import "vue-toastification/dist/index.css";

export default {
  setup(){
    const tip = useToast();
    return {tip};
  },
  name: "MyPost",
  components: {PostEntrance},
  data(){
    return{
      postData: {},
      postVisibility: false
    }
  },
  methods:{
    handleShare(){
      this.tip.info("Link Copied Successfully");
    }
  },
  created() {
    axios.get('http://127.0.0.1:4523/mock/831624/profile/my_post?apifoxResponseId=36910546', {
      params:{
        email: this.$route.query.email
      }
    })
        .then((response) =>{
          const code = response.status;
          if (code === 200){
            this.postData = response.data.data;
            this.postVisibility = true;
          }else if (code === 201){
            this.postVisibility = false;
          }
        })
  }
}
</script>

<style scoped>
a{
  text-decoration-line: none;
}
.createPostTip{
  width: 1000px;
  display: grid;
  grid-template-rows: 100px 50px;
  align-items: center;
}
.createPostSlogan{
  grid-area: 1 / 1 / 2 / 2;
  font-family: "Noto Sans", sans-serif;
  font-size: 20px;
  font-weight: bold;
}
.createPostButton {
  grid-area: 2 / 1 / 3 / 2;
  transition: .3s ease-in;
  width: 200px;
  height: 40px;
  border-radius: 100px;
  background-color: #00B8FF;
  justify-self: center;
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