import requests
import json
requests.packages.urllib3.disable_warnings()
#https://h5.cyol.com/special/daxuexi/dp1bsq1us7/images/end.jpg
def gettittle():
    url = "http://www.jxqingtuan.cn/pub/vol/volClass/current"
    res = requests.get(url).text
    res = json.loads(res)
    id = res["result"]["id"]
    tittle = res["result"]["title"]
    url =  res["result"]["uri"]
    t = "第{}期".format(id) + tittle
    print("第{}期".format(id) + "青年大学习标题：" + tittle   + "\n" + "青年大学习学习链接：" + url)
    return url

def sav_image(url,tittle):
    s = s = url.split('/')[-2]
    img_url = 'https://h5.cyol.com/special/daxuexi/%s/images/end.jpg'%s
    print('青年大学习学习截图：' + img_url)
    img = requests.get(img_url,verify=False)
    f = open('%s.jpg'%tittle, 'ab')  # 存储图片，多媒体文件需要参数b（二进制文件）
    f.write(img.content)  # 多媒体存储content
    f.close()

if __name__ == '__main__':
    url = gettittle()
    sav_image(url,'青年大学习学习截图')
