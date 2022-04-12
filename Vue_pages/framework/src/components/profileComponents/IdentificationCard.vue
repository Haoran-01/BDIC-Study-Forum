<template>
  <div :class="animate" class="Frame">
    <div class="rightBar"></div>
    <div class="informationArea"></div>
    <div class="directionBar">
      <div class="part1"></div>
      <div class="part2">
        <button :class="animateButton" class="SpanButton" @click="HandleClick"></button>
      </div>
      <div class="part3"></div>
    </div>
  </div>
</template>

<script>

export default {
  name: "IdentificationCard",
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
    grid-column-gap: 0px;
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
  }

  .directionBar{
    grid-area: 1 / 3 / 2 / 4;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(3, 1fr);
    grid-column-gap: 0;
    grid-row-gap: 0;
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

  .part2{
    grid-area: 2 / 1 / 3 / 2;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .part3{
    grid-area: 3 / 1 / 4 / 2;
  }
</style>