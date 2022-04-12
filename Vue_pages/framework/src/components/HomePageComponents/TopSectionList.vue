<template>
  <div class="topSectionFrame">
    <div class="topSectionListHead">
      <div class="topSectionListIntro">Today’s Top Forum Sections</div>
    </div>
    <div class="topSections">
      <SectionHomeEntrance></SectionHomeEntrance>
    </div>
  </div>
</template>

<script>
import SectionHomeEntrance from "@/components/HomePageComponents/SectionHomeEntrance";
export default {
  name: "TopSectionList",
  components: {SectionHomeEntrance}
}
</script>

<style scoped>
.topSectionFrame {
  display: grid;
  grid-template-columns: 296px;
  grid-template-rows: 80px auto;
  grid-column-gap: 0px;
  grid-row-gap: 0px;

  width: 296px;
  background-color: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.10);
}

.topSectionListHead {
  grid-area: 1 / 1 / 2 / 2;
  height: 100%;
  width: 100%;
  background-color: #00B8FF;
  display: flex;
  align-items: flex-end;
  justify-content: left;
  border-radius: 3px 3px 0 0;
}
.topSectionListIntro{
  font-family: "Noto Sans", sans-serif;
  font-weight: bold;
  font-size: 16px;
  margin-bottom: 10px;
  margin-left: 10px;
}

.topSections { grid-area: 2 / 1 / 3 / 2; }


</style>