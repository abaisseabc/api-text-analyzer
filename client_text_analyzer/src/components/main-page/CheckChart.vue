<template>
  <div class="check-chart">
    <highcharts :options="chartOptions"></highcharts>
  </div>
</template>

<script>
export default {
  props: {
    humanPercent: {
      type: Number,
      required: true,
    },
    machinePercent: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      chartOptions: {
        chart: {
          type: "pie",
        },
        title: {
          text: "Результат проверки текста",
        },
        tooltip: {
          valueSuffix: "%",
        },
        plotOptions: {
          series: {
            allowPointSelect: true,
            cursor: "pointer",
            dataLabels: [
              {
                enabled: true,
                distance: 20,
              },
              {
                enabled: true,
                distance: -40,
                format: "{point.percentage:.1f}%",
                style: {
                  fontSize: "1.2em",
                  textOutline: "none",
                  opacity: 0.7,
                },
                filter: {
                  operator: ">",
                  property: "percentage",
                  value: 10,
                },
              },
            ],
          },
        },
        series: [
          {
            name: "Percentage",
            colorByPoint: true,
            data: [
              {
                name: "Человек",
                y: parseFloat(this.humanPercent),
                color: "#B5C5C5",
              },
              {
                name: "Машина или ИИ",
                y: parseFloat(this.machinePercent),
                color: "#2F2B32",
              },
            ],
          },
        ],
      },
    };
  },
};
</script>

<style>
</style>