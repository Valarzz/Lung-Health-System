import urllib.request
import base64
import json

'''
easydl图像分类
'''
def check(img_base64):
    request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/llung"

    params = {"image": img_base64, "top_num": "5"}
    params = json.dumps(params).encode('utf-8')
    access_token = '24.0b44fc1a2c405a2b7847669b49da44d6.2592000.1625319189.282335-24305682'
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    try:
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            results = eval(content.decode('UTF8'))['results'][0]
            return results
    except Exception as e:
        print(e)
        return None


