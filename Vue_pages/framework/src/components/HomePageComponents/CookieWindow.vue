<template>
<div class="cookieWindow">
  <div class="cookieDecoration"></div>
  <div class="cookieIcon"></div>
  <div class="cookieTexts">
    <span class="cookieText">Cookies help us to provide better service for you. By clicking "I agree", you agree to our use of cookies.</span>
    <a href="" class="cookieProtocol">   Learn More</a>
  </div>
  <button class="cookieAgreeButton" @click="cookieAccepted">
    <span class="cookieAgreeButtonText">I AGREE</span>
  </button>
</div>
</template>

<script>
export default {
  name: "CookieWindow",
  emits: ['removeCookieWindow'],
  methods: {
    cookieAccepted(){
      this.$emit('removeCookieWindow');
    }
  }
}
</script>

<style scoped>
.cookieWindow {
  display: grid;
  grid-template-columns: 15px 100px 1fr 200px;
  grid-template-rows: 1fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;

  width: 1000px;
  height: 90px;
  border-radius: 4px 4px 0 0;
  background-color: white;
  border: 1px solid rgba(0, 0, 0, 0.2);
  align-items: center;
  justify-items: center;
  overflow: hidden;
}

.cookieDecoration {
  grid-area: 1 / 1 / 2 / 2;
  width: 100%;
  height: 100%;
  background-color: #00B8FF;
  margin: 0;
  padding: 0;
  border-radius: 3px 0 0 0;
}
.cookieIcon {
  grid-area: 1 / 2 / 2 / 3;
  background-color: #00B8FF;
  width: 50px;
  height: 50px;
}
.cookieTexts{
  grid-area: 1 / 3 / 2 / 4;
  text-align: left;
}
.cookieText {
  font-size: 20px;
  font-family: "Noto Sans", sans-serif;
}
.cookieProtocol {
  font-family: "Noto Sans", sans-serif;
  font-size: 20px;
  color: black;
  text-decoration: none;
}
.cookieProtocol :visited{
  color: black;
  text-decoration: none;
}
.cookieProtocol :active{
  color: black;
  text-decoration: none;
}
.cookieAgreeButton {
  grid-area: 1 / 4 / 2 / 5;
  width: 100px;
  height: 40px;
  background-color: #00B8FF;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
}
.cookieAgreeButtonText{
  font-size: 20px;
  font-family: "Noto Sans", sans-serif;
  font-weight: bold;
  color: white;
}
</style>