<template>
<n-card :bordered="false" style="height: 200px; background-color: rgba(255,255,255,0)">
  <n-card class="welcome" >
    <span style="font-size: 24px">Welcome administrator!</span>
  </n-card>
</n-card>
<n-card :bordered="false" style="background-color: rgba(255,255,255,0)">
  <n-grid :cols="3" x-gap="12" y-gap="12">
    <n-gi>
      <n-card class="dataShow">
        <n-statistic label="本站注册人数">
          1,234,123
        </n-statistic>
        <n-statistic label="当前在线人数">
          1,234
        </n-statistic>
      </n-card>
    </n-gi>
    <n-gi>
      <n-card>
        <n-statistic label="本站帖子总数">
          100000
        </n-statistic>
        <n-statistic label="今日发帖数量">
          100
        </n-statistic>
      </n-card>
    </n-gi>
    <n-gi>
      <n-card>
        <n-statistic label="本站帖子总数">
          100000
        </n-statistic>
        <n-statistic label="今日发帖数量">
          100
        </n-statistic>
      </n-card>
    </n-gi>
    <n-gi>
      <n-card>
        <n-statistic label="管理员待处理信息">
          100
        </n-statistic>
      </n-card>
    </n-gi>
  </n-grid>
</n-card>
</template>

<script>
export default {
  name: "controlBoardView"
}
</script>

<style scoped>
.welcome{
  width: 350px;
  position: relative;
  left: 100px;
  top: 50px;
  font-family: "Comic Sans MS", serif;
}
template{
  background-color: #f6f6f6;
}
</style>