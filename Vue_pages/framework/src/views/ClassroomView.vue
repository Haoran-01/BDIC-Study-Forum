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
              <n-button color="#00B8FF" style="bottom: 68px; left: 115px" @click="handleSearch">
                Search
              </n-button>
              <n-switch
                :rail-style="railStyle"
                style="position: relative; bottom: 68px; left: 345px;"
                size="large"
                v-model:value="active"
                @update:value="handleChangeSort"
              >
                <template #checked>
                  Sort by usable time
                </template>
                <template #unchecked>
                  Sort by room number
                </template>
              </n-switch>
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
import {defineComponent, ref, shallowRef} from "vue";
import RoomSection from "@/components/classroomComponents/RoomSection";
import axios from "axios";
import {useToast} from "vue-toastification";
export default defineComponent({
  components: {RoomSection},
  setup() {
    const tip = useToast();
    return {
      tip,
      value1: ref(null),
      value2: ref(null),
      value3: ref(null),
      options1: [
        {
          label: "Class 1~2",
          value: 0,
        },
        {
          label: "Class 3~4",
          value: 1
        },
        {
          label: "Class 5~6",
          value: 2
        },
        {
          label: "Class 7~8",
          value: 3
        },
        {
          label: "Class 9~10",
          value: 4
        },
        {
          label: "Class 11~12",
          value: 5
        }
      ],
      options2: [
        {
          label: "First Floor",
          value: 1
        },
        {
          label:"Second Floor",
          value: 2
        },
        {
          label:"Three Floor",
          value: 3
        },
        {
          label:"Four Floor",
          value: 4
        },
        {
          label:"Five Floor",
          value: 5
        },
      ],
      options3: [
        {
          label: "Monday",
          value: 0
        },
        {
          label: "Tuesday",
          value: 1
        },
        {
          label: "Wednesday",
          value: 2
        },
        {
          label: "Thursday",
          value: 3
        },
        {
          label: "Friday",
          value: 4
        },
        {
          label: "Saturday",
          value: 5
        },
        {
          label: "Sunday",
          value: 6
        }
      ],
      active: ref(false),
      handleChangeSort(value){
        if (value === false){
          axios.post("/search_empty_class/time_view", {
            floor: this.value2,
            date: this.value3,
            sort: 'room'
          })
              .then((response)=>{
                const code = response.status;
                if (code === 200){
                  this.postData = shallowRef(response.data.data);
                }
              })
        }
        else {
          axios.post("/search_empty_class/time_view", {
            floor: this.value2,
            date: this.value3,
            sort: 'time'
          })
              .then((response)=>{
                const code = response.status;
                if (code === 200){
                  this.postData = shallowRef(response.data.data);
                }
              })
        }
      },
      railStyle: ({
                    focused,
                    checked
                  }) => {
        const style = {};
        if (checked) {
          style.background = "#00B8FF";
          if (focused) {
            style.boxShadow = "0 0 0 2px #2080f040";
          }
        } else {
          style.background = "#00B8FF";
          if (focused) {
            style.boxShadow = "0 0 0 2px #2080f040";
          }
        }
        return style;
      }
    };
  },
  data() {
    return {
      postData:[ // axios请求的数据的示例
/*        { //教室一
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
        },*/

      ]
    }
  },
  methods: {
    handleSearch(){
      if (this.value2 === null || this.value3 === null){
        this.tip.error("The choices should not be blank");
      }else {
        axios.post("/search_empty_class/time_view", {
          floor: this.value2,
          date: this.value3
        })
            .then((response)=>{
              const code = response.status;
              if (code === 200){
                this.postData = shallowRef(response.data.data);
              }
            })
      }
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