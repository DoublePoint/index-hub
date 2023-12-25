<template>
  <!-- 柱形图+折线图多个展示 -->
  <div>
    <div class="title">
      <span>百度指数</span>
    </div>
    <div class="chart" v-loading="loading" element-loading-text="拼命加载中" element-loading-spinner="el-icon-loading"
      element-loading-background="rgba(0, 0, 0, 0.8)" id="myMaxbar" :style="{ width: '100%', height: '300px' }">
    </div>
  </div>
</template>
  
<script>
import echarts from 'echarts'
import { getBaiduIndex } from '@/api/index-hub/index-main.js'
require('echarts/theme/macarons') // echarts theme
export default {
  data() {
    return {
      searchIndex: "",
      loading: true,
    };
  },
  mounted() {
    this.drawLine();
    this.loading = false
  },
  computed: {
    indexName() {
      return this.$store.state.indexes.indexName;
    },
    startDate() {
      return this.$store.state.indexes.startDate;
    },
    endDate() {
      return this.$store.state.indexes.endDate;
    }
  },
  watch: {
    indexName(val) {
      //debugger
      this.drawLine();
    },
    startDate() {
      this.drawLine();
    },
    endDate() {
      this.drawLine();
    }
  },
  methods: {
    drawLine() {
      this.loading = true;
      const formatDate = date => `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;
      // 输出日志
      // console.log(`今天的日期是：${formatDate(today)}`);
      // console.log(`七天前的日期是：${formatDate(sevenDaysAgo)}`);
      if (this.indexName == null || this.indexName == "")
        return;
      if (this.startDate == null)
        return;
      if (this.endDate == null)
        return;
      getBaiduIndex(this.indexName, formatDate(this.startDate) + '', formatDate(this.endDate) + '').then(res => {
        // console.log(res);
        const result = res.data.reduce((acc, { type, date, index }) => {
          if (!acc[type]) {
            acc[type] = { dates: [], indexes: [] };
          }
          acc[type].dates.push(date);
          acc[type].indexes.push([date, index]);
          return acc;
        }, {}
        );
        // const { all: { dates: A, indexes: B } } = result;
        this.drawChart(result);
      })
    },
    drawChart(result) {
      this.loading = false;
      // 基于准备好的dom，初始化echarts实例
      let myMaxbar = echarts.init(document.getElementById("myMaxbar"));
      // 绘制图表
      myMaxbar.setOption({
        color: ["#0EA9A1", "#95CE5C", "#21D86D"],
        //提示框组件配置
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          },
          textStyle: {
            fontSize: 12,
            color: "#fff",
          },
          padding: 10,
        },
        // 图例组件
        legend: {
          show: true,
          top: "0",
          left: '5%',
          selectedMode: true,
          data: [
            {
              name: "总",
              textStyle: {
                color: "rgba(51, 51, 51, 1)",
              },
            },
            {
              name: "PC端",
              textStyle: {
                color: "rgba(51, 51, 51, 1)",
              },
            },
            {
              name: "移动端",
              textStyle: {
                color: "rgba(51, 51, 51, 1)",
              },
            },
          ],
        },
        //定义折线图距离左边多少右边多少的距离
        grid: {
          // left: "2%",
          // right: "5%",
          // bottom: "16%",
          containLabel: true, //区域是否包含坐标轴的刻度标签
        },
        xAxis: [ //定义x轴
          {
            // type: "time", //
            type: "category",
            // data: result.all.dates,
            nameTextStyle: {
              fontSize: 14,
            },
            axisLabel: { //坐标轴刻度的相关设置
              // interval: 0, //设置成 0 强制显示所有标签。
              // rotate: -45, //标签旋转的角度
              // margin: 15,
              textStyle: {
                // color:'#fff',
              }
            },
            // minInterval: 3
          },
        ],
        yAxis: [ // 定义y轴
          {
            nameTextStyle: {
              color: "#666666",
              fontSize: 14,
            },
            show: true,
            type: "value",
            axisLabel: { // 坐标轴刻度标签的相关设置
              textStyle: {
                // color: "#fff",
              },
            },
            axisLine: { // 坐标轴轴线相关设置
              show: false,
            },
            splitLine: { // 坐标轴在网格区域中的分隔线
              lineStyle: { //x轴网格样式设置
                color: "#12403F",
              },
            },
          },
        ],
        series: [ //系列列表。每个系列通过 type 决定自己的图表类型
          {
            name: "总",
            type: "line", // 设置为柱状图
            barWidth: 14,
            stack: 'Total',
            lineStyle: {
              width: 1
            },
            // showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(128, 255, 165)'
                },
                {
                  offset: 1,
                  color: 'rgb(1, 191, 236)'
                }
              ])
            },
            //柱状图设置数值
            label: {
              normal: {
                show: true,
                position: 'top'
              }
            },
            data: result.all.indexes,
          },
          {
            name: "PC端",
            type: "line", // 设置为折线图              
            lineStyle: {
              width: 1
            },
            // showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(255, 0, 135)'
                },
                {
                  offset: 1,
                  color: 'rgb(135, 0, 157)'
                }
              ])
            },
            data: result.pc.indexes,
          },
          {
            name: "移动端",
            type: "line",
            lineStyle: {
              width: 1
            },
            // showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(255, 191, 0)'
                },
                {
                  offset: 1,
                  color: 'rgb(224, 62, 76)'
                }
              ])
            },
            data: result.wise.indexes,
          },
        ],
      });
    }


  },
};
</script>
  
<style lang="scss" scoped>
.title{
  height: 50px;
  font-size: 20px;
  font-weight: 700;
  color: #111;
  line-height: 50px;
  padding-left: 5px;
}
.chart{
  background-color: white;
  border-radius: 10px;
}
</style>
  