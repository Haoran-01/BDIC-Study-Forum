<template>
<n-card :bordered="false" style="background-color: rgba(255,255,255,0);">
  <n-card class="welcomeCard" content-style="display:flex; align-items: center; justify-content:space-between">
    <n-avatar
        round
        :size=100
        src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
    />
    <span style="margin-left: 20px; font-size: 22px">Welcome, administrator. Start your work today!</span>
    <div style="height: 100%; display: flex">
    <n-card class="functionEntrance" @click="showUsers" :hoverable="true" content-style="font-size: 20px; display:flex; align-items: center; justify-content:center">
      <span>👨‍🎓<br/>User Management</span>
    </n-card>
    <n-card class="functionEntrance" @click="showPosts" :hoverable="true" content-style="font-size:20px; display:flex; align-items: center; justify-content:center">
      <span>📰<br/>Post Management</span>
    </n-card>
    <n-card class="functionEntrance" @click="showMessages" :hoverable="true" content-style="font-size: 20px; display:flex; align-items: center; justify-content:center; flex-direction: column;">
      <span>📫<br/>Message</span>
      <n-badge :value="messages.length" :max="10" />
    </n-card>
    </div>
  </n-card>
</n-card>
<n-card :bordered="false" style="background-color: rgba(255,255,255,0)">
  <n-grid :cols="3" x-gap="12" y-gap="12">
    <n-gi>
      <n-card class="dataShow">
        <n-statistic label="Registration Number">
          <n-number-animation ref="numberAnimationInstRef" :from="0" :to="registration_numbers" />
        </n-statistic>
      </n-card>
    </n-gi>
    <n-gi>
      <n-card>
        <n-statistic label="Post Gross Number">
          <n-number-animation ref="numberAnimationInstRef" :from="0" :to="gross_post_numbers" />
        </n-statistic>
        <n-statistic label="Number of Post Today">
          <n-number-animation ref="numberAnimationInstRef" :from="0" :to="today_post_num" />
        </n-statistic>
      </n-card>
    </n-gi>
    <n-gi>
      <n-card>
        <n-statistic label="Comment Gross Number">
          <n-number-animation ref="numberAnimationInstRef" :from="0" :to="gross_comment_numbers" />
        </n-statistic>
        <n-statistic label="Number of Comment Today">
          <n-number-animation ref="numberAnimationInstRef" :from="0" :to="today_comment_num" />
        </n-statistic>
      </n-card>
    </n-gi>
    <n-gi :span="3">
      <n-card v-if="isUserTableThere" class="table" title="👨‍🎓 User Management">
        <v-grid
            theme="compact"
            :source="userRows"
            :columns="userColumns"
            :resize="true"
            :filter="true"
            :columnTypes = "plugin"
        ></v-grid>
      </n-card>
      <n-card v-if="isPostTableThere" class="table" title="📰 Post Management">
        <v-grid
            theme="compact"
            :source="postRows"
            :columns="postColumns"
            :resize="true"
            :filter="true"
            :columnTypes = "plugin"
        ></v-grid>
      </n-card>
      <n-card v-if="isMessagesThere" class="table" title="📫 Message Management">
        <n-collapse>
        <span v-for="(item, index) in messages" :key="index">
          <n-collapse-item :title=item.messageID :display-directive="show">
            <n-card :bordered="false" size="small" content-style="text-align: left">
              {{ item.messageDetail }}
            </n-card>
            <n-input :value="helpReplies[index].value" type="text" maxlength="100" show-count style="text-align: left; margin: 5px"/>
            <n-button style="float: right; margin: 5px" @click="handleSubmit(index)" :disabled="replyButtons[index]">Submit</n-button>
            <template #header-extra>
              {{ item.messageTime }}
            </template>
          </n-collapse-item>
        </span>
        </n-collapse>
      </n-card>
    </n-gi>
  </n-grid>
</n-card>
</template>

<script>
import NumberColumnType from '@revolist/revogrid-column-numeral';
import SelectTypePlugin from "@revolist/revogrid-column-select";
import VGrid, {VGridVueTemplate}from "@revolist/vue3-datagrid"
import store from "../store/index";
import {toRaw} from "vue";
import deleteButton from "@/components/controlComponents/deleteButton";
import postButton from "@/components/controlComponents/postButton";
import axios from "axios";
import {useToast} from "vue-toastification";
export default {
  components:{VGrid},
  name: "controlBoardView",
  setup(){
    const tip = useToast();
    return {tip};
  },
  data(){
    return{
      registration_numbers: null,
      gross_comment_numbers: null,
      today_comment_num: null,
      gross_post_numbers:null,
      today_post_num: null,
      isUserTableThere: false,
      isPostTableThere: false,
      isMessagesThere: false,
      plugin : {'currency': new NumberColumnType('$0,0.00'), 'num': new NumberColumnType('0'), 'select': new SelectTypePlugin()},
      userColumns: [
        { name: "user email", prop: "user_email", size: 400, sortable: true},
        { name: "name", prop: "name", size: 400, sortable: true},
        { name: "action", cellTemplate: VGridVueTemplate(deleteButton)}
      ],
      userRows: [
        {
          user_email: "zzy@ucd.ie",
          name: "Zhou Zhongyang",
        },
        {
          user_email: "xwb@ucd.ie",
          name: "Xie Wenbei",
        },
        {
          user_email: "ldl@ucd.ie",
          name: "Liu Donglin",
        },
      ],
      postColumns: [
        { name: "post id", prop: "post_id", size: 100, sortable: true, filter: 'number',columnType: "num"},
        { name: "post title", prop: "post_title", size: 400, sortable: true},
        { name: "section", prop: "section", size: 200, sortable: true},
        { name: "delete", cellTemplate: VGridVueTemplate(deleteButton)},
        { name: "post", cellTemplate: VGridVueTemplate(postButton)}
      ],
      postRows: [
        {
          post_id: "1",
          post_title: "fdsfefes",
          section: "Lost & Found"
        },
        {
          post_id: "2",
          post_title: "fdsfsf",
          section: "Lost & Found"
        },
        {
          post_id: "3",
          post_title: "egewefs",
          section: "Lost & Found"
        },
      ],
      messages: [
        {
          messageID: "Liudonglin",
          messageTime: "2022.5.23",
          messageDetail: "wonendie"
        }
      ],
      helpReplies: [

      ],
      replyButtons:[]
    }
  },
  created() {

    axios.get('/adm')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            if (!response.data.data){
              window.location.assign(window.location.origin + '/user/login');
            }
          }
        })
    for (let i = 0; i < this.messages.length; i++){
      this.helpReplies.push({index: i, value: null});
      this.replyButtons.push(false);
    }
    axios.get('/adm/today_comment')
    .then((response)=>{
      const code = response.status;
      if (code === 200){
        this.today_comment_num = response.data.today_comment_num;
      }
    });
    axios.get('/adm/today_post')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.today_post_num = response.data.today_post_num;
          }
    });
    axios.get('/adm/post')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.postRows = response.data.data;
          }
        });
    axios.get('/adm/users')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.userRows = response.data.data;
          }
        });
    axios.get('/adm/registration')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.registration_numbers = response.data.registration_numbers;
          }
        });
    axios.get('/adm/gross_post')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.gross_post_numbers = response.data.gross_post_numbers;
          }
        });
    axios.get('/adm/gross_comment')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.gross_comment_numbers = response.data.gross_comment_numbers;
          }
        });
  },
  methods:{
    showUsers(){
      this.isPostTableThere=false;
      this.isMessagesThere=false;
      this.isUserTableThere=true;
    },
    showPosts(){
      this.isPostTableThere=true;
      this.isMessagesThere=false;
      this.isUserTableThere=false;
    },
    showMessages(){
      this.isPostTableThere=false;
      this.isMessagesThere=true;
      this.isUserTableThere=false;
    },
    handleSubmit(index){
      axios.post('', this.helpReplies[index].value)
      .then((response)=>{
        const code = response.status;
        if (code === 200){
          this.tip.info('Reply successfully.');
          this.replyButtons[index] = true;
        }
      })
    },
  },
  computed:{
    deleteUserIndex(){
      return store.state.currentDeleteIndex;
    },
    deletePostIndex(){
      return store.state.currentDeleteIndex;
    },
    postIndex(){
      return store.state.currentPostIndex;
    }
  },
  watch: {
    deleteUserIndex(value, old){
      const newValue = value.value;
      const data = toRaw(this.userRows);
      old;
      if (newValue !== -1){
        let newData = [];
        for (let i = 0; i<data.length; i++){
          if (i !== newValue){
            newData.push(data[i]);
            console.log(i);
          }
        }
        this.userRows = newData;
      }
    },
    deletePostIndex(value, old){
      const newValue = value.value;
      const data = toRaw(this.postRows);
      old;
      if (newValue !== -1){
        let newData = [];
        for (let i = 0; i<data.length; i++){
          if (i !== newValue){
            newData.push(data[i]);
            console.log(i);
          }
        }
        this.postRows = newData;
      }
      axios.post('/adm/post/delete', {
        post_id: data[newValue].post_id
      })
      .then((response)=>{
        const code = response.status;
        if (code === 200){
          this.tip.info("Delete successfully.");
        }
      })
    },
    postIndex(value, old){
      const newValue = value.value;
      const data = toRaw(this.postRows);
      old;
      if (newValue !== -1){
        const postId = data[newValue].post_id;
        this.$router.push({path:'/post',query:{postId:postId}});
      }
    }
  }
}
</script>

<style scoped>
.welcomeCard{
  height: 200px;
  border-radius: 10px;
}
.functionEntrance{
  width: 180px;
  height: 100%;
  margin-left: 20px;
  cursor: pointer;
  border-radius: 10px;
}
template{
  background-color: #f6f6f6;
}
.table{
  max-width: 100%;
  border-radius: 10px;
  height: calc(100vh - 290px - 20px - 200px - 12px);
}
</style>