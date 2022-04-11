<template>
  <div :class="animate" class="Frame">
    <div class="rightBar"></div>
    <div class="informationArea">
      <div class="pictureUpload"></div>
      <div class="selfie">
        <transition>
          <InforCollectionSpan v-show="animate.frameSpan"></InforCollectionSpan>
        </transition>
      </div>
      <div class="selfie">
        <transition>
          <InforCollection v-show="animate.frame"></InforCollection>
        </transition>
      </div>
    </div>
    <div class="directionBar">
      <div class="part1">
        <button :class="animateButton" class="SpanButton" @click="HandleClick"></button>
      </div>
      <div class="part2"></div>
    </div>
  </div>
</template>

<script>
import InforCollection from "@/components/profileComponents/InforCollection";
import InforCollectionSpan from "@/components/profileComponents/InforCollectionSpan";
export default {
  name: "IdentificationCard",
  components:{
    InforCollectionSpan,
    InforCollection
  },
  data(){
    return{
      animate:{
        transition: true,
        frame: true,
        frameSpan: false
      },
      animateButton:{
        Rotate:false,
        RotateBack:true
      }
    }
  },
  methods:{
    HandleClick(){
      this.$store.commit("changeSpanState");
      console.log(this.$store.Span);
      this.animate.frame = !this.animate.frame;
      this.animate.frameSpan = !this.animate.frameSpan;
      this.animateButton.Rotate = !this.animateButton.Rotate;
      this.animateButton.RotateBack = !this.animateButton.RotateBack;
    }
  }
}
</script>

<style scoped>
  .Frame{
    margin: 15px auto auto;
    width: 694px;
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
    transition: 1s height ease;
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
    grid-column-gap: 0px;
    grid-row-gap: 0px;
  }

  .pictureUpload{
    grid-area: 1 / 1 / 2 / 2;
  }

  .selfie{
    grid-area: 1 / 2 / 2 / 3;
    transition: 2s ease-in-out;
  }


  .directionBar{
    grid-area: 1 / 3 / 2 / 4;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 0px;
  }

  .SpanButton{
    border-style: none;
    cursor: pointer;
/*    background: url('../../assets/VectorIcon.png') no-repeat;*/
    background-size: 100%;
    width: 25px;
    height: 25px;
    border-radius: 50%;
  }

  .part1{
    grid-area: 1 / 1 / 2 / 2;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .part2{
    grid-area: 2 / 1 / 3 / 2;
  }

  .v-enter-from{
    opacity: 0;
  }

  .v-enter-active{
    transition: opacity 2s ease-out;
  }

  .v-enter-to{
    opacity: 1;
  }


</style>