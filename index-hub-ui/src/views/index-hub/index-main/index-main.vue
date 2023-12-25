<template>
    <div id="all">
        <el-row :gutter="20" class="row-bg" >
            <el-col :span="24">
                <div class="grid-content bg-purple">
                    <indexBaidu></indexBaidu>
                </div>
            </el-col>
        </el-row>
        <el-row :gutter="20" class="row-bg" >
            <el-col :span="24">
                <div class="grid-content bg-purple">
                    抖音
                </div>
            </el-col>
        </el-row>
        <el-row :gutter="20" class="row-bg" >
            <el-col :span="24">
                <div class="grid-content bg-purple">
                    360
                </div>
            </el-col>
        </el-row>
        <el-row :gutter="20" class="row-bg" >
            <el-col :span="24">
                <div class="grid-content bg-purple">
                    6188
                </div>
            </el-col>
        </el-row>
        <el-row :gutter="20" class="row-bg"  >
            <el-col :span="24">
                <div class="grid-content bg-purple">
                    谷歌
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import indexBaidu from './components/index-baidu.vue';
export default {
    components:{indexBaidu},
    data() {
        return {
            inputIndex: "",
            select: ""
        }
    }
}
</script>

<style scoped>
.all{
    height: 100%;
    width: 100%;
}
.bg-purple {
    /* background: #d3dce6; */
}

.bg-purple-light {
    background: #e5e9f2;
}

.grid-content {
    border-radius: 20px;
    min-height: 36px;
}
.row-bg {
    padding: 10px 0;
  }
</style>