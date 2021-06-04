<template>
    <div class="recordForm" style="height:100%">
        <div class="background"></div>
        <Tabbar></Tabbar>
        <div class="information">
            <i class="icon iconfont icon-yonghu" style="font-size:30px"></i>
            <span style="font-size:20px">{{recordInfo.username}}</span>
            <span style="float:right;font-size:20px;margin-top:5px">{{recordInfo.commit_time}}</span>
            <div class="symptoms">
                <div style="font-size:30px;margin-bottom:5px">Symptoms description:</div>
                <div class="description">{{recordInfo.symptoms}}</div>
            </div>
            <div class="testResult">
                <div style="font-size:30px;margin-bottom:5px">Diagnosis:</div>
                <div ref="img" class="image"><img height="100%" width="100%" :src="recordInfo.img_base64" /><div class="illness_position" :style="{'position':'absolute','top':this.top+'%','left':this.left+'%','width':this.width+'px','height':this.height+'px','border':'blue solid 2px'}"></div></div>
                <div class="prediction">
                    <div style="text-align:center;margin:15px;font-size:30px">Test Result</div>
                        <div style='font-size:20px'>
                        <el-row class="result_item">
                        <el-col :span="6" :offset="4">Name:</el-col>
                        <el-col :span="9" :offset="3">{{recordInfo.test_result.name}}</el-col>
                        </el-row >
                        <el-row class="result_item">
                        <el-col :span="6" :offset="4">Score:</el-col>
                        <el-col :span="7" :offset="5">{{recordInfo.test_result.score}}</el-col>
                        </el-row>
                        <el-row class="result_item">
                        <el-col :span="6" :offset="4">Position:</el-col>
                        <el-col :span="6" :offset="2">height:</el-col>
                        <el-col :span="3" :offset="0">{{recordInfo.test_result.height}}</el-col>
                        </el-row>
                        <el-row class="result_item">
                        <el-col :span="3" :offset="12">width:</el-col>
                        <el-col :span="3" :offset="3">{{recordInfo.test_result.width}}</el-col>
                        </el-row>
                        <el-row class="result_item">
                        <el-col :span="3" :offset="12">top:</el-col>
                        <el-col :span="3" :offset="3">{{recordInfo.test_result.top}}</el-col>
                        </el-row>
                        <el-row class="result_item">
                        <el-col :span="3" :offset="12">left:</el-col>
                        <el-col :span="3" :offset="3">{{recordInfo.test_result.left}}</el-col>
                        </el-row>
                        </div>
                </div>
            </div>
        </div>
        <div class="advice">
            <div>
                <div style="font-size:30px;margin-bottom:5px">
                    <span v-if="this.$store.state.user=='user'">Doctor's suggestion:</span>
                    <span v-else>Give suggestion:</span>
                </div>
                <el-collapse accordion>
                <el-collapse-item v-for="item,index in content" @click.native="toBottom">
                    <template slot="title">
                        <span style="font-size:20px">
                            <span v-if="$store.state.user=='user'"><i class="icon iconfont icon-yisheng" style="font-size:30px" />{{item.name}}</span>
                            <span v-else><i class="icon iconfont icon-yonghu" style="font-size:30px" />{{item.username}}</span>
                        </span>
                    </template>
                    <Chat ref="myChat" :content="item.content" :user_type="$store.state.user" v-on:send="send" :receiver="item.username" :index="index"></Chat>
                </el-collapse-item>
                </el-collapse>
            </div>
        </div>
    </div>
</template>

<script>
import https from '../api/https.js'
import Tabbar from '@/components/tabbar';
import Chat from '@/components/chat';
export default {
    name: 'login',
    components: {
        Tabbar,
        Chat,
    },
    data() {
        return{
            content:[],
            recordInfo: {},
            textarea: '',
            data:{},
            height: 0,
            width: 0,
            top: 0,
            left: 0,
        }
    },
    methods: {
    toBottom(){
        this.$refs.myChat[0].toBottom();
    },
    fetchRecord(){
        https.fetchGet('getRecord/' + this.$route.query.record_id).then((res) => {
            if(res.data.code === 200){
                this.recordInfo = res.data.recordInfo
                this.$nextTick(function(){
                    this.height =  this.$refs.img.clientHeight*this.recordInfo.test_result.height/1024;
                    this.width =  this.$refs.img.clientWidth*this.recordInfo.test_result.width/1024;
                    this.top = this.recordInfo.test_result.top/1024*100;
                    this.left = this.recordInfo.test_result.left/1024*100;
                    console.log(this.height,this.width,this.top,this.left)
                })
            }
        })
    },
    fetchChat(){
        https.fetchGet('getChat/' + this.$route.query.record_id).then((res) => {
            if(res.data.code === 200){
                this.content = res.data.chatInfo;
            }
        })
    },
    send(replyInfo, index){
        replyInfo['record_id'] = this.recordInfo.record_id;
        this.$socket.emit('send', replyInfo);
        this.content[index].content.push({
            'content': replyInfo.content,
            'user_type': this.$store.state.user
        })
        this.toBottom();
    }

    },
    created(){
        this.fetchRecord();
        this.fetchChat();
    },

    sockets:{    // socket.io携带，与watch/create/data等同级
    connect:function () {
        // 用自己的用户名和record_id创建一个房间
        this.$socket.emit('join', {'username': this.$store.state.username, 'record_id': this.recordInfo.record_id})
    	console.log('连接成功')   // 判断是否正确连接上后端
    	},
    	
    test:function (data) {    // api为对应后端发出的信息接口，可自行更换
        this.data = data      // 获取后端发出的信息
      },
    join:function (data) {    // api为对应后端发出的信息接口，可自行更换
        console.log(data)
    },
    send: function (data){
        var flag = false;
        console.log(data)
        for(let i=0; i<this.content.length;i++){
            if (data.sender == this.content[i].username){
                this.content[i].content.push({
                    'content': data.content,
                    'user_type': data.user_type,
                })
                flag = true;
            } 
        }
        if(flag == false){
            this.content.push({
                'name': data.name,
                'username': data.sender,
                'user_type': data.user_type,
                'content': [{
                    'content': data.content,
                    'user_type': data.user_type,
                }]
            });
        }
        this.toBottom()
    },
    },
    mounted () {    // 在组件开始渲染时进行调用
      var that = this
      this.$socket.connect() // socket连接
      console.log('连接中')
    },
    
    destroyed () {    // 当离开组件时，结束调用
      if (this.$socket) {
          this.$socket.disconnect()  // 如果socket连接存在，销毁socket连接
      }
      console.log('连接已断开')
    }
}

</script>

<style scoped>
    .background{
        width:100%;
        height:100%;
        position: absolute;
        background-image: url(../assets/background.jpg);
        background-size:100% 100%;
        opacity: .4;
        z-index:-1;
    }

    .information{
        width: 48%;
        height: 89%;
        border:1px solid rgb(105, 104, 104);
        border-radius:10px;
        float: left;
        box-sizing: border-box;
        padding: 2%;
        margin:1%
    }

    .advice{
        width: 48%;
        height: 89%;
        /* border:1px solid rgb(105, 104, 104); */
        border-radius:10px;
        float: left;
        box-sizing: border-box;
        padding: 2%;
        margin:1%
    }

    .symptoms{
        width: 100%;
        height: 35%;

        float: left;
        box-sizing: border-box;
        margin: 3% 0;
    }

    .description{
        border: 2px dashed rgb(99, 97, 97);
        border-radius:10px;
        font-size:18px;
        height:80%;
        text-decoration:underline dashed 1px rgb(167, 157, 157);
        padding:5px;
        
    }

    .testResult{
        width: 100%;
        height: 55%;
        float: left;
        box-sizing: border-box;
        margin-bottom:3%;
    }

    .image,.prediction{
        width: 45%;
        height: 88%;
        border:1px solid rgb(105, 104, 104);
        float: left;
        box-sizing: border-box;
        margin:0 2%;
        position:relative;
    }

    .suggestion{
        height:400px;
        background-color:rgb(224, 219, 219);
        padding:5px 0;
    }

    .result_item{
        margin:12px;
    }


</style>