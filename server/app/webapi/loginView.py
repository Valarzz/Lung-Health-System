from . import *

class Login(Resource):
    def post(self):
        req = request.json
        if req is None:
            return jsonify(code=403, message="未收到参数")

        user = UserModel.find_by_username(req.get("username"))

        if not user or not user.verify_password(req.get("password")):
            return jsonify(code=403, message="错误的用户名或密码")

        token = user.generate_auth_token()
        user_type = user.user_type
        return jsonify(code=200, message="成功", token=token, user_type=user_type)