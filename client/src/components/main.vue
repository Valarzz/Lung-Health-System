<template>
    <div class="mainForm" style="height:100%">
            <div class="background"></div>
            <el-main v-loading="imageUpLoad.loading" element-loading-text="Testing..." element-loading-background="rgba(255, 255, 255, 0.7)" style="height:100%">
            <Tabbar></Tabbar>

            <div class="mainContent" :sytle="{'height':screenHeight+'px'}">
                <div class="wel">Welcome to</div>
                    <div class="sysName">
                        <transition name="el-zoom-in-center">
                        <div v-show="showSysName">Lung Health System</div>
                        </transition>
                    </div>
                <el-upload
                class="imageUpLoader"
                :class="{disabled:imageUpLoad.uploadDisabled}"
                action="#"
                list-type="picture-card"
                :file-list="imageUpLoad.imagelist"
                :auto-upload="false"
                style="text-align:center;"
                :on-change="handleChange">
                    <i slot="default" class="el-icon-plus"></i>
                    <div slot="file" slot-scope="{file}">
                        <img
                            class="el-upload-list__item-thumbnail"
                            :src="file.url" alt=""
                        >
                        <span class="el-upload-list__item-actions">
                            <span
                            class="el-upload-list__item-preview"
                            @click="handlePictureCardPreview(file)"
                            >
                            <i class="el-icon-zoom-in"></i>
                            </span>
                            <span
                            class="el-upload-list__item-delete"
                            @click="handleUpLoad(file)"
                            >
                            <i class="el-icon-upload2"></i>
                            </span>
                            <span
                            class="el-upload-list__item-delete"
                            @click="handleRemove(file)"
                            >
                            <i class="el-icon-delete"></i>
                            </span>
                        </span>
                    </div>
                </el-upload>
                <el-dialog :visible.sync="imageUpLoad.dialogVisible">
                    <img width="100%" :src="imageUpLoad.dialogImageUrl" alt="" style="margin:0">
                </el-dialog>

                <el-col :span="8" :offset="8">
                    <div class="result" :style="{'border':'solid 1.5px','border-radius':'10px', 'margin-top':'20px','height':resultBoxHeight+'px','color':'#606266'}" v-if="showResult">
                        <div style="text-align:center;margin:15px;font-size:30px">Test Result</div>
                        <div v-if="!noProblem">
                            <el-row>
                            <el-col :span="6" :offset="6">Name:</el-col>
                            <el-col :span="9" :offset="3">{{predInfo.name}}</el-col>
                            </el-row>
                            <el-row>
                            <el-col :span="6" :offset="6">Score:</el-col>
                            <el-col :span="7" :offset="5">{{predInfo.score}}</el-col>
                            </el-row>
                            <el-row>
                            <el-col :span="6" :offset="6">Position:</el-col>
                            <el-col :span="6" :offset="2">height:</el-col>
                            <el-col :span="3" :offset="0">{{predInfo.height}}</el-col>
                            </el-row>
                            <el-row>
                            <el-col :span="3" :offset="14">width:</el-col>
                            <el-col :span="3" :offset="3">{{predInfo.width}}</el-col>
                            </el-row>
                            <el-row>
                            <el-col :span="3" :offset="14">top:</el-col>
                            <el-col :span="3" :offset="3">{{predInfo.top}}</el-col>
                            </el-row>
                            <el-row>
                            <el-col :span="3" :offset="14">left:</el-col>
                            <el-col :span="3" :offset="3">{{predInfo.left}}</el-col>
                            </el-row>
                            <el-row style="text-align:center;color:green;padding-top:10px;font-size:25px">
                                <span v-if="!this.$store.state.token"><el-link href="/#/login">Login to consult online</el-link></span>
                                <span v-else @click="completeInfo"><el-link>Consult doctors online</el-link></span>
                            </el-row>
                        </div>
                        <div v-else style="font-size:20px;margin:15px">
                            Congratulations, we did not detect any of your diseases, you can change to another x-ray image to retest.
                        </div>
                    </div>
                </el-col>
            </div>
        </el-main>
    </div>
</template>

<script>
import https from '../api/https.js';
import Tabbar from '@/components/tabbar';
export default {
    components:{
        Tabbar
    },
    data(){
        return{
            resultBoxHeight: 0,
            screenHeight: 0,
            screenWidth: 0,
            predInfo: {},
            imageUpLoad: {
                seeUpLoad: true,
                dialogImageUrl: '',
                dialogVisible: false,
                disabled: false,
                imagelist: [],
                uploadDisabled: false,
                loading: false,
            },
            showSysName: false,
            showResult: false,
            noProblem: false,
        }
    },
    mounted(){
        this.screenHeight = document.documentElement.clientHeight;
        this.screenWidth = document.documentElement.clientWidth;
        this.resultBoxHeight = 0.3*this.screenHeight
    },
    created(){
        setTimeout(() => {
            this.showSysName = true;
        },1000);
    },
    methods: {
        handleRemove(file) {
        this.$confirm(`Are you sure you want to remove ${ file.name }？`).then(() => {
            this.imageUpLoad.imagelist.splice(0,1);
            // 等图片框延迟消失的动画过后再显示添加图片框
            setTimeout(() => {
                        this.imageUpLoad.uploadDisabled = false;
                    }, 1100);
        });
      },
      handlePictureCardPreview(file) {
        this.imageUpLoad.dialogImageUrl = file.url;
        this.imageUpLoad.dialogVisible = true;
      },
      handleChange(file, filelist){
          this.imageUpLoad.imagelist.push(file);
          this.imageUpLoad.uploadDisabled = true;
      },
      handleUpLoad(file){
        let reader = new FileReader();
        reader.readAsDataURL(file.raw);
        reader.onload = () => {
            var imgInfo = {
                'img_base64': reader.result,
            }
            this.$confirm(`Are you sure you want to upload ${ file.name }？`).then(() => {
                this.imageUpLoad.loading = true;
                https.fetchPost('detect', imgInfo).then((res) => {
                    this.noProblem = false;
                    this.imageUpLoad.loading = false;
                    if (res.data['code'] === 200) {
                        if(res.data.message == "没有结果"){
                            this.noProblem = true;
                        }else{
                            res.data.predInfo.score = res.data.predInfo.score.toFixed(3)
                            this.predInfo = res.data.predInfo;
                        }
                        this.showResult = true;
                    }
                })
            })
        }
      },
      completeInfo(){
          this.$prompt('Describe your symptoms ', 'Complete your information', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancel',
          inputType: 'textarea',
        }).then(({ value }) => {
          if(!this.imageUpLoad.imagelist.length){
              this.$message({
                type: 'info',
                message: 'Please upload an X-ray image first'
            });
            return;
          }
          var file = this.imageUpLoad.imagelist[0]
          let reader = new FileReader();
          reader.readAsDataURL(file.raw);
          let that = this;
          reader.onload = () => {
            var recordInfo = {
                'img_base64': reader.result,
                'symptoms': value,
                'height': that.predInfo.height,
                'width': that.predInfo.width,
                'left': that.predInfo.left,
                'top': that.predInfo.top,
                'name': that.predInfo.name,
                'score': that.predInfo.score,
            };
            https.fetchPost('buildRecord', recordInfo).then((res) => {
                if (res.data['code'] === 200) {
                    this.$message({
                        type: 'success',
                        message: 'The input is successful, it will be redirected for you soon...'
                    });
                    setTimeout(() => {
                        this.$router.push({path: 'record', query: {record_id: res.data['record_id']}});
                    },1000);
                }
            })
          }
        })
      }
    }
}
</script>

<style>
    .background{
        width:100%;
        height:100%;
        position: absolute;
        background-image: url(../assets/background.jpg);
        background-size:100% 100%;
        opacity: .4;
        z-index:-1;
    }
    .mainContent{
        margin-top:5%;
    }
    .disabled .el-upload--picture-card{
        display: none;
    }

    .wel{
        text-align:center;
        font-weight:lighter;
        font-size:50px;
        color:#606266;
        font-family: Arial;
    }

    .sysName{
        height:90px;
        text-align:center;
        font-weight:lighter;
        font-size:70px;
        color:#606266;
        font-family: Arial;
    }



</style>