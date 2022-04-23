<template>
  <div class="forum">
    <div class="mainColumn" id="inputArea">
      <div id="cover">
        <div id="coverTitle">FORUM</div>
      </div>
      <span v-for="(item, index) in items" :key="index">
        <SectionEntrance v-bind="item"></SectionEntrance>
    </span>
    </div>

  </div>
</template>

<script>
import SectionEntrance from "@/components/forumComponents/SectionEntrance";
import axios from "axios";
export default {
  components: { SectionEntrance },
  data() {
    return {
      items: [
        {
          sectorCoverImageURL: require('../../../../templates/dist/images/R&Q.jpeg'),
          sectorTitle: "Lecture Question",
          sectorDetail: "This section is used for solving lecture question. You can post your questions encountered in class, and others may help you. You can also assist other if you like.",
          totalPost: 20,
          newPost: 3,
          todayNewComment: 26,
          rank: 1
        },
        {
          sectorCoverImageURL: require('../../../../templates/dist/images/Lost&Found.jpeg'),
          sectorTitle: "Lost And Found",
          sectorDetail: "This section is used for Lost and Found. If you lost or found something, you can post its details, thus others may get it and contact you.",
          totalPost: 12,
          newPost: 1,
          todayNewComment: 14,
          rank: 2
        },
        {
          sectorCoverImageURL: require('../../../../templates/dist/images/transaction.jpeg'),
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
  created() {
    axios.get('http://127.0.0.1:4523/mock/831624/forum/sections')
        .then((response) => {
          this.items = response.data.data;
          console.log(response);
          console.log(this.items);
        })
        .catch(function (error) {
          console.log(error);
        })
  },
}
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
  background-image: url("../../../../templates/dist/images/forumCover.png");
  position: relative;
}
#coverTitle {
  position: absolute;
  width: 177px;
  height: 58px;
  left: calc(500px - 177px/2);
  top: calc(50px - 48px/2);

  font-family: 'Inter', Sans-Serif;
  font-style: normal;
  font-weight: 700;
  font-size: 34px;
  line-height: 58px;
  color: #ffffff;
}
</style>

