<template>
<div class="menuMain">
  <div class="menuItem">
    <div class="menuItemIcon"></div>
    <router-link class="menuItemText" to="/profile"> Profile </router-link>
  </div>
  <div class="menuItem">
    <div class="menuItemIcon"></div>
    <div class="menuItemText">Log Out</div>
  </div>
</div>
</template>

<script>
export default {
  name: "NavUserMenu"
}
</script>

<style scoped>
.menuMain{
  width: 160px;
  height: auto;
  background-color: #FFFFFF;
  border-radius: 4px;
  border: 1px solid rgba(0, 0, 0, 0.2);
}
.menuItem{
  display: flex;
  width: 100%;
  height: 50px;
  box-sizing: border-box;
  padding-left: 10px;
  padding-right: 10px;
  align-items: center;
}
.menuItemIcon{
  width: 30px;
  height: 30px;
  background-color: #00B8FF;
}
.menuItemText, .menuItemText:visited{
  font-family: "Noto Sans", sans-serif;
  font-weight: normal;
  font-size: 20px;
  margin-left: 20px;
  text-decoration-line: none;
  color: black;
}
</style>