from . import *

class CheckUsername(Resource):
    def post(self):
        req = request.json
        if not req:
            return jsonify(code=403, message="未收到参数")
        user = UserModel.find_by_username(req.get("username"))
        if user:
            return jsonify(code=403, wrongType="username", message="用户名已被注册")
        return jsonify(code=200, message="用户名可注册！")

class Register(Resource):
    def post(self):
        req = request.json
        if req is None:
            return jsonify(code=403, message="未收到参数")

        username = req.get('username')
        password = req.get('password')
        u = UserModel(username=username)
        # 单独设置密码（调用加密函数）
        u.password = password
        u.add_user()
        return jsonify(code=200, message="注册成功！")

class RegisterDoc(Resource):
    def post(self):
        req = request.json
        if req is None:
            return jsonify(code=403, message="未收到参数")

        username = req.get('username')
        password = req.get('password')
        name = req.get('name')
        background = req.get('background')
        organization = req.get('organization')
        u = UserModel(username=username, user_type='doctor')
        # 单独设置密码（调用加密函数）
        u.password = password
        u.add_user()
        i = InformationModel(username,name,background, organization)
        i.add_information()
        return jsonify(code=200, message="注册成功！")