<template>
  <div class="sectionCard">
    <div class="sectionRank">1</div>
    <div class="sectionImage"></div>
    <div class="sectionName">Campus News</div>
    <div class="newComments"> 12 Comments</div>
  </div>
</template>

<script>
export default {
  name: "SectionEntrance"
}
</script>

<style scoped>
  .sectionCard {
    display: grid;
    grid-template-columns: 20px repeat(3, auto) 20px;
    grid-template-rows: 1fr repeat(2, auto) 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    align-items: center;

    width: 100%;
    height: 50px;
    border-bottom: rgba(0, 0, 0, 0.2) solid 1px;
  }

  .sectionRank {
    grid-area: 2 / 2 / 4 / 3;

    font-weight: bold;
  }
  .sectionImage {
    grid-area: 2 / 3 / 4 / 4;
    width: 30px;
    height: 30px;
    background-color: #00B8FF;
    margin: auto;
    border-radius: 50%;
  }
  .sectionName {
    grid-area: 2 / 4 / 3 / 5;
    text-align: left;
    font-family: "Noto Sans", sans-serif;
    font-size: 14px;
  }
  .newComments {
    grid-area: 3 / 4 / 4 / 5;
    text-align: left;
    font-family: "Noto Sans", sans-serif;
    font-size: 14px;
  }
</style>