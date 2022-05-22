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
</template>

<script>

import {defineComponent, h} from "vue";
import { RouterLink } from "vue-router";

const menuOptions = [
  {
    label: () => h(RouterLink, {
      to: {
        path: "/control/controlBoard"
      }
    }, { default: () => "控制面板" }),
    key: "1",
  },
  {
    label: () => h(RouterLink, {
      to: {
        path: "/control/controlData"
      }
    }, { default: () => "数据报表" }),
    key: "2",
  }
];

export default defineComponent({
  name: "controlNavigator",
  setup() {
    return {
      menuOptions
    };
  }
});
</script>

<style scoped>

</style>