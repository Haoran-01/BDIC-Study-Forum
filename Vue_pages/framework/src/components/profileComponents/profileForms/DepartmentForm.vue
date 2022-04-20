<template>
  <form class="Field" @submit.prevent>
    <div class="Field-Content">
      <div class="UserContent" v-show="flag">
        <div id="infor">{{inforMsg}}</div>
        <button type="button" class="ButtonEdit"  @click="edit">
          <span class="imgShow">
            <img src="../../../assets/EditIcon.png">
          </span>
          {{EditName}}
        </button>
      </div>
      <div class="Input" v-show="flagEdit">
        <div class="InputArea">
          <input id="UserInput" type="text" v-model="Submit">
        </div>
        <div class="ButtonArea">
          <button type="submit" class="ButtonChoice" @click="submitContent">Save</button>
          <button type="button" class="ButtonChoice" @click="edit">Back</button>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  name: "DepartmentForm",
  props:['EditName', 'inforMsg'],
  emits:['SubmitDepartment'],
  data(){
    return{
      flag:true,
      flagEdit:false,
      Submit: ""
    }
  },
  methods:{
    edit(){
      this.flag=!this.flag;
      this.flagEdit=!this.flagEdit;
    },
    submitContent(){
      this.$emit('SubmitDepartment', this.Submit);
      this.flag=!this.flag;
      this.flagEdit=!this.flagEdit;
    }
  }
}
</script>

<style scoped>

#infor{
  font-size: 15px;
}

.UserContent{
  font-size: 18px;
  display: flex;
}

.Field-Content{
  display: flex;
  margin: 20px 0;
}


.Input{
  display: flex;
}

.ButtonArea{
  display: flex;
}

.ButtonEdit{
  border: none;
  cursor: pointer;
  background-color: white;
  color: #00B8FF;
}

.ButtonChoice{
  height: inherit;
  margin: 0 12px;
  text-align: center;
  border: 1px solid rgba(10, 10, 10, 0.2);
  border-radius: 3px;
  cursor: pointer;
  background-color: white;
  color: #727272;
}

.ButtonChoice:hover{
  border:  1px solid rgba(0, 184, 255, 0.2);
  background-color:#00B8FF;
  color: white;
}

.imgShow img{
  width: 16px;
  height: 16px;
}

.imgShow{
  display: inline-flex;
  align-items: center;
}

.InputArea input{
  border-radius: 2px;
  padding: 2px;
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.InputArea input:focus-visible{
  outline: 1px solid rgba(0, 184, 255, 0.5);
}




</style>