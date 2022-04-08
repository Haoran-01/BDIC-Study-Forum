<template>
  <div class="parent">
    <IdentificationCard class="Identify"></IdentificationCard>
    <div class="navigator">
      <nav class="nav">
        <div class="choice">
          <router-link to="/profile/posts">My posts</router-link>
        </div>
        <div class="choice">
          <router-link to="/profile/favourite">My favourite</router-link>
        </div>
      </nav>
    </div>
    <div class="content">
      <router-view/>
    </div>
  </div>
</template>

<script>
import IdentificationCard from "@/components/profileComponents/IdentificationCard";
export default {
  name: "FrameWorkProfile",
  components: {
    IdentificationCard
  }
}

</script>

<style scoped>
  .parent {
    display: grid;
    grid-template-columns: 1fr 694px 1fr;
    grid-template-rows: 155px 5vh 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 15px;
  }

  .Identify { grid-area: 1 / 2 / 2 / 3; }

  .navigator {
    grid-area: 2 / 2 / 3 / 3;
    background: linear-gradient(90.17deg, #00B8FF 0%, #FFFFFF 100%);
    border-radius: 4px;
  }
  .nav{
    display: flex;
    margin: 0;
    padding: 0;
  }

  .nav a{
    padding: 5px;
    text-decoration: none;
    border-radius: 8px;
    color: #FFFFFF;
  }


  .nav a:hover{
    background-color: #ffffff;
    color: #00B8FF;
  }

  .content {
    grid-area: 3 / 2 / 4 / 3;
  }

  .choice{
    margin: 5px;
    padding: 5px;
  }

  .choice a.router-link-exact-active{
    background-color: #ffffff;
    color: #00B8FF;
  }

</style>