<template>
  <div class="forum">
    <div class="mainColumn" id="inputArea">
      <div id="cover">
        <div id="coverTitle">FORUM</div>
      </div>
      <span v-for="(item, index) in items" :key="index">
      <SectionEntrance :sectorCoverImageURL="item.sectorCoverImageURL" :sectorTitle="item.sectorTitle" :sectorDetail="item.sectorDetail" :totalPost="item.totalPost" :newPost="item.newPost" :todayNewComment="item.todayNewComment" :rank="item.rank"/>
    </span>
    </div>

  </div>
</template>

<script>
import SectionEntrance from "@/components/forumComponents/SectionEntrance";
// import axios from "axios";
export default {
  components: { SectionEntrance },
  data() {
    // let msg = {
    // }
    return {
      items: [
        {
          sectorCoverImageURL: require('../../../../static/images/R&Q.jpeg'),
          sectorTitle: "Lecture Question",
          sectorDetail: "This section is used for solving lecture question. You can post your questions encountered in class, and others may help you. You can also assist other if you like.",
          totalPost: 20,
          newPost: 3,
          todayNewComment: 26,
          rank: 1
        },
        {
          sectorCoverImageURL: require('../../../../static/images/Lost&Found.jpeg'),
          sectorTitle: "Lost And Found",
          sectorDetail: "This section is used for Lost and Found. If you lost or found something, you can post its details, thus others may get it and contact you.",
          totalPost: 12,
          newPost: 1,
          todayNewComment: 14,
          rank: 2
        },
        {
          sectorCoverImageURL: require('../../../../static/images/transaction.jpeg'),
          sectorTitle: "Transaction",
          sectorDetail: "This section is used for trading used products. If you need something or want to sell something, just post you requirement and waiting others who need contact you.",
          totalPost: 44,
          newPost: 5,
          todayNewComment: 8,
          rank: 3
        }
      ]
    }
  },
}
// axios.post('/sections', {
//   firstName: 'Fred',
//   lastName: 'Flintstone'
// })
//     .then(function (response) {
//       console.log(response);
//     })
//     .catch(function (error) {
//       console.log(error);
//     });
// axios.get('/sections')
//     .then(function (response) {
//       console.log(response);
//     })
//     .catch(function (error) {
//       console.log(error);
//     });
</script>

<style scoped>
.forum {
  display: flex;
  justify-content: center;
}
.mainColumn{
  flex-direction: column;
  width: 1000px;
}
#cover{
  flex-direction: column;
  width: 1000px;
  height: 100px;
  background-image: url("../../../../static/images/forumCover.png")
}
#coverTitle {
  position: absolute;
  width: 177px;
  height: 58px;
  left: 631px;
  top: 74px;

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 34px;
  line-height: 58px;
  color: #ffffff;
}
</style>

