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
                  <router-link :to="{path:'/sector/new',query:this.$route.query.typeName}" @click="sendSectionRequirement">New</router-link>
                </div>
                <div class="choice">
                  <router-link :to="{path:'/sector/hot',query:this.$route.query.typeName}">Hot</router-link>
                </div>
              </div>
              <div class="blank"></div>
              <div class="PostChoice">
                  <router-link :to="{path:'/create_post'}">Post</router-link>
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
  methods:{
    sendSectionRequirement(){
      this.$store.commit("setCurrentSection", this.item.type_name);
    }
  },
  created() {
    axios.get('/forum/section_detail',{
      params:{
        type_name:this.$route.query.typeName
      }
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
    transition: .2s ease-in;
    display: block;
    text-decoration: none;
    color: #00B8FF;
    padding: 5px;
    width: 50px;
  }

  .choice{
    transition: .2s ease-in;
    margin: 5px;
    width: 70px;
  }

  .choice a:hover{
    transition: .2s ease-out;
    background-color: #00B8FF;
    border-radius: 100px;
    color: #FFFFFF;
  }

  .choice a.router-link-exact-active{
    background-color: #00B8FF;
    color: #FFFFFF;
    display: block;
    width: 50px;
    padding: 5px;
    border-radius: 100px;
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
    align-items: center;
  }

  .blank{
    grid-area: 1 / 2 / 2 / 3;
  }

  .PostChoice{
    transition: .2s ease-in;
    grid-area: 1 / 3 / 2 / 4;
    justify-self: center;
    width: 60px;
    border: 1px solid #00B8FF;
    border-radius: 100px;
  }
  .PostChoice:hover{
    transition: .2s ease-out;
    background-color: #00B8FF;
  }
  .PostChoice:hover a{
    transition: .2s ease-out;
    color: #FFFFFF;
  }

  .ContentFrame{
    display: grid;
    grid-template-columns: 1fr 1000px 1fr;
    grid-template-rows: 40px 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 21px;
  }


</style>