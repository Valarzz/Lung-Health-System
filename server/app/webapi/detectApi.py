from . import *
from ..baidu import check

class Detect(Resource):
    def post(self):
        req = request.json
        # 要把前面data...部分去掉再decod
        img_base64 = req.get('img_base64').split(',')[1]
        result = check(img_base64)
        if result == None:
            return jsonify(code=200, message="没有结果")
        predInfo = {
            'height': result['location']['height'],
            'left': result['location']['left'],
            'top': result['location']['top'],
            'width': result['location']['width'],
            'name': result['name'],
            'score': result['score']
        }
        return jsonify(code=200, predInfo=predInfo)