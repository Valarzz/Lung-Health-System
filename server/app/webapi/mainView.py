from . import *

class BuildRecord(Resource):
    @auth.login_required
    def post(self):
        req = request.json
        if req is None:
            return jsonify(code=403, message="未收到参数")

        symptoms = req.get('symptoms')
        username = g.user.username
        height = req.get('height')
        top = req.get('top')
        width = req.get('width')
        left = req.get('left')
        score = req.get('score')
        name = req.get('name')
        r = RecordModel(username, symptoms,height,top,width,left,score,name)
        r.add_record()
        id=r.id       
        img_base64 = req.get('img_base64').split(',')[1]
        import base64
        img = base64.b64decode(img_base64)
        with open("static/X-ray_image/"+str(id)+".png", 'wb')as f:
            f.write(img)
        r.image_path = "static/X-ray_image/"+str(id)+".png"
        db.session.commit()
        return jsonify(code=200, record_id = id)