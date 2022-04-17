<template>
  <div class="Sector">
    <div class="sectorImage">
      <img :src=sectorCoverImageURL height="80" width="80"/>
    </div>
    <div class="sectorContent">
      <div class="sectorTitle" Style="font-size:20px; font-weight: bold; text-align:left">{{ sectorTitle }}</div>
      <div class="sectorDetail" Style="text-align:left; position: relative; top: 15px;">
        {{ sectorDetail }}
      </div>
    </div>
    <div class="sectorPostImage">
      <img src="../../../../../templates/dist/images/sectorPostImage.png" height="40" width="40"/>
    </div>
    <div class="sectorRankImage">
      <img src="../../../../../templates/dist/images/sectorRankImage.png" height="40" width="40"/>
    </div>
    <div class="sectorPostDetail" >
      <div class="sectorPostOrRankDetail">
        Total Post: {{ totalPost }}<br/>
        New Post: {{ newPost }}
      </div>
    </div>
    <div class="sectorRankDetail">
      <div class="sectorPostOrRankDetail">
        Today New Comment: {{ todayNewComment }}<br/>
        Rank: {{ rank }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SectionEntrance",
  props: [
    // sectionContain: {
    //   type: Object
    // }
      "sectorCoverImageURL",
      "sectorTitle",
      "sectorDetail",
      "totalPost",
      "newPost",
      "todayNewComment",
      "rank"
  ],

  // data() {
  //   return {
  //     /*sectorTitle: this.sectionContent.sectorTitle,
  //     sectorDetail: this.sectionContent.sectorDetail,
  //     sectorPostImageURL: this.sectionContent.sectorPostImageURL,
  //     sectorRankImageURL: this.sectionContent.sectorRankImageURL,
  //     totalPost: this.sectionContent.totalPost,
  //     newPost: this.sectionContent.newPost,
  //     todayNewComment: this.sectionContent.todayNewComment,
  //     rank: this.sectionContent.rank,*/
  //     sectionContent
  //   }
  // },
  //
  // watch:{
  //   'sectionContain': function (val){
  //     this.sectionContent = val;
  //   }
  // }
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