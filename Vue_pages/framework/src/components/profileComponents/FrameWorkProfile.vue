<template>
  <div class="parent">
    <IdentificationCard class="div1"></IdentificationCard>
    <div class="div2">
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
    grid-template-columns: 1fr 45vw 1fr;
    grid-template-rows: 20vh 5vh 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 15px;
  }

  .div1 { grid-area: 1 / 2 / 2 / 3; }
  .div2 {
    grid-area: 2 / 2 / 3 / 3;
    background: linear-gradient(90.17deg, #00B8FF 0%, #FFFFFF 100%);
    border-radius: 4px;
  }

</style>