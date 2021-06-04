from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from flask_socketio import SocketIO
# 导入配置文件
from config import DevelopConfig
from config import ProductConfig
 
# 初始化应用实例
app = Flask(__name__)
 
# 添加配置信息
app.config.from_object(DevelopConfig)

#添加websocket协议
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')

# 使应用支持跨域资源访问
CORS(app, supports_credentials=True)

# 创建api实例
api = Api(app)
 
# 初始化数据库
db = SQLAlchemy(app)

# 初始化auth认证
auth = HTTPTokenAuth(scheme="JWT")

from .webapi.detectApi import Detect
from .webapi.registerView import CheckUsername,RegisterDoc,Register
from .webapi.loginView import Login
from .webapi.mainView import BuildRecord
from .webapi.recordView import GetRecord, GetChat
from .webapi.doctorView import ShowRecord
from .webapi.websocket import test, join, send


api.add_resource(Detect, '/api/detect', endpoint='detect')
api.add_resource(CheckUsername, '/api/checkUsername', endpoint='checkUsername')
api.add_resource(Register, '/api/register', endpoint='register')
api.add_resource(RegisterDoc, '/api/registerDoc', endpoint='registerDoc')
api.add_resource(Login,'/api/login', endpoint='login')
api.add_resource(BuildRecord, '/api/buildRecord', endpoint='buildRecord')
api.add_resource(GetRecord, '/api/getRecord/<int:record_id>', endpoint='getRecord')
api.add_resource(ShowRecord, '/api/showRecord/<int:page>', endpoint='showRecord')
api.add_resource(GetChat, '/api/getChat/<int:record_id>', endpoint='getChat')