<template>
  <n-layout has-sider>
    <n-layout-sider
        bordered
        :width="200"
        :native-scrollbar="false"
        :inverted="inverted"
        content-style="padding: 10px; height: calc(100vh - 50px); box-shadow: 0 0 50px rgba(0, 0, 0, 0.10); ">
      <n-menu :options="menuOptions" />
    </n-layout-sider>
    <n-layout content-style="background-color: #f6f6f6;">
      <router-view></router-view>
    </n-layout>
  </n-layout>
  <n-modal :show="showModal">
    <n-card
      style="width: 600px"
      title="Please enter the admin password:"
      :bordered="false"
      size="huge"
      role="dialog"
      aria-modal="true"
  >
      <n-input type="password" placeholder="" v-model:value="adminPass"></n-input>
      <n-button style="float: right; display: flex; margin-top: 10px" @click="closeModal">Submit</n-button>
    </n-card>
  </n-modal>
</template>

<script>

import {defineComponent, h, ref} from "vue";
import { RouterLink } from "vue-router";
import axios from "axios";
import {useToast} from 'vue-toastification';

const menuOptions = [
  {
    label: () => h(RouterLink, {
      to: {
        path: "/control/controlBoard"
      }
    }, { default: () => "Control Board" }),
    key: "1",
  },
  {
    label: () => h(RouterLink, {
      to: {
        path: "/control/controlData"
      }
    }, { default: () => "Data Report" }),
    key: "2",
  }
];

export default defineComponent({
  name: "controlNavigator",
  setup() {
    const tip = useToast();
    return {
      showModal: ref(false),
      menuOptions,
      adminPass: ref(null),
      tip
    };
  },
  mounted(){
    this.showModal = true;
    axios.get('/adm')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            if (!response.data.data){
              this.showModal = true;
            }
          }else {
            window.location.assign(window.location.origin + '/user/login');
          }
        })
  },
  methods: {
    closeModal(){
      if (this.adminPass === null || this.adminPass === ''){
        this.tip.error('Password should not be empty.');
      }else {
        axios.post('/adm/password', {
          password: this.adminPass
        })
        .then((response)=>{
          if (response.status === 200){
            this.showModal = false;
          }else {
            this.tip.error("Wrong Password");
            this.adminPass = "";
          }
        })
      }
    }
  }
});
</script>

<style scoped>

</style>