<template>
  <div class="Sector">
    <div class="sectorImage">
      <img src="../../../../../static/images/letter.png" height="80" width="80"/>
    </div>
    <div class="sectorContent">
      <div class="sectorTitle" Style="font-size:20px; font-weight: bold; text-align:left">Title of this Sector</div>
      <div class="sectorDetail" Style="text-align:left">
          The detail of this sector.The detail of this sector.The detail of this sector.The detail of this sector.The detail of this sector.The detail of this sector.The detail of this sector.The detail of this sector.
      </div>
    </div>
    <div class="sectorPostImage">
      <img src="../../../../../static/images/letter.png" height="40" width="40"/>
    </div>
    <div class="sectorRankImage">
      <img src="../../../../../static/images/letter.png" height="40" width="40"/>
    </div>
    <div class="sectorPostDetail" Style="font-size: 12px; text-align:left">
      Total Post: ???<br/>
      New Post: ???
    </div>
    <div class="sectorRankDetail" Style="font-size: 12px; text-align:left">
      Today New Comment: ???<br/>
      Rank: ???
    </div>
  </div>
</template>

<script>
export default {
  name: "SectionEntrance"
}
</script>

<style scoped>
.Sector {
  background-color: white;
  display: grid;
  grid-template-columns: 10px 80px 644px 40px 160px 10px;
  grid-template-rows: repeat(2, 10px) 30px 20px 30px repeat(2, 10px);
  grid-column-gap: 14px;
  grid-row-gap: 0px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 4px;
}

.sectorImage {
  grid-area: 3 / 2 / 6 / 3;
  background-color: pink; /*测试图片范围使用，最后删掉*/
}
.sectorContent {
  grid-area: 3 / 3 / 6 / 4;

}
.sectorPostImage {
  grid-area: 2 / 4 / 4 / 5;
  background-color: pink; /*测试图片范围使用，最后删掉*/
}
.sectorRankImage {
  grid-area: 5 / 4 / 7 / 5;
  background-color: pink; /*测试图片范围使用，最后删掉*/
}
.sectorPostDetail { grid-area: 2 / 5 / 4 / 6; }
.sectorRankDetail { grid-area: 5 / 5 / 7 / 6; }

</style>