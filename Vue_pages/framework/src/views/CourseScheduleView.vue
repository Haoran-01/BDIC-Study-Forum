<template>
<!--  <DndProvider :backend="HTML5Backend">-->
<!--    <Home></Home>-->
<!--  </DndProvider>-->
  <div class="topBar"></div>
  <div class="courseTable">
    <div class="timeSection">
      <div class="div1">
        08:00<br>
        1~2<br>
        09:35
      </div>
      <div class="div2">
        09:55<br>
        3~4<br>
        11:30
      </div>
      <div class="div3">
        13:30<br>
        5~6<br>
        15:05
      </div>
      <div class="div4">
        15:25<br>
        7~8<br>
        17:00
      </div>
      <div class="div5">
        18:00<br>
        9~10<br>
        19:35
      </div>
      <div class="div6">
        19:55<br>
        11~12<br>
        21:30
      </div>
    </div>
    <div class="cardSection">
      <course-board></course-board>
    </div>
    <div class="xingQiJiSection">
      <div class="mon">MON </div>
      <div class="tue"> TUE</div>
      <div class="wed"> WED</div>
      <div class="thu"> THU</div>
      <div class="fri"> FRI</div>
      <div class="line" Style="bottom: 455px;"></div>
      <div class="line" Style="bottom: 325px;"></div>
      <div class="line" Style="bottom: 195px;"></div>
      <div class="line" Style="bottom: 65px;"></div>
      <div class="line" Style="bottom: -65px;"></div>
    </div>
  </div>
  <footer></footer>
</template>

<script>
import CourseBoard from "@/components/courseScheduleComponents/CourseBoard";

export default {
  name: "CourseScheduleView",
  components: {CourseBoard}
}
</script>

<style scoped>
template{
  display: flex;
}
.topBar{
  height: 50px;
}
.courseTable{
  height: 850px;
  width: 1200px;
  margin: auto;

  /*background-color: #f600ff;*/

  display: grid;
  grid-template-columns: 1fr 120px 1080px 200px;
  grid-template-rows: 1fr 70px 780px 1fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
}

.timeSection {
  grid-area: 3 / 2 / 4 / 3;
  text-align: center;
  align-items: center;
  /*color: #9A9A9A;*/
  font-size: 20px;
  font-weight: bold;
  letter-spacing:2px;
  /*background-color: green;*/

  display: grid;
  grid-template-columns: 1fr 120px 1fr;
  grid-template-rows: 1fr repeat(6, 130px) 1fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
}

.div1 { grid-area: 2 / 2 / 3 / 3; }
.div2 { grid-area: 3 / 2 / 4 / 3; }
.div3 { grid-area: 4 / 2 / 5 / 3; }
.div4 { grid-area: 5 / 2 / 6 / 3; }
.div5 { grid-area: 6 / 2 / 7 / 3; }
.div6 { grid-area: 7 / 2 / 8 / 3; }
.cardSection {
  grid-area: 3 / 3 / 4 / 4;
  /*background-color: rebeccapurple;*/
}
.xingQiJiSection {
  grid-area: 2 / 3 / 3 / 4;
  text-align: center;
  align-items: center;
  /*color: #9A9A9A;*/
  font-size: 20px;
  font-weight: bold;
  letter-spacing:2px;
  /*background-color: yellow;*/

  display: grid;
  grid-template-columns: 1fr repeat(5, 216px) 1fr;
  grid-template-rows: 1fr 70px 1fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
}
footer{
  height: 50px;
}

.mon { grid-area: 2 / 2 / 3 / 3; }
.tue { grid-area: 2 / 3 / 3 / 4; }
.wed { grid-area: 2 / 4 / 3 / 5; }
.thu { grid-area: 2 / 5 / 3 / 6; }
.fri { grid-area: 2 / 6 / 3 / 7; }
.line{
  position: absolute;
  background-color: #9A9A9A;
  height: 1px;
  width: 1080px;
  z-index: -1;
}
</style>