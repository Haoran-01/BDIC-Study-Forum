<template>
  <n-card :bordered="false" style="background-color: rgba(255,255,255,0)">
    <n-grid :cols="3" x-gap="12" y-gap="12">
      <n-gi>
        <n-card title="近七日发帖数量">
          1
        </n-card>
      </n-gi>
      <n-gi>
        <n-card title="近七日上线人数">
          2
        </n-card>
      </n-gi>
      <n-gi>
        <n-card title="近七日新注册人数">
          3
        </n-card>
      </n-gi>
      <n-gi>
        <n-card title="各section的发帖数量">
          4
        </n-card>
      </n-gi>
      <n-gi>
        <n-card title="各section发帖数量占比">
          5
        </n-card>
      </n-gi>
      <n-gi>
        <n-card title="管理员每日收到信息次数">
          6
        </n-card>
      </n-gi>
      <n-gi>
        <n-card >
          7
        </n-card>
      </n-gi>
    </n-grid>
  </n-card>
</template>

<script>
export default {
  name: "controlDataView"
}
</script>

<style scoped>

</style>