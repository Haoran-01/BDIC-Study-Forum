<template>
<div class="navigator-main">
  <div class="logo"></div>
  <nav>
    <router-link class="home" to="/"> Home </router-link>
    <router-link class="profile" to="/profile"> Profile </router-link>
    <router-link class="forum" to="/forum">Forum</router-link>
  </nav>
  <button class="userMenu"></button>
</div>
  <router-view/>
</template>

<script>
export default {
  name: "NavigatorBar"
}
</script>

<style scoped>
.navigator-main{
  display: grid;
  grid-template-columns: 200px 270px 1fr 100px;
  grid-template-rows: 50px;
}

.logo {
  background-color: #2c3e50;
  grid-area: 1 / 1 / 2 / 2;
}

nav {
  grid-area: 1 / 2 / 2 / 3;
  display: flex;
  grid-template-rows: 100%;
  grid-template-columns: repeat(2, 100px);
  padding: 0;
  margin: 0;
  text-align: center;
  align-items: center;
  flex-basis: auto;
  font-family: "Noto Sans", sans-serif;
}

nav a:link, a:visited{
  width: 100px;
  color: #000000;
  text-decoration:none;
}

.userMenu:hover{
  transition: 0.2s;
  box-shadow: 0 0 4px #727272;
}

.userMenu{
  transition: 0.2s;
  z-index: 10;
  background-color: #00B8FF;
  height: 40px;
  margin: 10px;
  grid-area: 1 / 4 / 2 / 5;
  border: none;
  border-radius: 4px;
}

.div3 { grid-area: 1 / 3 / 2 / 4; }
.div4 { grid-area: 1 / 4 / 2 / 5; }
</style>