<template>
    <div class="dcotorForm" style="height:100%">
        <div class="background"></div>
        <Tabbar></Tabbar>
        <div class="record">
            <div v-for="r in currentPage" class="item">
                <div class="info">
                    <i class="icon iconfont icon-yonghu" style="font-size:20px"></i>
                    <span style="font-size:15px">{{r.username}}</span>
                    <span style="float:right;font-size:15px;margin-top:5px">{{r.commit_time}}</span>
                </div>
                <div class="symptoms">{{r.showSymptom}}</div>
                <div class="testResult">
                    <div class="image"><img height="100%" width="100%" :src="r.img_base64" /></div>
                    <div class="prediction">
                        <div style="text-align:center;margin:10px;font-size:15px">Test Result</div>
                        <div style='font-size:10px'>
                        <el-row>
                        <el-col :span="6" :offset="6">Name:</el-col>
                        <el-col :span="9" :offset="3">{{r.test_result.name}}</el-col>
                        </el-row>
                        <el-row>
                        <el-col :span="6" :offset="6">Score:</el-col>
                        <el-col :span="7" :offset="5">{{r.test_result.score}}</el-col>
                        </el-row>
                        <el-row>
                        <el-col :span="6" :offset="6">Position:</el-col>
                        <el-col :span="6" :offset="2">height:</el-col>
                        <el-col :span="3" :offset="0">{{r.test_result.height}}</el-col>
                        </el-row>
                        <el-row>
                        <el-col :span="3" :offset="14">width:</el-col>
                        <el-col :span="3" :offset="3">{{r.test_result.width}}</el-col>
                        </el-row>
                        <el-row>
                        <el-col :span="3" :offset="14">top:</el-col>
                        <el-col :span="3" :offset="3">{{r.test_result.top}}</el-col>
                        </el-row>
                        <el-row>
                        <el-col :span="3" :offset="14">left:</el-col>
                        <el-col :span="3" :offset="3">{{r.test_result.left}}</el-col>
                        </el-row>
                        </div>
                    </div>
                    <div class='help'>
                        <div style="float:right;margin:130px 0">
                            <el-link @click="goToRecord(r.record_id)">
                                <span v-if="$store.state.user=='doctor'">Give suggestion>></span>
                                <span v-else>View>></span>
                            </el-link></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="block" style="text-align:center">
            <el-pagination
            @current-change="handleCurrentChange"
            @prev-click="handelPrevClick"
            @next-click="handelNextClick"
            :current-page="currentPageNum"
            :page-size="1"
            layout="total, prev, pager, next, jumper"
            :total="total">
            </el-pagination>
        </div>
    </div>
    
</template>

<script>
import Tabbar from '@/components/tabbar';
import https from '../api/https.js'
export default {
    name: 'history',
    components: {
        Tabbar,
    },
    data(){
        return{
            currentPageNum: 0,
            currentPage:[],
            allPages:[],
            total: 0,
        }
    },
    methods: {
        goToRecord(record_id){
            this.$router.push({path: 'record', query: {record_id: record_id}});
        },
        handelPrevClick(page){
            if(this.allPages[page-1].length >0){
                this.currentPage = this.allPages[page-1];
            }else{
                https.fetchGet('showRecord/'+page).then((res) => {
                    if(res.data.code === 200){
                        for(let i=0; i<res.data.retInfo.length;i++){
                            if(res.data.retInfo[i].symptoms.length > 40){
                                res.data.retInfo[i].showSymptom = res.data.retInfo[i].symptoms.substr(0,40)+'...';
                            }else{
                                res.data.retInfo[i].showSymptom = res.data.retInfo[i].symptoms;
                            }
                        }
                        this.allPages[page-1] = res.data.retInfo;
                        this.currentPage = res.data.retInfo;
                        this.currentPageNum = page;
                    }
                })
            }
        },
        handelNextClick(page){
            if(this.allPages[page-1].length >0){
                this.currentPage = this.allPages[page-1];
            }else{
                https.fetchGet('showRecord/'+page).then((res) => {
                    if(res.data.code === 200){
                        for(let i=0; i<res.data.retInfo.length;i++){
                            if(res.data.retInfo[i].symptoms.length > 40){
                                res.data.retInfo[i].showSymptom = res.data.retInfo[i].symptoms.substr(0,40)+'...';
                            }else{
                                res.data.retInfo[i].showSymptom = res.data.retInfo[i].symptoms;
                            }
                        }
                        this.allPages[page-1] = res.data.retInfo;
                        this.currentPage = res.data.retInfo;
                        this.currentPageNum = page;
                    }
                })
            }
        },
        handleCurrentChange(page){
            if(this.allPages[page-1].length >0){
                this.currentPage = this.allPages[page-1];
            }else{
                https.fetchGet('showRecord/'+page).then((res) => {
                    if(res.data.code === 200){
                        for(let i=0; i<res.data.retInfo.length;i++){
                            if(res.data.retInfo[i].symptoms.length > 40){
                                res.data.retInfo[i].showSymptom = res.data.retInfo[i].symptoms.substr(0,40)+'...';
                            }else{
                                res.data.retInfo[i].showSymptom = res.data.retInfo[i].symptoms;
                            }
                        }
                        this.allPages[page-1] = res.data.retInfo;
                        this.currentPage = res.data.retInfo;
                        this.currentPageNum = page;
                    }
                })
            }
        },
    },
    created(){
         https.fetchGet('showRecord/1').then((res) => {
            if(res.data.code === 200){
                for(let i=0; i<res.data.retInfo.length;i++){
                    if(res.data.retInfo[i].symptoms.length > 40){
                        res.data.retInfo[i].showSymptom = res.data.retInfo[i].symptoms.substr(0,40)+'...';
                    }else{
                        res.data.retInfo[i].showSymptom = res.data.retInfo[i].symptoms;
                    }
                }
                this.total=Math.ceil(res.data.total/3);;
                for (let i=0;i<this.total;i++){
                    this.allPages.push([])
                }
                this.allPages[0] = res.data.retInfo;
                this.currentPage = res.data.retInfo;
                console.log(this.currentPage)
                this.currentPageNum = 1
            }
        })
    },
}
</script>

<style scoped>
    .record{
        width: 50%;
        height: 80%;
        border-radius:5px;
        box-sizing: border-box;
        margin:2% auto
    }

    .item{
        width: 95%;
        height: 32%;
        border:1px solid rgb(105, 104, 104);
        border-radius:10px;
        box-sizing: border-box;
        margin:1% auto;

    }

    .info{
        width: 96%;
        height: 8%;
        box-sizing: border-box;
        margin:1% auto
    }

    .symptoms{
        width: 95%;
        height: 3%;
        float: left;
        box-sizing: border-box;
        margin-bottom:2%;
        margin-left:2%
    }

    .testResult{
        width: 100%;
        height: 70%;
        float: left;
        box-sizing: border-box;
        margin-bottom:3%;
    }

    .help{
        width: 25%;
        height: 100%;
        float: left;
        box-sizing: border-box;
        margin:0 2%;
    }

    .image,.prediction{
        width: 30%;
        height: 100%;
        float: left;
        border:1px solid rgb(105, 104, 104);
        box-sizing: border-box;
        margin:0 2%;
    }

    .background{
        width:100%;
        height:100%;
        position: absolute;
        background-image: url(../assets/background.jpg);
        background-size:100% 100%;
        opacity: .4;
        z-index:-1;
    }
</style>>