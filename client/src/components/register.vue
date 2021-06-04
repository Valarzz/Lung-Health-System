<template>
    <div class="registerForm">
        <!-- 用来提示填写不符合规范的消息框 -->
            <el-dialog
            title="提交失败"
            :visible.sync="dialogVisible1"
            width=30%>
            <span>填写不符合规范！</span>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="dialogVisible1 = false">确认</el-button>
            </span>
            </el-dialog>

            <!-- 用来提示验证码错误的消息框 -->
            <el-dialog
            title="注册失败"
            :visible.sync="dialogVisible2"
            width=30%>
            <span>注册失败，请稍后再试！</span>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="dialogVisible2 = false">确认</el-button>
            </span>
            </el-dialog>

            <!-- 用来提示注册成功的消息框 -->
            <el-dialog
            title="注册成功"
            :visible.sync="dialogVisible3"
            width=30%>
            <span>注册成功！点击确认跳转到登录页面</span>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="goToLogin()">确认</el-button>
            </span>
            </el-dialog>
        <div class="background"></div>
        <div class="register_box">
            <div class="avator_box">
                <img src="../assets/logo.png" alt />
            </div>
            <el-tabs type="border-card" :stretch=true class="register_form">
                <el-tab-pane>
                    <span slot="label"><i class="icon iconfont icon-yonghu" style="font-size:30px"></i>Register as a user</span>
                    <el-form label-width="100px" class="user_register" :model="userInfo" ref="userInfo" :rules="userRules">
                        <el-form-item label="Username:" prop="Username">
                        <el-input  prefix-icon="el-icon-user" placeholder="Please enter your username" v-model="userInfo.Username"></el-input>
                        </el-form-item>
                        <el-form-item label="Password:"  prop="Password">
                        <el-input prefix-icon="el-icon-lock" placeholder="Please enter your password" type="password" v-model="userInfo.Password"></el-input>
                        </el-form-item>
                        <el-form-item label="Confirm:" prop="Confirm">
                        <el-input prefix-icon="el-icon-lock" placeholder="Please confirm your password" type="password" v-model="userInfo.Confirm"></el-input>
                        </el-form-item>
                        <el-form-item class="btns">
                            <div style="text-align:center">
                        <el-button type="info" @click="register('userInfo')" :loading="userInfo.loading">
                            <span v-if="!userInfo.loading">Register</span>
                            <span v-else>Loading</span>
                        </el-button>
                        </div>
                        </el-form-item>
                    </el-form>
                </el-tab-pane>
                 <el-tab-pane>
                    <span slot="label"><i class="icon iconfont icon-yisheng" style="font-size:30px"></i>Register as a doctor</span>
                    <el-form label-width="100px" class="doc_register" :model="doctorInfo" :rules="doctorRules" ref="doctorInfo">
                        <el-form-item label="Username:" prop="Username">
                        <el-input  prefix-icon="el-icon-user" placeholder="Please enter your username" v-model="doctorInfo.Username"></el-input>
                        </el-form-item>
                        <el-form-item label="Password:"  prop="Password">
                        <el-input prefix-icon="el-icon-lock" placeholder="Please enter your password" type="password" v-model="doctorInfo.Password"></el-input>
                        </el-form-item>
                        <el-form-item label="Confirm:" prop="Confirm">
                        <el-input prefix-icon="el-icon-lock" placeholder="Please confirm your password" type="password" v-model="doctorInfo.Confirm"></el-input>
                        </el-form-item>
                        <h2 style="font-weight:lighter;font-size:20px">Personal Information:</h2>
                        <el-row>
                            <el-col :span="12">
                                <el-form-item  label="First name:" prop="FirstName">
                                <el-input v-model="doctorInfo.FirstName" placeholder="your first name"></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="12">
                                <el-form-item  label="Last name:" prop="LastName">
                                <el-input v-model="doctorInfo.LastName" placeholder="your first last name"></el-input>
                                </el-form-item>
                            </el-col>
                        </el-row>

                        <el-form-item  label="Organization:" prop="Organization">
                        <el-input v-model="doctorInfo.Organization" placeholder="Please confirm your school/enterprise"></el-input>
                        </el-form-item>

                        <el-form-item  label="Background:" prop="Background">
                            <el-select placeholder="Please choose your background" style="width:80%" v-model="doctorInfo.Background">
                            <el-option label="Student in medical school" value="Medical school student"></el-option>
                            <el-option label="Doctor in hospital" value="Doctor"></el-option>
                            <el-option label="Teacher in medical school" value="Professor"></el-option>
                            </el-select>
                        </el-form-item>

                        <el-form-item>
                        <el-checkbox>I guarantee that the above information is true</el-checkbox>
                        </el-form-item>
                        
                        <el-form-item  class="btns">
                            <div style="text-align:center">
                            <el-button type="info" :loading="doctorInfo.loading">
                                <span v-if="!doctorInfo.loading" @click="registerDoc('doctorInfo')">Register</span>
                                <span v-else>Loading</span>
                            </el-button>
                            </div>
                        </el-form-item>
                    </el-form>
                </el-tab-pane>
            </el-tabs>
            <!-- 输入表单 -->
        </div>
    </div>
</template>

<script>
    import https from '../api/https.js';
    export default {
        name: 'register',
        data(){
            var validateUser = (rule, value, callback) => {
                    if (value === '') {
                    callback(new Error('Please enter Username'));
                    } else {
                    var form = {
                        'username': value,
                    };
                    https.fetchPost('checkUsername', form).then((res) => {
                        if (res.data['code'] === 200) {
                            callback();
                        }else{
                            callback(new Error('Username has been registered'));
                        }
                    })
                }
            };
            var validateUserConfirm = (rule, value, callback) => {
                    if (value === '') {
                    callback(new Error('Please confirm Password'));
                    } else {
                        if(this.userInfo.Password!= '' && this.userInfo.Password != value){
                            callback(new Error('Inconsistent passwords'))
                        }else{
                            callback();
                        }
                }
            };

            var validateDocConfirm = (rule, value, callback) => {
                    if (value === '') {
                    callback(new Error('Please confirm Password'));
                    } else {
                        if(this.doctorInfo.Password!= '' && this.doctorInfo.Password != value){
                            callback(new Error('Inconsistent passwords'))
                        }else{
                            callback();
                        }
                }
            };
            return{
                dialogVisible1: false,
                dialogVisible2: false,
                dialogVisible3: false,
                userInfo: {
                    loading: false,
                    Username: '',
                    Password: '',
                    Confirm: '',
                },
                doctorInfo: {
                    loading: false,
                    Username: '',
                    Password: '',
                    Confirm: '',
                    FirstName: '',
                    LastName: '',
                    Organization: '',
                    Background: '',
                },
                userRules: {
                    Username: [
                        { required: true,validator: validateUser, trigger: 'blur' },
                        { min: 5, max: 10,  message: 'The length should be between 5 and 10 characters', trigger: 'blur'}
                    ],
                    Password: [
                        { required: true, message: 'Please enter password!', trigger: 'blur'},
                        { min: 6, max: 12,  message: 'The length should be between 6 and 12 characters', trigger: 'blur'}
                    ],
                    Confirm: [
                        { required: true,validator: validateUserConfirm, trigger: 'blur'}
                    ]
                },
                doctorRules: {
                    Username: [
                        { required: true,validator: validateUser, trigger: 'blur' },
                        { min: 5, max: 10,  message: 'The length should be between 5 and 10 characters', trigger: 'blur'}
                    ],
                    Password: [
                        { required: true, message: 'Please enter password!', trigger: 'blur'},
                        { min: 6, max: 12,  message: 'The length should be between 6 and 12 characters', trigger: 'blur'}
                    ],
                    Confirm: [
                        { required: true,validator: validateDocConfirm, trigger: 'blur'}
                    ],
                    FirstName: [
                        { required: true, message: 'Please enter first name', trigger: 'blur'},
                    ],
                    LastName: [
                        { required: true, message: 'Please enter last name', trigger: 'blur'},
                    ],
                    Organization: [
                        { required: true, message: 'Please enter Organization', trigger: 'blur'},
                    ],
                    Background: [
                        { required: true, message: 'Please choose background', trigger: 'change'},
                    ],
                }
            }
        },
        methods: {
            register(formname){
                var username = this.userInfo.Username;
                var password = this.userInfo.Password;
                var registerInfo = {
                    'username' : username,
                    'password': password
                };
                this.$refs[formname].validate((valid) => {
                    if (valid) {
                        // 让注册按钮显示为loading
                        this.userInfo.loading = true;
                        https.fetchPost('register', registerInfo).then((res) => {
                        // 让注册按钮恢复
                        this.userInfo.loading = false;
                        if (res.data['code'] === 200) {
                            this.dialogVisible3 = true;
                            return true;
                        }else{
                            this.dialogVisible2 = true;
                            return false;
                        }
                        })
                    }else {
                        this.dialogVisible1 = true;
                        return false;
                    }
                });
            },
            registerDoc(formname){
                var username = this.doctorInfo.Username;
                var password = this.doctorInfo.Password;
                var name = this.doctorInfo.FirstName +' '+ this.doctorInfo.LastName;
                var organization = this.doctorInfo.Organization;
                var background = this.doctorInfo.Background;
                var registerInfo = {
                    'username' : username,
                    'password': password,
                    'name': name,
                    'organization':organization,
                    'background': background,
                };
                this.$refs[formname].validate((valid) => {
                    if (valid) {
                        // 让注册按钮显示为loading
                        this.doctorInfo.loading = true;
                        https.fetchPost('registerDoc', registerInfo).then((res) => {
                        // 让注册按钮恢复
                        this.doctorInfo.loading = false;
                        if (res.data['code'] === 200) {
                            this.dialogVisible3 = true;
                            return true;
                        }else{
                            this.dialogVisible2 = true;
                            return false;
                        }
                        })
                    }else {
                        this.dialogVisible1 = true;
                        return false;
                    }
                });
            },
            goToLogin() {
                this.dialogVisible3 = false;
                this.$router.push("/login");
            }
        }
    }
</script>


<style lang="less" scoped>

    .registerForm {
        // background-color: #9ec1f0;
        height: 100%;
        .register_box {
        width: 650px;
        // height: 300px;
        background-color: #fff;
        border-radius: 3px;
        position: absolute;
        left: 50%;
        top: 10%;
        transform: translate(-50%, -50%);
        }
    }
    .avator_box {
        z-index:1;
        height: 130px;
        width: 130px;
        border: 1px solid #eee;
        border-radius: 40%;
        padding: 10px;
        box-shadow: 0 0 10px #ddd;
        position: absolute;
        left: 50%;
        transform: translate(-50%, -50%);
        img {
            height: 100%;
            width: 100%;
            border-radius: 40%;
            background-color: #eee;
        }
    }
    .register_form{
        z-index:-1;
        position: absolute;
        top: 0;
        width: 100%;
        box-sizing: border-box;
        .user_register{
            height:240px;
            margin-top:5%;
            padding: 0 80px;
        }
        .doc_register{
            height:530px;
            margin-top:5%;
            padding: 0 80px;
        }
    }
    .btns{
        text-align:center
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

</style>