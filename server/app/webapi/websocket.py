from . import *

@socketio.on('test', namespace='/test')   # 监听前端发回的包头 test ,应用命名空间为 api 
def test(params):  # 此处可添加变量，接收从前端发回来的信息
    print('触发test函数')
    print('接收到参数：',params)
    socketio.emit('test', {'data': 'test_OK'}, namespace='/test') # 此处 api 对应前端 sockets 的 api 

@socketio.on('join', namespace='/test')
def join(params):
    username = params['username']
    record_id = params['record_id']
    room = "username:"+str(username)+"record_id:"+str(record_id)
    join_room(room)
    socketio.emit('join', {'data':username + ' has entered the room.'}, room=room, namespace='/test')

@socketio.on('send', namespace='/test')
def send(params):
    c = ChatModel(params['record_id'], params['receiver'], params['sender'], params['content'])
    c.add_record()
    u = UserModel.find_by_username(params['sender'])
    name = ''
    user_type = u.user_type
    if u.user_type == 'doctor':
        r = RecordModel.find_by_id(params['record_id'])
        r.doctors.append(u)
        r.add_record()
        name = u.information[0].name
    receiver = params['receiver']
    record_id = params['record_id']
    room = "username:"+str(receiver)+"record_id:"+str(record_id)
    socketio.emit('send', {'content': params['content'], 'sender': params['sender'], 'user_type': user_type, 'name':name}, room=room, namespace='/test')