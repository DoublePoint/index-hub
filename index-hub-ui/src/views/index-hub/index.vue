<template>
  <div class="all">
    <div class="container">
      <div class="big-title">
        <vue-typed-js :strings="['指数搜索 一站式服务! ', '指数搜索 打包全下载! ', '指数搜索 持续更新中! ']" class="vue-typed-js" :type-speed="200"
          :back-speed="100" :startDelay="100" :loop="true" :show-cursor="true" cursor-char="|" :smart-backspace="true">
          <h1 class="typing typed-text"></h1>
        </vue-typed-js>
      </div>
      <div class="sec-title">
        <p>Index-Hub提供了一站式指数💹搜索的功能，本为个人使用现免费提供给大家🆓，初步计划集成百度指数、抖音指数、360指数、B站指数、谷歌指数等。本平台只从页面上对上述指数站进行了集成，暂时不具备如调用各大指数站API获取历史指数的能力，后续如有需要，在资金、精力允许的情况下也会考虑集成🚀🚀...</p>
      </div>
      <v-form class="centered"  @submit.native.prevent>
        <v-container>
          <v-row>
            <v-col cols="2"></v-col>
            <v-col cols="8">
              <v-text-field v-model="message" append-icon="mdi-magnify" filled single-line label="Please input index"
                @keydown="onEnter"></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </div>
  </div>
</template>
<script>
import { VueTypedJs } from 'vue-typed-js'
export default {
  components: {
    VueTypedJs
  },
  data: () => ({
    password: 'Password',
    show: false,
    message: '',
    marker: true,
    iconIndex: 0,
    icons: [
      'mdi-emoticon',
      'mdi-emoticon-cool',
      'mdi-emoticon-dead',
      'mdi-emoticon-excited',
      'mdi-emoticon-happy',
      'mdi-emoticon-neutral',
      'mdi-emoticon-sad',
      'mdi-emoticon-tongue',
    ],
  }),

  computed: {   
    icon() {
      return this.icons[this.iconIndex]
    },
  },

  methods: {
    onEnter(keyboardEvent){
      if(this.message=="")
        return;
      if(keyboardEvent.key==='Enter'){
        //debugger
        this.$store.dispatch('indexes/removeIndexName', this.message);
        this.$store.dispatch('indexes/unshiftIndexName', this.message);
        const end = new Date();
        const start = new Date();
        start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
        this.selectDate=[start,end]
        this.$store.dispatch('indexes/setIndexStartDate',start);
        this.$store.dispatch('indexes/setIndexEndDate',end);
        this.$router.push({
          path:'/index-hub/index-main',
          query:{
            searchIndex:this.message
          }
        })
      }
    }
  },
}
</script>

<style lang="scss" scoped>
.v-input__control .v-text-field__slot .v-label {
  transform-origin: top left;
}

.v-input__control .v-input__slot {
  opacity: 0.9;
  background-color: #fff !important;
}

.centered {
  position: relative;
  top: 15%;
}

.all {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-image: url("../../assets/images/bg.png");
  background-size: cover;
}

.typed-text {
  font-weight: 600;
  font-family: Manrope, Arial, "Helvetica Neue", Helvetica, sans-serif !important;
}

.container {
  position: relative;
  height: 100%;

  .big-title {
    position: relative;
    top: 15%;
    height: 60px;

    h1 {
      text-align: center;
      font-size: 60px;
    }

    .typed-cursor {
      font-size: 60px;
    }
  }

  .sec-title {
    font-size: 18px;
    font-weight: 400;
    line-height: 26px;
    color: rgba(30,25,44,.6);
    margin: 37px auto 51px;
    max-width: 544px;
    top: 15%;
    position: relative
  }
}

.vue-typed-js {
  padding-left: 50%;
  margin-left: -289px;
}

</style>
