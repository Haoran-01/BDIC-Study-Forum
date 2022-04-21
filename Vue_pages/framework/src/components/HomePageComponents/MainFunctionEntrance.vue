<template>
  <div class="entrances">
    <router-link class="entrance" id = "forum" to="/forum">
      <div class="entranceText">Forum</div>
    </router-link>
    <router-link class="entrance" id="courseSchedule" to="/course_schedule">
      <div class="entranceText">Course<br/>Schedule</div>
    </router-link>
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
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 15px;
  align-items: center;
  justify-content: center;
  position: relative;
  bottom: 0;
  text-decoration: none;
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.10);
  background-repeat: no-repeat;
  background-size: cover;
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
  color: #ffffff;
  z-index: 2;
}

.entrance::before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  background-color: rgba(0, 0, 0, .5);
  z-index: 1;
  border-radius: 15px;
}

#forum{
  background-image: url("../../../../../templates/dist/images/forum_entrance.png");
}

#courseSchedule{
  background-image: url("../../../../../templates/dist/images/course_schedule_entrance.png");
}

</style>