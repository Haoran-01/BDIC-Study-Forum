<template>
  <div class="postListLogic" v-for="(item, index) in postData" :key="index">
    <post-entrance v-bind="{item, index}" :width="1000" @send-share-info="handleShare"></post-entrance>
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
  name: "NewPosts",
  components: {PostEntrance},
  data(){
    return{
      section: '',
      postData: {}
    }
  },
  methods:{
    handleShare(){
      this.tip.info("Link Copied Successfully");
    }
  },
  created() {
    axios.get('/forum/section/get_new_posts', {
      type_name: this.$route.query.typeName
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
  },
  beforeRouteEnter(to, from, next){
    next(vm =>{
      vm.section = vm.$store.state.currentSection;
    })
  }
}
</script>

<style scoped>

</style>