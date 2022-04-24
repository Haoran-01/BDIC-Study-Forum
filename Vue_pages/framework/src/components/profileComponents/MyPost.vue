<template>
  <div class="postList" v-if="postVisibility">
    <div class="postListLogic" v-for="(item, index) in postData" :key="index">
      <post-entrance v-bind="{item, index}" :width="998" @send-share-info="handleShare"></post-entrance>
    </div>
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
    axios.get('http://127.0.0.1:4523/mock/831624/profile/my_post', {
      email: this.$route.params.email
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

</style>