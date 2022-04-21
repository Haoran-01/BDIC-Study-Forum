<template>
  <div class="courseCard">
    <div class="colorBar"> </div>
    <div class="subjectTitle"> Subject</div>
    <div class="classRoom">
    Classroom:<br>
      <span Style="font-weight: bold;">Building 4 614</span>
    </div>
    <div class="lecture">
    Lecturer:<br>
      <span Style="font-weight: bold;">Sean Russel</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "courseCard"
}
</script>

<style scoped>
.courseCard {
  height: 130px;
  width: 200px;
  display: grid;
  grid-template-columns: 1fr repeat(2, 13px) 10px 170px 1fr;
  grid-template-rows: 0 11px 22px 12px 30px 12px 30px 12px 0;
  grid-column-gap: 0px;
  grid-row-gap: 0px;

  position: relative;
  top: 250px;
  left: 550px;

  background-color: white;
  border-radius: 10px;
  box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.15);

  text-align:left;
}

.colorBar {
  grid-area: 2 / 3 / 9 / 4;
  background-color: red;
}
.subjectTitle {
  grid-area: 3 / 5 / 4 / 6;

  font-family: 'Arial Rounded MT',sans-serif;
  font-style: normal;
  font-size: 22px;

  color: #000000;
}
.classRoom {
  grid-area: 5 / 5 / 6 / 6;
}
.lecture {
  grid-area: 7 / 5 / 8 / 6;
}
</style>