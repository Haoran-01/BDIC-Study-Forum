<template>
<n-card :bordered="false" style="background-color: rgba(255,255,255,0)">
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
      <n-badge :value="10" :max="10" />
    </n-card>
    </div>
  </n-card>
</n-card>
<n-card :bordered="false" style="background-color: rgba(255,255,255,0)">
  <n-grid :cols="3" x-gap="12" y-gap="12">
    <n-gi>
      <n-card class="dataShow">
        <n-statistic label="Registration Number">
          <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12039" />
        </n-statistic>
        <n-statistic label="Current Online Population">
          <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12039" />
        </n-statistic>
      </n-card>
    </n-gi>
    <n-gi>
      <n-card>
        <n-statistic label="Post Gross Number">
          <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12039" />
        </n-statistic>
        <n-statistic label="Number of Post Today">
          <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12039" />
        </n-statistic>
      </n-card>
    </n-gi>
    <n-gi>
      <n-card>
        <n-statistic label="Comment Gross Number">
          <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12039" />
        </n-statistic>
        <n-statistic label="Number of Comment Today">
          <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12039" />
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
          <n-collapse-item :title=item.messageID>
            <n-card :bordered="false" size="small" content-style="text-align: left">
              {{ item.messageDetail }}
            </n-card>
            <n-input type="text" maxlength="100" show-count style="text-align: left; margin: 5px"/>
            <n-button style="float: right; margin: 5px">Submit</n-button>
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
export default {
  components:{VGrid},
  name: "controlBoardView",
  data(){
    return{
      isUserTableThere: false,
      isPostTableThere: false,
      isMessagesThere: false,
      plugin : {'currency': new NumberColumnType('$0,0.00'), 'num': new NumberColumnType('0'), 'select': new SelectTypePlugin()},
      userColumns: [
        { name: "user email", prop: "user_email", size: 400, sortable: true},
        { name: "name", prop: "user_name", size: 400, sortable: true},
        { name: "action", cellTemplate: VGridVueTemplate(deleteButton)}
      ],
      userRows: [
        {
          user_email: "zzy@ucd.ie",
          user_name: "Zhou Zhongyang",
        },
        {
          user_email: "xwb@ucd.ie",
          user_name: "Xie Wenbei",
        },
        {
          user_email: "ldl@ucd.ie",
          user_name: "Liu Donglin",
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
      ]
    }
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
    }
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
      console.log(newValue);
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
      console.log(newValue);
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
  height: calc(100vh - 290px - 20px - 200px - 12px);
}
</style>