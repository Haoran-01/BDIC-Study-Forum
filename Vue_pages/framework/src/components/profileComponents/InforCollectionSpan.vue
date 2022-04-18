<template>
  <div class="Span">
    <div class="header">
      <ProfileForm EditName="Edit your user name"></ProfileForm>
      <div class="title">Introduction</div>
      <div class="line"></div>
    </div>
    <div class="content">
      <ProfileForm EditName="Add your personalities"></ProfileForm>
      <div class="Ti contentText">E-mail</div>
      <div class="line"></div>
      <div class="e-mail contentText">2639230771@qq.com</div>
      <div class="Ti contentText">Grade</div>
      <div class="line"></div>
      <ProfileForm EditName="Edit your grade"></ProfileForm>
      <div class="Ti contentText">Department</div>
      <div class="line"></div>
      <ProfileForm EditName="Edit your department"></ProfileForm>
      <div class="Ti contentText">Major</div>
      <div class="line"></div>
      <ProfileForm EditName="Edit your major"></ProfileForm>
    </div>
  </div>
</template>

<script>
import ProfileForm from "@/components/profileComponents/ProfileForm";
export default {
  name: "InforCollectionSpan",
  components: {ProfileForm},
  data(){
    return{
      Email:''
    }
  }
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


  .title{
    font-size: 13px;
    display: flex;
    color: #929497;
    margin: 5px 0;

  }
</style>