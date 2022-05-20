import json

import requests


def getIDInfo():
    url = "http://osscache.vol.jxmfkj.com/pub/vol/config/organization?pid=" + nid
    response = requests.get(url)
    if response.content:
        res = json.loads(requests.get(url).text)
    if res.get("status") == 200:
        print(str(res.get("result")) + str(res.get("status")))
        return res.get("result")
    else:
        print("查询组织导致未知错误：" + res.text)
        exit()


def getStudy(course, nid, subOrg, cardNo, i,tit):
    global datas
    url = "http://osscache.vol.jxmfkj.com/pub/vol/volClass/join?accessToken="
    if len(subOrg) > 0:
        data = {"course": course, "nid": nid, "cardNo": cardNo, "subOrg": subOrg}
    else:
        data = {"course": course, "nid": nid, "cardNo": cardNo}
    response = requests.post(url=url, data=json.dumps(data))
    if response.content:
        res = json.loads((requests.post(url=url, data=json.dumps(data))).text)
    if res.get("status") == 200:
        num = "班级：" + str(subOrg) + "  学院NID：" + str(nid) + "  姓名：" + str(cardNo)
        print( str(i+1) +"、姓名：" + str(cardNo) + '\n' + num + '\n' + str(res) + '\n' + str(cardNo) + tit + "大学习成功！" + '\n\n')
    else:
        print("提交大学习导致未知错误：" + res.text)

def gettittle():
    global datas
    url = "http://osscache.vol.jxmfkj.com/pub/vol/volClass/current"
    res = requests.get(url).text
    res = json.loads(res)
    id = res["result"]["id"]
    tittle = res["result"]["title"]
    url =  res["result"]["uri"]
    t = "第{}期".format(id) + tittle
    print("第{}期".format(id) + "青年大学习标题：" + tittle   + "\n" + "青年大学习学习链接：" + url)
    return id,t


def QNstudy():
    id,tit = gettittle()
    f = open('mingdan.txt', encoding='utf-8')
    list1 = []
    for line in f:
        t = line.split()
        list1.append(t)
    for i in range(len(list1)):
        list2 = list1[i]
        subOrg = list2[1]
        nid = list2[0]
        name = list2[2]
        getStudy(id, nid, subOrg, name, i,tit)

if __name__ == '__main__':
    QNstudy()


