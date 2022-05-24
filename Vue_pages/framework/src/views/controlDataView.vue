<template>
  <n-card :bordered="false" style="background-color: rgba(255,255,255,0);">
    <n-grid :cols="3" x-gap="12" y-gap="12">
      <n-gi>
        <n-card>
            <v-chart class="chart" :option="NPPSD" :autoresize="true" />
        </n-card>
      </n-gi>
      <n-gi>
        <n-card>
          <v-chart class="chart" :option="NCPSD" :autoresize="true" />
        </n-card>
      </n-gi>
      <n-gi>
        <n-card>
          <v-chart class="chart" :option="NOUPSD" :autoresize="true" />
        </n-card>
      </n-gi>
      <n-gi>
        <n-card>
          <v-chart class="chart" :option="NRPSD" :autoresize="true" />
        </n-card>
      </n-gi>
      <n-gi>
        <n-card>
          <v-chart class="chart" :option="PPES" :autoresize="true" />
        </n-card>
      </n-gi>
      <n-gi>
        <n-card title="管理员每日收到信息次数">
          6
        </n-card>
      </n-gi>
      <n-gi>
        <n-card >
          7
        </n-card>
      </n-gi>
    </n-grid>
  </n-card>
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart,LineChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import {defineComponent, ref} from "vue";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent,
  LineChart
]);
export default defineComponent({
  name: "controlDataView",
  components: {
    VChart
  },
  provide: {
    [THEME_KEY]: "light"
  },
  setup() {
    const NPPSD = ref({
      xAxis: {
        data: [1, 2, 3, 4, 5, 6, 7]
      },
      yAxis:{},
      title: {
        text: "Number of Posts Past Seven Days",
        left: "center"
      },
      series: [
        {
          name: "Number of Posts Past Seven Days",
          type: "line",
          data: [23, 44, 11, 22, 41, 48, 20],
          emphasis: {
            label:{
              show: true
            },/*
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)"
            }*/
          }
        }
      ]
    });
    const NCPSD = ref({
      xAxis: {
        data: [1, 2, 3, 4, 5, 6, 7]
      },
      yAxis:{},
      title: {
        text: "Number of Comments Past Seven Days",
        left: "center"
      },
      series: [
        {
          name: "Number of Comments Past Seven Days",
          type: "line",
          data: [23, 44, 11, 22, 41, 48, 20],
          emphasis: {
            label:{
              show: true
            },/*
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)"
            }*/
          }
        }
      ]
    });
    const NOUPSD = ref({
      xAxis: {
        data: [1, 2, 3, 4, 5, 6, 7]
      },
      yAxis:{},
      title: {
        text: "Number of Online Users Past Seven Days",
        left: "center"
      },
      series: [
        {
          name: "Number of Online Users Past Seven Days",
          type: "line",
          data: [23, 44, 11, 22, 41, 48, 20],
          emphasis: {
            label:{
              show: true
            },/*
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)"
            }*/
          }
        }
      ]
    });
    const NRPSD = ref({
      xAxis: {
        data: [1, 2, 3, 4, 5, 6, 7]
      },
      yAxis:{},
      title: {
        text: "Number of Registration Past Seven Days",
        left: "center"
      },
      series: [
        {
          name: "Number of Registration Past Seven Days",
          type: "line",
          data: [23, 44, 11, 22, 41, 48, 20],
          emphasis: {
            label:{
              show: true
            },/*
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)"
            }*/
          }
        }
      ]
    });
    const PPES = ref({
      title: {
        text: "Proportion of Post In Each Section",
        left: "center"
      },
      tooltip: {
        trigger: "item",
        formatter: "{a} <br/>{b} : {c} ({d}%)"
      },
      legend: {
        orient: "horizontal",
        left:'center',
        top: 30,
        data: ["Hot Food", "Clothes", "Tools", "Food Origins", "Snacks"]
      },
      series: [
        {
          name: "Proportion of Post In Each Section",
          type: "pie",
          radius: "55%",
          center: ["50%", "60%"],
          data: [
            { value: 335, name: "Hot Food" },
            { value: 310, name: "Clothes" },
            { value: 234, name: "Tools" },
            { value: 135, name: "Food Origins" },
            { value: 1548, name: "Snacks" }
          ],
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)"
            }
          }
        }
      ]
    });
    return { NPPSD, NCPSD, NOUPSD, NRPSD, PPES };
  }
});
</script>

<style scoped>
.chart{
  height: 400px;
  width: 100%;
}
</style>