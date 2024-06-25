<template>
  <div class="main-page">
    <CheckChart :humanPercent="human" :machinePercent="machine" />
  </div>
</template>

<script>
import CheckChart from "../components/main-page/CheckChart.vue";
export default {
  components: {
    CheckChart,
  },
  data() {
    return {
      human: 60.0,
      machine: 40.0,
    };
  },
};
</script>