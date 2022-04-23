<template>
    <div class="SeEntrance">
      <div class="Detail">
        <span v-for="(item, index) in items" :key="index">
          <SectionEntrance v-bind="item"></SectionEntrance>
        </span>
      </div>
    </div>
    <div class="ContentFrame">
      <div class="navBar">
          <nav class="nav">


            <div class="girdNav">
              <div class="FirstChoice">
                <div class="choice">
                  <router-link :to="{name:'new',params:this.$route.params.typeName}">New</router-link>
                </div>
                <div class="choice">
                  <router-link :to="{name:'hot',params:this.$route.params.typeName}">Hot</router-link>
                </div>
              </div>
              <div class="blank"></div>
              <div class="PostChoice">
                <div class="choice">
                  <router-link :to="{name:'createPost'}">Post</router-link>
                </div>
              </div>
            </div>


          </nav>
      </div>
      <div class="posts">
        <router-view/>
      </div>
  </div>
</template>

<script>
import axios from "axios";
import SectionEntrance from "@/components/forumComponents/SectionEntrance";
export default {
  name: "InSection",
  components:{SectionEntrance},
  data(){
    return{
      items:[

      ]
    }
  },
  created() {
    axios.get('http://127.0.0.1:4523/mock/831624/forum/section_detail',{
      type_name:this.$route.params.typeName
    }).then((response) => {
      this.items=response.data.data;
    }).catch(function (error) {
      console.log(error);
    });
  }
}
</script>

<style scoped>
  .SeEntrance{
    display: flex;
    justify-content: center;
  }

  .Detail{
    flex-direction: column;
    width: 1000px;
  }

  .navBar{
    grid-area: 1 / 2 / 2 / 3;
    background: #FFFFFF;
    border-radius: 4px;
  }

  .FirstChoice{
    display: flex;
    margin: 0;
    padding: 0;
    grid-area: 1 / 1 / 2 / 2;
  }

  .nav a{
    padding: 5px;
    text-decoration: none;
    border-radius: 8px;
    color: #00B8FF;
  }

  .nav a:hover{
    background-color: #00B8FF;
    color: #FFFFFF;
  }

  .choice{
    margin: 5px;
    padding: 5px;
  }

  .choice a.router-link-exact-active{
    background-color: #00B8FF;
    color: #FFFFFF;
  }

  .posts{
    grid-area: 2 / 2 / 3 / 3;
  }

  .girdNav{
    display: grid;
    grid-template-columns: 250px 650px 1fr;
    grid-template-rows: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 18px;
  }

  .blank{
    grid-area: 1 / 2 / 2 / 3;
  }

  .PostChoice{
    grid-area: 1 / 3 / 2 / 4;
  }

  .ContentFrame{
    display: grid;
    grid-template-columns: 1fr 1000px 1fr;
    grid-template-rows: 40px 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 21px;
  }


</style>