<template>
  <div class="navigator">
    <NavigatorBar></NavigatorBar>
  </div>

</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body{
  background-color: #D6E5EB;
  padding: 0;
  margin: 0;
}
</style>
<script>
import NavigatorBar from "@/components/generalComponents/NavigatorBar";
export default {
  components: {NavigatorBar}
}
</script>