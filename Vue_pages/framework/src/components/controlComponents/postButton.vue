<template>
    <n-button class="button" @click="handlePost" size="small" quaternary circle>
      📰
    </n-button>
</template>

<script>
import {NButton} from "naive-ui";
import store from "../../store/index";
import {toRaw} from "vue";
export default {
  props: ["rowIndex", "prop"],
  components: {NButton},
  name: "postButton",
  methods:{
    handlePost(){
      const index = toRaw(this.rowIndex);
      let indexMid = index.toString();
      let indexFinal = parseInt(indexMid);
      store.commit("changeCurrentPost", indexFinal);
    }
  }
}
</script>

<style scoped>
</style>