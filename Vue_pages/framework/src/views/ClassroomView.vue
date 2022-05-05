<template>
  <div class="Classroom">
    <div class="ClassroomCover">
      <div class="CoverTitle">
        Search empty room
      </div>
    </div>
    <div class="InputSearch"></div>
    <div class="ClassroomDisplay"></div>
  </div>
</template>

<script>
export default {
  name: "ClassroomView"
}
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