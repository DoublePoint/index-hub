<template>
  <div class="all">
    <el-container class="llcontainer">
      <el-aside width="500px">
        <IndexSideBar></IndexSideBar>
      </el-aside>
      <el-main>
        <IndexMain></IndexMain>
      </el-main>
    </el-container>
  </div>
</template>
<script>
import IndexSideBar from './index-sidebar/index-sidebar.vue'
import IndexMain from './index-main/index-main.vue'


export default {
  data: () => ({
    alignments: [
      'start',
      'center',
      'end',
    ],
  }),
  components:{IndexSideBar,IndexMain}
}
</script>

<style lang="scss" >
.all{
  height: 100%;
  width: 100%;

  .llcontainer{
    height: inherit;
    width: inherit;
  }
}
.el-aside {
  background-color: #D3DCE6;
  color: #333;
  height: 100%;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  height: 100%;
}
</style>