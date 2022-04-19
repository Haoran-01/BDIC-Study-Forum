<template>
  <div class="Sector">
    <div class="sectorImage">
      <img :src=sector_image_url height="80" width="80"/>
    </div>
    <div class="sectorContent">
      <div class="sectorTitle" Style="font-size:20px; font-weight: bold; text-align:left">{{ type_name }}</div>
      <div class="sectorDetail" Style="text-align:left; position: relative; top: 15px;">
        {{ sector_detail }}
      </div>
    </div>
    <div class="sectorPostImage">
      <img src="../../../../../templates/dist/images/total_post.png" height="40" width="40"/>
    </div>
    <div class="sectorRankImage">
      <img src="../../../../../templates/dist/images/rank.png" height="40" width="40"/>
    </div>
    <div class="sectorPostDetail" >
      <div class="sectorPostOrRankDetail">
        Total Post: {{ total_post }}<br/>
        New Post: {{ today_post }}
      </div>
    </div>
    <div class="sectorRankDetail">
      <div class="sectorPostOrRankDetail">
        Today New Comment: {{ today_comment }}<br/>
        Rank: {{ rank }}
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "SectionEntrance",
  props: [
    "type_name",
    "total_post",
    "today_post",
    "today_comment",
    "rank",
    "sector_image_url",
    "sector_detail"
  ],
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
}
.sectorContent {
  grid-area: 3 / 3 / 6 / 4;

}
.sectorPostImage {
  grid-area: 2 / 4 / 4 / 5;
}
.sectorRankImage {
  grid-area: 5 / 4 / 7 / 5;
}
.sectorPostDetail {
  grid-area: 2 / 5 / 4 / 6;
  font-size: 12px;
  text-align:left;
  display: flex;
  align-items: center;
}
.sectorRankDetail {
  grid-area: 5 / 5 / 7 / 6;
  font-size: 12px;
  text-align:left;
  display: flex;
  align-items: center;
}

</style>