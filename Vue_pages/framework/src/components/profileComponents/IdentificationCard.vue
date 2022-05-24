<template>
  <div :class="animate" class="Frame">
    <div class="rightBar"></div>
    <div class="informationArea">
      <div class="pictureUpload">
        <img class="Heading" :src="this.profile_url">
        <button type="button" class="changeButton" @click="showModal=true" v-show="IsHost">
          Avatar
        </button>
        <n-modal v-model:show="showModal" class="modal" transform-origin="center">
          <div>
            <CropperImage></CropperImage>
          </div>
        </n-modal>
      </div>
      <div class="Otherselfie" v-if="!IsHost">
        <InforCollection></InforCollection>
      </div>
      <div class="selfie" v-else>
        <transition>
          <InforCollectionSpan v-show="animate.frameSpan"></InforCollectionSpan>
        </transition>
        <transition>
          <InforCollection v-show="animate.frame"></InforCollection>
        </transition>
      </div>
    </div>
    <div class="directionBar" v-show="IsHost">
      <div class="part1">
        <button :class="animateButton" class="SpanButton" @click="HandleClick"></button>
      </div>
    </div>
  </div>
</template>

<script>
import InforCollection from "@/components/profileComponents/InforCollection";
import InforCollectionSpan from "@/components/profileComponents/InforCollectionSpan";
import axios from "axios";
import CropperImage from "@/components/profileComponents/CropperImage";
import 'vue-cropper/dist/index.css';
import '@kouts/vue-modal/dist/vue-modal.css'
import {ref} from "vue";

export default {
  name: "IdentificationCard",
  components:{
    InforCollectionSpan,
    InforCollection,
    CropperImage
  },
  data(){
    return{
      showModal: ref(false),
      animate:{
        transition: true,
        frame: true,
        frameSpan: false
      },
      animateButton:{
        Rotate:false,
        RotateBack:true
      },
      IsHost:true,
      accessEmail:'',
      hostEmail:'',
      profile_url:''
    }
  },
  methods:{
    HandleClick(){
      this.$store.commit("changeSpanState");
      this.animate.frame = !this.animate.frame;
      this.animate.frameSpan = !this.animate.frameSpan;
      this.animateButton.Rotate = !this.animateButton.Rotate;
      this.animateButton.RotateBack = !this.animateButton.RotateBack;
    }
  },
  created() {
    this.hostEmail=this.$route.query.email;
    axios.get('/get_session')
        .then((response) => {
          this.accessEmail=response.data.message;
          console.log(this.hostEmail);
          console.log(this.accessEmail);
          if (this.accessEmail != this.hostEmail){
            this.IsHost=false;
          }else {
            this.IsHost=true;
          }
        })
        .catch(function (error) {
          console.log(error);
        });

    axios.get('/get_profile', {
      params:{
        user_email:this.hostEmail
      }
    })
        .then((response) => {
          this.profile_url=response.data.profile;
        })
        .catch(function (error) {
          console.log(error);
        });
  }
}
</script>

<style scoped>
  .Frame{
    margin: 15px auto auto;
    width: 1000px;
    background-color: #FFFFFF;
    border-radius: 4px;
    display: grid;
    grid-template-columns: 40px 1fr 40px;
    grid-template-rows: 1fr;
    grid-column-gap: 0;
    grid-row-gap: 15px;
    overflow: hidden;
  }

  .transition{
    transition: .5s height ease-in-out;
  }

  .frame{
    height: 155px;
  }

  .frameSpan{
    height: 455px;
  }

  .Rotate{
    transition: all 1s;
    transform: rotate(180deg);
  }

  .RotateBack{
    transition: all 1s;
  }

  .rightBar{
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    grid-area: 1 / 1 / 2 / 2;
    background:
        linear-gradient(176.67deg, rgba(255, 255, 255, 0) -4.42%,
        rgba(121, 218, 255, 0.315625) -4.41%, rgba(0, 184, 255, 0.6) 107.24%);
  }

  .informationArea{
    grid-area: 1 / 2 / 2 / 3;
    display: grid;
    grid-template-columns: 155px 1fr;
    grid-template-rows: 1fr;
    grid-column-gap: 25px;
    grid-row-gap: 0px;
  }

  .pictureUpload{
    grid-area: 1 / 1 / 2 / 2;
  }

  .selfie{
    grid-area: 1 / 2 / 2 / 3;
  }

  .SpanButton{
    border-style: none;
    cursor: pointer;
    background: url('../../../../../templates/dist/images/VectorIcon.png') no-repeat;
    background-size: 100%;
    width: 25px;
    height: 25px;
    border-radius: 50%;
  }

  .part1{
    margin: 70px auto;
  }

  .v-enter-from{
    opacity: 0;
  }

  .v-enter-active{
    transition: opacity 1.5s ease-out;
  }

  .v-enter-to{
    opacity: 1;
  }

  .changeButton{
    transition: 0.5s ease-in;
    background-color: rgba(92, 92, 184, 0);
    height: 30px;
    width: 60px;
    cursor: pointer;
    font-weight: bold;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 10px;
  }

  .changeButton:hover{
    background-color: #00B8FF;
    color: #FFFFFF;
  }

  .Heading{
    width: 100px;
    height: 100px;
    margin-top: 10px;
    margin-bottom: 5px;
    box-shadow: 0 0 3px #727272;
    border-radius: 100px;
  }

  .modal{
    background-color: #FFFFFF;
    padding: 0 20px 20px 20px;
    justify-content: center;
    border-radius: 10px;
  }


</style>