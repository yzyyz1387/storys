import requests
import json


# 可选国家: en-US, zh-CN, ja-JP, en-AU, en-UK, de-DE, en-NZ
def get_img():
    url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    data1 = 'https://cn.bing.com/'
    html = requests.get(url).text  # 获取这个网页源码
    text = json.loads(html)
    data = text['images'][0]['url']
    img = data1 + data
    return img


if __name__ == '__main__':
    get_img()
