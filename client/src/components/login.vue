<template>
    <div class="loginForm">
        <!-- 用来提示用户名或密码错误的消息框 -->
        <el-dialog
        title="登录失败"
        :visible.sync="dialogVisible"
        width=30%>
        <span>用户名或密码错误</span>
        <span slot="footer" class="dialog-footer">
            <el-button type="primary" @click="dialogVisible = false">确认</el-button>
        </span>
        </el-dialog>

        <!-- 用来提示不符合填写规范的消息框 -->
        <el-dialog
        title="提交失败"
        :visible.sync="dialogVisible1"
        width=30%>
        <span>请填写用户名和密码</span>
        <span slot="footer" class="dialog-footer">
            <el-button type="primary" @click="dialogVisible1 = false">确认</el-button>
        </span>
        </el-dialog>
        <div class="background"></div>
        <div class="login_box">

      <div class="avator_box">
        <img src="../assets/logo.png" alt />
      </div>

      <el-form label-width="0" class="login_form" ref="loginInfo" :rules="rules" :model="loginInfo">

        <el-form-item prop="username">
          <el-input v-model="loginInfo.username" prefix-icon="el-icon-user" placeholder="Please enter username"></el-input>
        </el-form-item>

        <el-form-item prop="password">
          <el-input v-model="loginInfo.password" prefix-icon="el-icon-lock" placeholder="Please enter password" type="password"></el-input>
        </el-form-item>
        
        <el-form-item>
        <el-checkbox v-model="loginInfo.remember" >Remember me</el-checkbox>
        </el-form-item>

        <el-form-item class="btns">
            <div style="text-align:center">
          <el-button type="primary" :loading="loginInfo.loading" @click="login('loginInfo')">
              <span v-if="!loginInfo.loading">Login</span>
              <span v-else>Loading</span>
          </el-button>
          <el-button type="info" @click="goToRegister">Register</el-button>
          </div>
        </el-form-item>
      </el-form>
    </div>
    </div>
</template>

<script>
  import https from '../api/https.js'
  import CryptoJS from 'crypto-js'
  const key = CryptoJS.enc.Utf8.parse('13579BDFFDB97531');
  const iv = CryptoJS.enc.Utf8.parse('02468ACEECA86420');
    export default {
        name: 'login',
        data() {
            return{
                dialogVisible: false,
                dialogVisible1: false,
                loginInfo:{
                    username: '',
                    password: '',
                    remember: false,
                    loading:false,
                },
                rules: {
                    username: [
                        { required: true, message: 'Please enter username!', trigger: 'blur' }
                    ],
                    password: [
                        { required: true, message: 'Please enter password!', trigger: 'blur' }
                    ]
                }
            }
        },
        mounted(){
            window.addEventListener('keydown',this.keyDown);
        },
        created () {
            let username = this.getCookie('username');
            let password = this.decrypt(this.getCookie('password'));
            if (username) {
                this.loginInfo.username = username;
                this.loginInfo.password = password;
                this.loginInfo.remember = true;
            }
        },
        methods: {
            keyDown(e){
                if(e.keyCode == 13 && this.$route.path === '/login'){
                    this.login('loginInfo');
                }
            },
            login(formName){
                var username = this.loginInfo['username'];
                var password = this.loginInfo['password'];
                var loginInfo = {'username': username,
                                 'password': password
                };
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.loginInfo.loading = true;
                        https.fetchPost('login', loginInfo).then((res) => {
                        if (res.data['code'] === 200) {
                            this.$store.commit('set_token', res.data['token']);
                            sessionStorage.setItem('token', res.data['token']);
                            this.setUserInfo();
                            this.$store.commit('set_user',res.data['user_type']);
                            this.$store.commit('set_username',username);
                            if(res.data.user_type === 'user'){
                                this.$router.push('/');
                            }
                            else{
                                this.$router.push('/history')
                            }
                            return true;
                        } else {
                            this.loginInfo.loading = false;
                            this.dialogVisible = true;
                            return false;
                        }
                        });
                    } else {
                        this.dialogVisible1 = true;
                        return false;
                    }
                });
            },
            setCookie (cName, value, expiredays) {
                var exdate = new Date();
                exdate.setDate(exdate.getTime() + expiredays);
                document.cookie = cName + '=' + value + ((expiredays == null) ? '' : ';expires=' + exdate.toGMTString());
            },
            getCookie (key) {
                if (document.cookie.length > 0) {
                var start = document.cookie.indexOf(key + '=');
                if (start !== -1) {
                    start = start + key.length + 1;
                    var end = document.cookie.indexOf(';', start);
                    if (end === -1) {
                    end = document.cookie.length;
                    }
                    return unescape(document.cookie.substring(start, end));
                }
                }
                return '';
            },
            setUserInfo () {
                if (this.loginInfo.remember) {
                    this.setCookie('username', this.loginInfo.username, 7);
                    let pwd = this.encrypt(this.loginInfo.password);
                    this.setCookie('password', pwd, 7);
                } else {
                    this.setCookie('username', '', null);
                    this.setCookie('password', '', null);
                }
            },
            decrypt (word) {
                let encryptedHexStr = CryptoJS.enc.Hex.parse(word);
                let srcs = CryptoJS.enc.Base64.stringify(encryptedHexStr);
                let decrypt = CryptoJS.AES.decrypt(srcs, key, { iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7 });
                let decryptedStr = decrypt.toString(CryptoJS.enc.Utf8);
                return decryptedStr.toString();
            },
            encrypt (word) {
                let srcs = CryptoJS.enc.Utf8.parse(word);
                let encrypted = CryptoJS.AES.encrypt(srcs, key, { iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7 });
                return encrypted.ciphertext.toString().toUpperCase();
            },
            destroyed(){
                window.removeEventListener('keydown',this.keyDown,false);
            },
            goToRegister(){
                this.$router.push('register')
            }
        }
    }
</script>


<style lang="less" scoped>

    .loginForm {
        // background-color: #9ec1f0;
        height: 100%;
        }
        .login_box {
        width: 450px;
        height: 350px;
        background-color: #fff;
        border-radius: 3px;
        position: absolute;
        left: 50%;
        top: 40%;
        transform: translate(-50%, -50%);
    }
    .avator_box {
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
    .login_form{
        position: absolute;
        bottom: 0;
        width: 100%;
        padding: 0 20px;
        box-sizing: border-box;
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