from . import *
import base64
from datetime import datetime

class GetRecord(Resource):
    @auth.login_required
    def get(self, record_id):
        r = RecordModel.find_by_id(record_id)
        username = r.username
        if g.user.user_type!='doctor' and username != g.user.username:
            return jsonify(code=403, message="没有访问权限")

        commit_time = str(r.commit_time)
        symptoms = r.symptoms
        image_path = r.image_path
        try:
            with open(image_path, 'rb') as f:
                img_base64 = base64.b64encode(f.read()).decode('utf-8')
        except Exception as e:
            print(e)
            img_base64 = ''
        test_result = {
            'height': r.height,
            'left': r.left,
            'top': r.top,
            'width': r.width,
            'name': r.name,
            'score': r.score,
        }
        recordInfo = {
            'record_id': record_id,
            'username': username,
            'commit_time': commit_time,
            'symptoms': symptoms,
            'test_result': test_result,
            'img_base64': 'data:image/jpeg;base64,'+img_base64
        }
        return jsonify(code=200, recordInfo=recordInfo)

class GetChat(Resource):
    @auth.login_required
    def get(self, record_id):
        r = RecordModel.find_by_id(record_id)
        username = r.username
        if g.user.user_type!='doctor' and username != g.user.username:
            return jsonify(code=403, message="没有访问权限")
        totalInfo = []
        # 医生来访问只返回他自己和用户的聊天记录
        if g.user.user_type == 'doctor':
            chat = ChatModel.find_chat(g.user.username, record_id)
            content = []
            for c in chat:
                content.append({
                    'user_type': UserModel.find_by_username(c.sender).user_type,
                    'content': c.content,
                })
            chatInfo = {
                'name': '',
                'username': username,
                'user_type': 'user',
                'content': content
            }
            totalInfo.append(chatInfo)
        # 用户来访问返回他和所有医生的聊天记录
        else:
            u = r.doctors
            for user in u:
                chat = ChatModel.find_chat(user.username, record_id)
                content = []
                for c in chat:
                    content.append({
                        'user_type': UserModel.find_by_username(c.sender).user_type,
                        'content': c.content,
                    })
                chatInfo = {
                    'name': user.information[0].name,
                    'username': user.username,
                    'user_type': 'doctor',
                    'content': content
                }
                totalInfo.append(chatInfo)
        return jsonify(code=200, chatInfo=totalInfo)

        