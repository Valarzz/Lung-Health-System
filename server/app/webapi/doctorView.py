from . import *
import base64

class ShowRecord(Resource):
    @auth.login_required
    def get(self, page):
        retInfo = []
        if g.user.user_type == 'doctor':
            r_page = RecordModel.pagination_doctor(page)
        else:
            r_page = RecordModel.pagination_user(page, g.user.username)
        for r in r_page.items:
            image_path = r.image_path
            try:
                with open(image_path, 'rb') as f:
                    img_base64 = 'data:image/jpeg;base64,'+base64.b64encode(f.read()).decode('utf-8')
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
                'symptoms': r.symptoms,
                'test_result': test_result,
                'img_base64': img_base64,
                'commit_time': str(r.commit_time),
                'username': r.username,
                'record_id': r.id,
            }
            retInfo.append(recordInfo)
        if page == 1:    
            return jsonify(code=200, message='返回成功', retInfo=retInfo, total=r_page.total)
        return jsonify(code=200, message='返回成功', retInfo=retInfo)