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
      <n-badge :value="newMessages.length" :max="10" />
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
            style="height: 95%"
            :source="userRows"
            :columns="userColumns"
            :resize="true"
            :filter="true"
            :columnTypes = "plugin"
        ></v-grid>
        <n-pagination class="tablePages" v-model:page="userPage" :page-count="userTotalPages" @update:page="changeUserPage" show-quick-jumper>
          <template #goto>
            go to
          </template>
        </n-pagination>
      </n-card>
      <n-card v-if="isPostTableThere" class="table" title="📰 Post Management">
        <v-grid
            style="height: 95%"
            theme="compact"
            :source="postRows"
            :columns="postColumns"
            :resize="true"
            :filter="true"
            :columnTypes = "plugin"
        ></v-grid>
          <n-pagination class="tablePages" v-model:page="postPage" :page-count="postTotalPages" @update:page="changePostPage" show-quick-jumper>
            <template #goto>
              go to
            </template>
          </n-pagination>
      </n-card>
      <n-card v-show="isMessagesThere" class="table" title="📫 Message Management" content-style="display: flex;">
        <n-card class="messageCard" title="Waiting for Reply">
          <n-collapse>
            <n-collapse-item v-for="(item, index) in newMessages" :key="index" :title=item.name>
              <n-card :bordered="false" size="small" content-style="text-align: left" style="height: 100px;">
                {{ item.content }}
                <n-input v-model:value="this.helpReplies[index].value" type="text" maxlength="100" show-count style="text-align: left; margin: 5px"/>
                <n-button style="float: right; margin: 5px;" @click="handleSubmit(index)" :disabled="this.replyButtons[index]">Submit</n-button>
              </n-card>
              <template #header-extra>
                {{ item.datetime }}
              </template>
            </n-collapse-item>
          </n-collapse>
        </n-card>
        <n-card class="messageCard" title="Replied">
          {{ this.helpReplies }}
          <n-collapse>
            <n-collapse-item v-for="(item, index) in repliedMessages" :key="index" :title=item.name>
              <n-card :bordered="false" size="small" content-style="text-align: left">
                {{ item.content }}
                <div>
                  <div style="font-weight: bolder">Reply:</div>
                  {{ item.reply }}
                </div>
              </n-card>
              <template #header-extra>
                {{ item.datetime }}
              </template>
            </n-collapse-item>
          </n-collapse>
        </n-card>
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
import {toRaw, ref, defineComponent} from "vue";
import deleteButton from "@/components/controlComponents/deleteButton";
import postButton from "@/components/controlComponents/postButton";
import axios from "axios";
import {useToast} from "vue-toastification";
import muteButton from "@/components/controlComponents/muteButton";
import {NPagination} from "naive-ui";

export default defineComponent({
  components:{VGrid, NPagination},
  name: "controlBoardView",
  setup(){
    const tip = useToast();
    return {
      tip,
      replyButtons: ref([]),
      userPage: ref(1),
      postPage: ref(1),
      userTotalPages: ref(1),
      postTotalPages: ref(1),
      helpReplies: ref([]),
    };
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
        { name: "action", cellTemplate: VGridVueTemplate(muteButton)}
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
      newMessages:[],
      repliedMessages:[]
    }
  },
  created() {
    axios.get('/adm/all_question')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.newMessages = response.data.data2;
            this.repliedMessages = response.data.data1;
            let replies = [];
            let buttons = [];
            for (let i = 0; i < this.newMessages.length; i++){
              replies.push({index: i, value: null});
              buttons.push(false);
            }
            this.replyButtons = buttons;
            this.helpReplies = replies;
          }}
        );
    axios.get('/adm')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            if (!response.data.data){
              window.location.assign(window.location.origin + '/user/login');
            }
          }
        })
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
    axios.get('/adm/post/pages')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.postTotalPages = response.data.pages;
          }
        });
    axios.post('/adm/post', {
      page_number: 1
    })
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.postRows = response.data.data;
          }
        });
    axios.get('/adm/users/pages')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.userTotalPages = response.data.pages;
          }
        });
    axios.post('/adm/users', {
      page_number: 1
    })
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
      if (this.helpReplies[index].value === '' || this.helpReplies[index].value === null){
        this.tip.error('Reply should not be empty.');
      }else {
        axios.post('/adm/reply', {value: this.helpReplies[index].value})
            .then((response)=>{
              const code = response.status;
              if (code === 200){
                this.tip.info('Reply successfully.');
                this.replyButtons[index] = true;
              }
            })
      }
    },
    changeUserPage (page){
      axios.post('/adm/users', {
        page_number: page
      })
          .then((response)=>{
            const code = response.status;
            if (code === 200){
              this.userRows = response.data.data;
            }
          });
    },
    changePostPage (page){
      axios.post('/adm/post', {
        page_number: page
      })
          .then((response)=>{
            const code = response.status;
            if (code === 200){
              this.postRows = response.data.data;
            }
          });
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
/*    deleteUserIndex(value, old){
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
    },*/
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
})
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
.messageCard{
  width: 50%;
  height: 100%;
}
</style>