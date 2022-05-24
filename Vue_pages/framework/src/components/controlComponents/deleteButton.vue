<template>
  <n-popconfirm
      @positive-click="handlePositiveClick"
  >
    <template #trigger>
      <n-button class="button" size="small" quaternary circle>
        ❌
      </n-button>
    </template>
    Are you sure you want to delete this row?
  </n-popconfirm>
</template>

<script>
import {NButton, NPopconfirm} from "naive-ui";
import store from "../../store/index";
import {toRaw} from "vue";
export default {
  props: ["rowIndex", "prop"],
  components: {NButton, NPopconfirm},
  name: "deleteButton",
  methods:{
    handlePositiveClick(){
      const index = toRaw(this.rowIndex);
      let indexMid = index.toString();
      let indexFinal = parseInt(indexMid);
      store.commit("changeCurrentDeletion", indexFinal);
    }
  }
}
</script>

<style scoped>
</style>