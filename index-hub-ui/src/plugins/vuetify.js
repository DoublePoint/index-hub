import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import zhHans from 'vuetify/es5/locale/zh-Hans'   // 引入中文语言包
// import 'typeface-roboto/index.css'    // 引入本地的Roboto字体资源
import '@mdi/font/css/materialdesignicons.css'  // 引入本地的Material Design Icons资源

Vue.use(Vuetify)

const opts = {
  lang: {
    locales: { zhHans },
    current: 'zhHans'
  },
  icons: {
    iconfont: 'mdi',	// 设置使用本地的icon资源
  },
  breakpoint: {
    mobileBreakpoint: 'Large' // 这个值等于960
  },
}

export default new Vuetify(opts)