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
          <v-chart class="chart" :option="NRPSD" :autoresize="true" />
        </n-card>
      </n-gi>
      <n-gi>
        <n-card>
          <v-chart class="chart" :option="PPESPSD" :autoresize="true" />
        </n-card>
      </n-gi>
      <n-gi>
        <n-card>
          <v-chart class="chart" :option="PPES" :autoresize="true" />
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
import axios from "axios";

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
    const PPESPSD = ref({
      title: {
        text: "Proportion of Post In Each Section Past Seven Days",
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
    return { NPPSD, NCPSD, NRPSD, PPESPSD, PPES };
  },
  created() {
    axios.get('/adm')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            if (!response.data.data){
              window.location.assign(window.location.origin + '/user/login');
            }
          }
        })
    axios.get('/adm/seven_types')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.PPESPSD.series[0].data = response.data.data;
          }
        });
    axios.get('/adm/seven_comment')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.NCPSD.series[0].data = response.data.data;
          }
        });
    axios.get('/adm/seven_post')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.NPPSD.series[0].data = response.data.data;
          }
        });
    axios.get('/adm/types')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.PPES.series[0].data = response.data.data;
          }
        });
    axios.get('/adm/seven_registration')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.NRPSD.series[0].data = response.data.data;
          }
        });

    axios.get('/adm/type_name')
        .then((response)=>{
          const code = response.status;
          if (code === 200){
            this.PPESPSD.legend.data = response.data.data;
            this.PPES.legend.data = response.data.data;
          }
        });
  }
});
</script>

<style scoped>
.chart{
  height: 500px;
  width: 100%;
}
</style>