<template>
    <div class="all">
        <el-date-picker v-model="selectDate" type="daterange" align="right" unlink-panels range-separator="至"
        value-format="yyyy-MM-dd HH:mm:ss"
        @change="dateOnPick"
            class="datepicker" start-placeholder="开始日期" end-placeholder="结束日期" :picker-options="pickerOptions">
        </el-date-picker>
        <el-input v-model="indexName" class="input-with-select" @change="indexNameChange">
            <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>

        <el-tag v-for="tag in allIndexName" :key="tag" closable type="" @close="handleClose(tag)" @click="handleClick(tag)">
        {{tag}}
        </el-tag>
    </div>
</template>

<script>
export default {
    data() {
        return {
            theme: {
        default: { isDark: false },
      },
            indexName:this.$store.state.indexes.indexName[this.$store.state.indexes.indexName.length-1],
            selectDate:[this.$store.state.indexes.startDate,this.$store.state.indexes.endDate],
            pickerOptions: {
                shortcuts: [{
                    text: '最近一周',
                    onClick(picker) {
                    const end = new Date();
                    const start = new Date();
                    start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
                    picker.$emit('pick', [start, end]);
                    }
                }, {
                    text: '最近一个月',
                    onClick(picker) {
                    const end = new Date();
                    const start = new Date();
                    start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
                    picker.$emit('pick', [start, end]);
                    }
                }, {
                    text: '最近三个月',
                    onClick(picker) {
                    const end = new Date();
                    const start = new Date();
                    start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
                    picker.$emit('pick', [start, end]);
                    }
                }]
            }
        }
    },
    computed:{
        allIndexName() {
            return this.$store.state.indexes.indexName;
        }
        // indexName:{
        //     get(){
        //         return 
        //     },
        //     set(){

        //     }
        // },
        // selectDate:{
        //     get(){
        //         //debugger
        //         const end = this.$store.state.indexes.endDate;
        //         const start = this.$store.state.indexes.startDate;
        //         return [start,end];
        //     },
        //     set(val){
        //         this.$store.dispatch("indexes/setIndexStartDate",new Date(val[0]));
        //         this.$store.dispatch("indexes/setIndexEndDate",new Date(val[1]));
        //     }
        // }
    },
    watch:{
        // selectDate(newVal,oldVal){
        //     console.log(newVal[0],"~",newVal[1]);
        //     this.$store.dispatch('indexes/setIndexStartDate',newVal[0]);
        //     this.$store.dispatch('indexes/setIndexEndDate',newVal[1]);
        // },
        // indexName(newVal,oldVal){
        //     this.$store.dispatch('indexes/setIndexName', newVal);
        // },
        
    },
    mounted() {
        console.log(this.$store)
        // console.log(this.$route);
        // this.inputIndex = this.$route.query.searchIndex;
        // const end = new Date();
        // const start = new Date();
        // start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
        // // picker.$emit('pick', [start, end]);
        // this.selectDate=[start,end]
        // this.$store.dispatch('indexes/setIndexName', this.inputIndex);
        // this.$store.dispatch('indexes/setIndexStartDate',start);
        // this.$store.dispatch('indexes/setIndexEndDate',end);
    },
    methods:{
        indexNameChange(val){
            this.$store.dispatch('indexes/unshiftIndexName', val);
        },
        dateOnPick(dateArr){
            //debugger
            this.$store.dispatch('indexes/setIndexStartDate',new Date(dateArr[0]));
            this.$store.dispatch('indexes/setIndexEndDate',new Date(dateArr[1]));
        },
        handleClose(tag){
            this.$store.dispatch('indexes/removeIndexName', tag);
        },
        handleClick(tag){
            this.indexName = tag;
            this.$store.dispatch('indexes/removeIndexName', tag);
            this.$store.dispatch('indexes/unshiftIndexName', tag);
        }
    }
    
}
</script>

<style lang="scss" scoped>
.all {
    .datepicker {
        width: 100%;
        margin: 15px 0 15px 0;
    }
}
</style>