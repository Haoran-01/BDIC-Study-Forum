<template>
  <div class="navigator">
    <n-config-provider :locale="zhCN" :date-locale="dateZhCN" :theme-overrides="themeOverrides">
      <NavigatorBar></NavigatorBar>
    </n-config-provider>
  </div>

</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body{
  background-color: #D6E5EB;
  padding: 0;
  margin: 0;
}
</style>
<script>
import { defineComponent } from 'vue'
import NavigatorBar from "@/components/generalComponents/NavigatorBar";
import {dateZhCN, NConfigProvider, zhCN} from "naive-ui";
import('naive-ui').GlobalThemeOverrides;

const themeOverrides = {
  common: {
    primaryColor: '#00B8FF',
    primaryColorHover: '#00B8FF'
  },
  Button: {
    textColor: '#00B8FF'
  },
  Select: {
    peers: {
      InternalSelection: {
        textColor: '#00B8FF'
      }
    }
  },
}
export default defineComponent({
  components: {NavigatorBar,NConfigProvider},
  setup() {
    return {
      zhCN,
      dateZhCN,
      themeOverrides
    }
  }
})
</script>