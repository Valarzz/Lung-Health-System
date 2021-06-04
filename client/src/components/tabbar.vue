<template>
    <div class="tabbar">
        <el-row>
            <el-col :span="4" :offset="1" style="margin-top:15px">
                <i class="icon iconfont icon-yiliao_" style="font-size: 40px;margin-right:20px" />
                <span v-if="this.$store.state.token">
                <span v-if="this.$store.state.user=='user'"><i class="icon iconfont icon-yonghu" style="font-size: 40px" /></span>
                <span v-else><i class="icon iconfont icon-yisheng" style="font-size: 40px" /></span>
                </span>
            </el-col>

            <el-col :offset="14" :span="5" style="margin-top:15px">


                <el-tooltip class="item" content="History" placement="top">
                    <i v-show="this.$store.state.token" class="icon iconfont icon-lishijilu" style="font-size: 40px;margin-right:20px" @click="goToHistory" />
                </el-tooltip>

                <el-tooltip class="item" content="Message" placement="top">
                    <i v-show="this.$store.state.token" class="el-icon-message-solid" style="font-size: 40px;margin-right:20px" @click="" />
                </el-tooltip>


                <span v-if="this.$store.state.token">
                    <el-tooltip class="item" content="Logout" placement="top">
                        <i class="icon iconfont icon-tuichu" style="font-size: 40px;margin-right:20px" @click="logout" />
                    </el-tooltip>
                </span>

                <span v-else>
                    <el-tooltip class="item" content="Login" placement="top">
                        <i class="el-icon-s-home" style="font-size: 40px;margin-right:20px" @click="goToLogin" />
                    </el-tooltip>
                </span>
                

                <el-tooltip class="item" content="Contacts us" placement="top">
                    <el-popover
                    placement="right"
                    width="200"
                    trigger="click"
                    title="E-mail"
                    content="2819238408@qq.com">
                    <i class="el-icon-chat-dot-square" style="font-size: 40px;margin-right:20px" slot="reference" />
                    </el-popover>
                </el-tooltip>

                <el-tooltip class="item" content="FAQ" placement="right">
                    <el-popover
                    placement="right"
                    width="200"
                    trigger="click">
                    <el-collapse accordion>
                        <el-collapse-item title="Functions">
                        Our system can quickly give the user a preliminary diagnosis result based on image of the lung X-ray inspection.
                        </el-collapse-item>
                        <el-collapse-item title="How to use">
                            <el-steps :active="1">
                            <el-step title="step1" description="Have a lung x-ray examination"></el-step>
                            <el-step title="step2" description="Upload the examination result to our system"></el-step>
                            <el-step title="step3" description="Get the result"></el-step>
                            </el-steps>
                        </el-collapse-item>
                        <el-collapse-item title="Statement">
                            We only use the images of your x-ray inspection results for detection, and will not reveal any of your personal privacy.
                        </el-collapse-item>
                    </el-collapse>
                    <i class="el-icon-question" style="font-size: 40px;margin-right:20px" slot="reference" />
                    </el-popover>
                </el-tooltip>

            </el-col>
        </el-row>
    </div>
    
</template>

<script>
export default {
    name: 'tabbar',
    data(){
        return{
            login: '',
        }
    },
    methods: {
        goToLogin(){
            this.$router.push('login');
        },
        goToHistory(){
            this.$router.push('history');
        },
        logout(){
             this.$store.commit('del_token');
             sessionStorage.clear();
             this.$router.push('/')
        }
    }
}
</script>

<style scoped>
    i:hover{
        cursor:pointer;
    }
</style>