<template>
  <div class="Span">
    <div class="header">
      <div class="Username">UserName</div>
      <div class="title">Introduction</div>
      <div class="line"></div>
    </div>
    <div class="content">
      <div class="intro contentText">SelfIntro</div>
      <div class="Ti contentText">E-mail</div>
      <div class="line"></div>
      <div class="e-mail contentText">2639230771@qq.com</div>
      <div class="Ti contentText">Grade</div>
      <div class="line"></div>
      <div class="grade contentText">2020</div>
      <div class="Ti contentText">Department</div>
      <div class="line"></div>
      <div class="department contentText">BDIC</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InforCollectionSpan"
}
</script>

<style scoped>
  .intro{
    color: #929497;
  }

  .contentText{
    display: flex;
    margin: 13px 0 5px;
    font-size: 15px;
  }

  .Ti{
    font-weight: bold;
  }

  .line{
    display: flex;
    width: 100px;
    height: 0.5px;
    margin: 5px 0;
    padding: 0;
    background-color: #929497;
  }

  .Username{
    font-size: 23px;
    display: flex;
    margin: 30px 0;
  }

  .title{
    font-size: 13px;
    display: flex;
    color: #929497;
    margin: 5px 0;

  }
</style>