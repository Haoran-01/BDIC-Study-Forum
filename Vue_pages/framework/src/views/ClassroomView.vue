<template>
  <div class="Classroom">
    <div class="ClassroomCover">
      <div class="CoverTitle">
        Search empty room
      </div>
    </div>
    <div class="InputSearch">
      <n-card>
        <n-tabs type="line" animated="true">
          <n-tab-pane name="timeView" tab="Time View">
            <div>
              <n-select placeholder="Floor"
                        v-model:value="value2"
                        :options="options2"
                        clearable="true"
                        style="width: 200px;"/>
              <n-select placeholder="Date"
                        v-model:value="value3"
                        :options="options3"
                        clearable="true"
                        style="width: 200px; position: relative; left: 220px; bottom: 34px"/>
              <n-button color="#00B8FF" style="bottom: 68px; left: 25px">
                Search
              </n-button>
            </div>
            <div style="position: relative; bottom: 25px;">
              <span v-for="(item, index) in postData" :key="index"> <!-- 这个地方是时间视图中，对于每个教室的循环，因为我不知道每一层有几个教室，所以循环postData中的内容，有几个显示几个-->
                <room-section v-bind="item"></room-section>
              </span>
            </div>
          </n-tab-pane>
          <n-tab-pane name="FloorView" tab="Floor View">
            <div>
              <n-select placeholder="Time period"
                        v-model:value="value1"
                        :options="options1"
                        clearable="true"
                        style="width: 200px;"/>
              <n-select placeholder="Date"
                        v-model:value="value3"
                        :options="options3"
                        clearable="true"
                        style="width: 200px; position: relative; left: 220px; bottom: 34px"/>
              <n-button color="#00B8FF" style="bottom: 68px; left: 25px">
                Search
              </n-button>
            </div>
            <n-result status="404" title="太🐕⑧🚹了，不想做了😜" description="Time view又不是不能用">
            </n-result>
          </n-tab-pane>
        </n-tabs>
      </n-card>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import RoomSection from "@/components/classroomComponents/RoomSection";
export default defineComponent({
  components: {RoomSection},
  setup() {
    return {
      value1: ref(null),
      value2: ref(null),
      value3: ref(null),
      options1: [
        {
          label: "Class 1~2",
          value: "firstClass",
        },
        {
          label: "Class 3~4",
          value: "secondClass"
        },
        {
          label: "Class 5~6",
          value: "thirdClass"
        },
        {
          label: "Class 7~8",
          value: "fourthClass"
        },
        {
          label: "Class 9~10",
          value: "fiveClass"
        },
        {
          label: "Class 11~12",
          value: "sixClass"
        }
      ],
      options2: [
        {
          label: "First Flour",
          value: "firstFlour"
        },
        {
          label:"Second Flour",
          value: "secondFlour"
        },
        {
          label:"Three Flour",
          value: "threeFlour"
        },
        {
          label:"Four Flour",
          value: "fourFlour"
        },
        {
          label:"Five Flour",
          value: "fiveFlour"
        },
      ],
      options3: [
        {
          label: "Monday",
          value: "monday",
        },
        {
          label: "Tuesday",
          value: "tuesday"
        },
        {
          label: "Wednesday",
          value: "wednesday"
        },
        {
          label: "Thursday",
          value: "thursday"
        },
        {
          label: "Friday",
          value: "friday"
        }
      ],
    };
  },
  data() {
    return {
      postData:[ // axios请求的数据的示例
        { //教室一
          roomNumber: 222,
          plugNumber: 4,
          firstClass: "full",
          secondClass: "empty",
          thirdClass: "empty",
          fourthClass: "full",
          fifthClass: "full",
          sixthClass: "empty"
        },
        { //教室二
          roomNumber: 1314,
          plugNumber: 1,
          firstClass: "empty",
          secondClass: "empty",
          thirdClass: "full",
          fourthClass: "full",
          fifthClass: "full",
          sixthClass: "full"
        },

      ]
    }
  }
});
</script>

<style scoped>
  .Classroom{
    display: grid;
    grid-template-columns: 1fr 1000px 1fr;
    grid-template-rows: 100px 45px 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 14px;
  }

  .ClassroomCover{
    grid-area: 1 / 2 / 2 / 3;
    background-image: url("../../../../templates/dist/images/ClassroomCover.jpg");
  }

  .InputSearch{
    grid-area: 2 / 2 / 3 / 3;
    background-color: #FFFFFF;
    border-radius: 5px;
  }

  .ClassroomDisplay{
    grid-area: 3 / 2 / 4 / 3;
  }

  .CoverTitle{
    font-size: 28px;
    color: #FFFFFF;
    font-weight: bold;
    text-align: left;
    margin-top: 50px;
    margin-left: 25px;
  }

</style>