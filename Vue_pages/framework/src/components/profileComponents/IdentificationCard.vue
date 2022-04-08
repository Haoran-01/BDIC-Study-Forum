<template>
  <div class="Frame">
    <div class="rightBar"></div>
    <div class="informationArea"></div>
    <div class="directionBar"></div>
  </div>
</template>

<script>
export default {
  name: "IdentificationCard"
}
</script>

<style scoped>
  .Frame{
    background-color: #FFFFFF;
    border-radius: 4px;
    display: grid;
    grid-template-columns: 2.5vw 1fr 2.5vw;
    grid-template-rows: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 15px;
  }

  .rightBar{
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    grid-area: 1 / 1 / 2 / 2;
    background:
        linear-gradient(176.67deg, rgba(255, 255, 255, 0) -4.42%,
        rgba(121, 218, 255, 0.315625) -4.41%, rgba(0, 184, 255, 0.6) 107.24%);
  }

  .informationArea{
    grid-area: 1 / 2 / 2 / 3;
  }

  .directionBar{
    grid-area: 1 / 3 / 2 / 4;
  }
</style>