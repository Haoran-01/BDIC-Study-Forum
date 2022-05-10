<template>
  <n-card style="height: 97px;">
    <div class="roomNumber">
      {{ class_room_number }}<br>
      <img src="../../../../../templates/dist/images/electricityBlack.png" style="width: 12px; height: 15px;"/>{{ plug_number }}
    </div>
    <div class="roomDisplay">
      <n-grid x-gap="10" :cols="6">
        <n-gi>
          <div :class=first_class > <!--使用样式绑定，后端传过来full和empty两种string，绑定到此处 -->
            <div class="text">1 ~ 2</div>
          </div>
        </n-gi>
        <n-gi>
          <div :class=second_class >
            <div class="text">3 ~ 4</div>
          </div>
        </n-gi>
        <n-gi>
          <div :class=third_class >
           <div class="text"> 5 ~ 6</div>
          </div>
        </n-gi>
        <n-gi>
          <div :class=fourth_class >
           <div class="text"> 7 ~ 8</div>
          </div>
        </n-gi>
        <n-gi>
          <div :class=fifth_class >
           <div class="text"> 9 ~ 10</div>
          </div>
        </n-gi>
        <n-gi>
          <div :class=sixth_class >
            <div class="text">11 ~ 12</div>
          </div>
        </n-gi>
      </n-grid>
    </div>
  </n-card>
</template>

<script>
export default {
  name: "RoomSection",
  props: [
    "class_room_number",
    "plug_number",
    "first_class",
    "second_class",
    "third_class",
    "fourth_class",
    "fifth_class",
    "sixth_class"
  ],
}
</script>

<style scoped>
.full {
  font-size: 16px;
  color: #FFFFFF;
  height: 50px;
  font-weight: bold;
  display: flex;
  background-color: #9b9b9b
}
.empty {
  font-size: 16px;
  color: #FFFFFF;
  font-weight: bold;
  height: 50px;
  display: flex;
  background-color: rgba(0, 128, 0, 1);
}
.roomDisplay{
  position: relative;
  left: 40px;
  bottom: 50px;
  width: 855px
}
.roomNumber{
  display: inline;
  font-size: 16px;
  float: left;
}
.text{
  margin: auto;
}

</style>