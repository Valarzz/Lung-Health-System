<template>
    <div class="chatForm">
        <div style="overflow:hidden auto;height:400px;margin:10px;background-color: #f7f5f2;" class="test test-1">
            <div v-for="item in thisContent">
                <el-row v-if="thisUser_type==item.user_type">
                    <el-col :span="20" :offset="3">
                        <span class="sender">
                        {{item.content}}
                        </span>
                    </el-col>
                    <el-col :span="1">
                        <span v-if="item.user_type==user">                                 
                            <i class="icon iconfont icon-yonghu" style="font-size:30px" />
                        </span>
                        <span v-else>
                            <i class="icon iconfont icon-yisheng" style="font-size:30px" />
                        </span>
                    </el-col>
                </el-row>
                <el-row v-else>
                    <el-col :span="1">
                        <span v-if="item.user_type==user">                                 
                            <i class="icon iconfont icon-yonghu" style="font-size:30px" />
                        </span>
                        <span v-else>
                            <i class="icon iconfont icon-yisheng" style="font-size:30px" />
                        </span>
                    </el-col>
                    <el-col :span="20" :offset="0">
                        <span class="receiver">
                        {{item.content}}
                        </span>
                    </el-col>
                </el-row>
            </div>
        </div>
        <div style="margin:10px;">
        <el-input
        type="textarea"
        :rows="4"
        placeholder="Please enter content"
        v-model="reply">
        </el-input>
        <el-button size="small" style="float:right;margin:5px" @click="send">send</el-button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'chat',
    props: ['content', 'user_type', 'receiver', "index"],
    data(){
        return{
            thisContent: this.content,
            thisUser_type: this.user_type,
            doctor:'doctor',
            user:'user',
            reply: '',
        }
    },
    methods: {
        toBottom(){
            var container = this.$el.querySelector(".test");
            container.scrollTop = container.scrollHeight;
        },
        send(){
            var date = new Date();
            var replyInfo = {
                'sender': this.$store.state.username,
                'receiver': this.receiver,
                'commit_time': date,
                'content': this.reply,
            }
            this.$emit('send', replyInfo, this.index);
            this.reply = ''
        }
    },
    // created(){
    //   this.$on('test', function(){
    //   console.log('something handled!');
    // });
    // }
}
</script>

<style scoped>
    .chatform{
        height:80%;
        padding:1%;
        width:100%;
    }

    .sender{
        float: right;
        position: relative;
        display: inline-block;
        max-width: calc(40%);
        min-height: 35px;
        line-height: 2.1;
        font-size: 15px;
        padding: 6px 10px;
        text-align: left;
        word-break: break-all;
        background-color: #9eea6a;
        color: #000;
        border-radius: 4px;
        box-shadow: 0px 1px 7px -5px #000;
        border:0px solid #000;
        margin-top: 0;
        margin-right: 10px;
    }
    .sender:after {
        content: "";
        border-top: solid 5px #00800000;
        border-left: solid 10px #9eea6a;
        border-right: solid 10px #00800000;
        border-bottom: solid 5px #00800000;
        position: absolute;
        top: 10px;
        left: 100%;
    }

    .receiver{
        display: inline-block;
        line-height:30px;
        font-style: normal;
        background-color: white;
        letter-spacing: 2px;
        position: relative;
        max-width: calc(40%);
        min-height: 35px;
        line-height: 2.1;
        font-size: 15px;
        padding: 6px 10px;
        text-align: left;
        word-break: break-all;
        border-radius: 4px;
        color: #000;
        box-shadow: 0px 1px 7px -5px #000;
        border:0px solid #000;
        margin-top: 0;
        margin-left: 10px;
    }
    .receiver:after {
        content: "";
        border-top: solid 5px #00800000;
        border-left: solid 10px #00800000;
        border-right: solid 10px white;
        border-bottom: solid 5px #00800000;
        position: absolute;
        top: 10px;
        right: 100%;
    }

    .test-1::-webkit-scrollbar {
    /*滚动条整体样式*/
    width : 10px;  /*高宽分别对应横竖滚动条的尺寸*/
    height: 1px;
    }
    .test-1::-webkit-scrollbar-thumb {
    /*滚动条里面小方块*/
    border-radius: 10px;
    box-shadow   : inset 0 0 5px rgba(0, 0, 0, 0.2);
    background   : #535353;
    }
    .test-1::-webkit-scrollbar-track {
    /*滚动条里面轨道*/
    box-shadow   : inset 0 0 5px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    background   : #ededed;
    }

</style>