<template>
  <div class="entrances">
    <router-link class="entrance" to="/forum">
      <div class="entranceText">Forum</div>
    </router-link>
    <div class="entrance" id="courseSchedule">
      <div class="entranceText">Course<br/>Schedule</div>
    </div>
    <div class="entrance" id="comingSoon">
      <div class="entranceText">Coming<br/>Soon</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainFunctionEntrance"
}
</script>

<style scoped>

.entrances{
  max-width: 1000px;
  width: 100vw;
  height: calc(694px * 0.25 * 5/6);
  display: flex;
  justify-content: space-around;
}
.entrance{
  transition: 0.3s ease-in;
  display: flex;
  width: calc(694px *0.25);
  height: 100%;
  background-color: #00B8FF;
  border-radius: 15px;
  align-items: center;
  justify-content: center;
  position: relative;
  bottom: 0;
  text-decoration: none;
}
.entrance:hover{
  transition: 0.3s ease-out;
  bottom: 2px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
}

.entranceText{
  font-size: 20px;
  font-family: "Noto Sans", sans-serif;
  font-weight: bold;
  color: #000;
}

</style>