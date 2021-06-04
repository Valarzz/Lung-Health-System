import urllib.request
import base64
import json
import click

'''
easydl image detection
'''

@click.command()
@click.option('--image', help='Input your image path')
def get_results(image):
    """
    Using Baidu EasyDL computer vision API to check what's wrong with your lung.
    The detection API contains 8 different kinds of lung disease:
    Atelectasis, Cardiomegaly, Effusion, Infiltrate, Mass, Nodule, Pneumonia, Pneumothorax.

    If the image shows a healthy lung, then a 'None' will return.
    If certain diseases have been found, then a dictionary which includes the location, name and confidence of the diseases will return
    """
    request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/llung"
    with open(image, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode('UTF8')

    params = {"image": s, "top_num": "5"}
    params = json.dumps(params).encode('utf-8')
    access_token = '24.0b44fc1a2c405a2b7847669b49da44d6.2592000.1625319189.282335-24305682'
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        content = eval(content.decode('UTF8'))['results'][0]
        print(content)
    return content


if __name__ == '__main__':
    result = get_results()



