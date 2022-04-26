<template>
    <div class="Identify">
      <IdentificationCard></IdentificationCard>
    </div>
    <div class="contentFrame">
      <div class="navigator">
        <nav class="nav">
          <div class="choice">
            <router-link :to="{path:'/posts',query:this.$route.params.email}">My posts</router-link>
          </div>
          <div class="choice">
            <router-link :to="{path:'/favourite',query:this.$route.params.email}">My favourite</router-link>
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
  .contentFrame {
    margin-top: 20px;
    display: grid;
    grid-template-columns: 1fr 1000px 1fr;
    grid-template-rows: 40px 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 17px;
  }



  .navigator {
    grid-area: 1 / 2 / 2 / 3; ;
    background: linear-gradient(90.17deg, #00B8FF 0%, #FFFFFF 100%);
    border-radius: 4px;
  }
  .nav{
    display: flex;
  }
  .nav a{
    transition: .2s ease-in;
    display: block;
    text-decoration: none;
    color: #ffffff;
    padding: 5px;
    width: 100px;
  }

  .choice{
    transition: .2s ease-in;
    margin: 5px;
    width: 120px;
  }

  .choice a:hover{
    transition: .2s ease-out;
    background-color: #ffffff;
    border-radius: 120px;
    color: #00B8FF;
  }

  .choice a.router-link-exact-active{
    background-color: #FFFFFF;
    color: #00B8FF;
    display: block;
    width: 100px;
    padding: 5px;
    border-radius: 100px;
  }

  .content {
    grid-area: 2 / 2 / 3 / 3;
  }

</style>