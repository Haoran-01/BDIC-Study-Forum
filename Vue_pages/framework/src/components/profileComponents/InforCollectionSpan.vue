<template>
  <div class="Span">
    <div class="header">
      <UsernameForm :infor-msg="Username" EditName="Edit your user name" @SubmitUsername="handleUsername"></UsernameForm>
      <div class="title">Introduction</div>
      <div class="line"></div>
    </div>
    <div class="content">
      <IntroForm :infor-msg="Intro" EditName="Add your personalities" @SubmitIntro="handleIntro"></IntroForm>
      <div class="Ti contentText">E-mail</div>
      <div class="line"></div>
      <div class="e-mail contentText">{{UserEmail}}</div>
      <div class="Ti contentText">Grade</div>
      <div class="line"></div>
      <GradeForm :infor-msg="Grade" EditName="Edit your grade" @SubmitGrade="handleGrade"></GradeForm>
      <div class="Ti contentText">Department</div>
      <div class="line"></div>
      <DepartmentForm :infor-msg="Department" EditName="Edit your department" @SubmitDepartment="handleDepartment"></DepartmentForm>
      <div class="Ti contentText">Major</div>
      <div class="line"></div>
      <MajorForm :infor-msg="Major" EditName="Edit your major" @SubmitMajor="handleMajor"></MajorForm>
    </div>
  </div>
</template>

<script>
import UsernameForm from "@/components/profileComponents/profileForms/UsernameForm";
import IntroForm from "@/components/profileComponents/profileForms/IntroForm";
import GradeForm from "@/components/profileComponents/profileForms/GradeForm";
import DepartmentForm from "@/components/profileComponents/profileForms/DepartmentForm";
import MajorForm from "@/components/profileComponents/profileForms/MajorForm";
import axios from "axios";
export default {
  name: "InforCollectionSpan",
  components: {UsernameForm,IntroForm,GradeForm,DepartmentForm,MajorForm},
  data(){
    return{
      Username:'',
      Intro:'',
      Grade:'',
      Department:'',
      Major:'',
      UserEmail:''
    }
  },
  methods:{
    handleUsername(Submit){
      this.Username = Submit;
      axios.post('/profile',{
        user_name:this.Username,
        introduction:this.Intro,
        grade:this.Grade,
        major:this.Major,
        department:this.Department,
        user_email:this.UserEmail
      }).then((response) => {
        console.log(response);
      }).catch((error) => {
        console.log(error);
      })
    },
    handleIntro(Submit){
      this.Intro = Submit;
      axios.post('/profile',{
        user_name:this.Username,
        introduction:this.Intro,
        grade:this.Grade,
        major:this.Major,
        department:this.Department,
        user_email:this.UserEmail
      }).then((response) => {
        console.log(response);
      }).catch((error) => {
        console.log(error);
      })
    },
    handleGrade(Submit){
      this.Grade = Submit;
      axios.post('/profile',{
        user_name:this.Username,
        introduction:this.Intro,
        grade:this.Grade,
        major:this.Major,
        department:this.Department,
        user_email:this.UserEmail
      }).then((response) => {
        console.log(response);
      }).catch((error) => {
        console.log(error);
      })
    },
    handleDepartment(Submit){
      this.Department = Submit;
      axios.post('/profile',{
        user_name:this.Username,
        introduction:this.Intro,
        grade:this.Grade,
        major:this.Major,
        department:this.Department,
        user_email:this.UserEmail
      }).then((response) => {
        console.log(response);
      }).catch((error) => {
        console.log(error);
      })
    },
    handleMajor(Submit){
      this.Major = Submit;
      axios.post('/profile',{
        user_name:this.Username,
        introduction:this.Intro,
        grade:this.Grade,
        major:this.Major,
        department:this.Department,
        user_email:this.UserEmail
      }).then((response) => {
        console.log(response);
      }).catch((error) => {
        console.log(error);
      })
    }
  },
  created() {
    axios.get('/get_session')
      .then((response) => {
        this.UserEmail=response.data.message;
      })
      .catch(function (error) {
      console.log(error);
    });

    axios.get('/get_profile', {
      params:{
        user_email:this.UserEmail
      }
    })
      .then((response) => {
        this.Username=response.data.user_name;
        this.Intro=response.data.introduction;
        this.Grade=response.data.grade;
        this.Major=response.data.major;
        this.Department=response.data.department;
      })
      .catch(function (error) {
      console.log(error);
    });
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