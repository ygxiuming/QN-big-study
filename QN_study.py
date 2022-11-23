import json
import requests
import xlrd
from numpy.core.defchararray import isdigit
import os
requests.packages.urllib3.disable_warnings()
tittle = '''
####################################################################
                  ___====-_  _-====___
            _--^^^#####//      \\#####^^^--_
         _-^##########// (    ) \\##########^-_
        -############//  |\^^/|  \\############-
      _/############//   (@::@)   \############\_
     _/#############((     \\//     ))#############\_
    -###############\\    (oo)    //###############-
   -#################\\  / VV \  //#################-
  -###################\\/      \//###################-
 _#/|##########/\######(   /\   )######/\##########|\#_
 |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
 `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
    `   `  `      `   / | |  | | \   '      '  '   '
                     (  | |  | |  )
                    __\ | |  | | /__
                   (vvv(VVV)(VVV)vvv)

     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               神兽保佑            永无BUG

github:https://github.com/ygxiuming/QN-big-study
               
                        使用声明
       本源代码是本人利用时间的写成，《免费》向编程爱好者学习使用！
                    本源禁止使用商业非法用途！
            本源代码无任何恶意代码！所造成的损失等概与本人无关
                使用编译本原始码即取代同意上述声明
                                                ——————修明
####################################################################
'''



def get_mes(pid):
    url = f"http://www.jxqingtuan.cn/pub/vol/config/organization?pid={pid}"

    payload = {}
    headers = {
        'Host': 'www.jxqingtuan.cn',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b21) NetType/WIFI Language/zh_CN',
        'Referer': 'http://www.jxqingtuan.cn/html/h5_index.html',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'X-Requested-With': 'XMLHttpRequest',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    print("")
    response = json.loads(response.text)
    response = response["result"]
    response_len = len(response)
    k = {}
    num = []
    for i in response:
        tittle = i['title']
        id = i['id']
        k["{}".format(tittle)] = id
    num = list(k.values())
    return k,num

def id_getinfo():
    list_tittle = {"团省委机关": "N0017",
                   "省直属单位团委": "N0016",
                   "省属本科院校团委": "N0013",
                   "非省属本科院校团委": "N0014",
                   "高职专科院校团委": "N0015",
                   "南昌市": "N0002",
                   "九江市": "N0003",
                   "景德镇市": "N0004",
                   "萍乡市": "N0005",
                   "新余市": "N0006",
                   "鹰潭市": "N0007",
                   "赣州市": "N0008",
                   "宜春市": "N0009",
                   "上饶市": "N0010",
                   "吉安市": "N0011",
                   "抚州市": "N0012"
                   }
   #第一级
    t=0
    while(1):
        if t == 0:
            i = 0
            samp = list(list_tittle.values())
            print("请输入相应序号！")
            for k in list_tittle:
                print(str(i + 1) + "." + str(k) + ":" + str(list_tittle[k]))
                i = i + 1
            t = input("请输入对应序号:")
            if isdigit(t):
                t = int(t)
            else:
                break

            pid = samp[t - 1]
        elif t == 'q':
            break
        else:
            list1,num = get_mes(pid)
            i = 0
            for k in list1:
                print(str(i+1) + "." + str(k) + ":" + str(list1[k]))
                i = i + 1
            t = input("请输入对应序号(输入0重新查询,输入q退出查询！):")
            if isdigit(t):
                t = int(t)
            else:
                break
            if t !=0 :
                pid = num[t - 1]
            else:
                pass

def getIDInfo():
    url = "http://www.jxqingtuan.cn/pub/vol/config/organization?pid=" + nid
    response = requests.get(url)
    if response.content:
        res = json.loads(requests.get(url).text)
    if res.get("status") == 200:
        print(str(res.get("result")) + str(res.get("status")))
        return res.get("result")
    else:
        print("查询组织导致未知错误：" + res.text)
        exit()


def getStudy(course, nid, subOrg, cardNo):
    global datas
    url = "http://www.jxqingtuan.cn/pub/vol/volClass/join?accessToken="
    if len(subOrg) > 0:
        data = {"course": course, "nid": nid, "cardNo": cardNo, "subOrg": subOrg}
    else:
        data = {"course": course, "nid": nid, "cardNo": cardNo}
    response = requests.post(url=url, data=json.dumps(data))
    print(response.text)
    if response.content:
        res = json.loads((requests.post(url=url, data=json.dumps(data))).text)
    if res.get("status") == 200:
        return '青年大学习学习成功！！！'
    else:
        text = ("提交大学习导致未知错误：" + res.text)
        return text

def gettittle():
    global datas
    url = "http://www.jxqingtuan.cn/pub/vol/volClass/current"
    res = requests.get(url).text
    res = json.loads(res)
    id = res["result"]["id"]
    tittle = res["result"]["title"]
    url =  res["result"]["uri"]
    t = "第{}期".format(id) + tittle
    print("第{}期".format(id) + "青年大学习标题：" + tittle   + "\n" + "青年大学习学习链接：" + url)
    return id,t,url

def sav_image(url,tittle):
    s = s = url.split('/')[-2]
    img_url = 'https://h5.cyol.com/special/daxuexi/%s/images/end.jpg'%s
    print('青年大学习学习截图：' + img_url)
    if os.path.exists('./青年大学习学习截图'):
        pass
    else:
        os.makedirs('./青年大学习学习截图')

    img = requests.get(img_url,verify=False)
    f = open('./青年大学习学习截图/%s.jpg'%tittle, 'ab')  # 存储图片，多媒体文件需要参数b（二进制文件）
    f.write(img.content)  # 多媒体存储content
    f.close()


def QNstudy():
    id,tit,url_study = gettittle()
    data_excel = xlrd.open_workbook('名单.xls')
    table = data_excel.sheets()[0]  # 通过索引顺序获取
    nid_list = table.col_values(colx=0)
    for i in range(1,len(nid_list)):
        text = table.row_values(i,start_colx=0,end_colx=None)
        if text[2] == '':
            sub = '四级组织'
        else:
            sub = '三级组织'
        nid = text[0]
        name = text[1]
        subOrg = text[2]
        tx = getStudy(id, nid, subOrg, name)
        message = f'''
 #################################################################
         第{id}期青年大学习：{tit}
         序号：第{i}个学习
         组织id：{nid}
         组织级别：{sub}
         姓名：{name}
         班级：{subOrg}（四级组织无班级选项）
         学习状态：{tx}
 #################################################################
'''
        print(message)


if __name__ == '__main__':
    print(tittle)
    model = '''
 #########################使用说明###################################
     使用说明：
         将名单.xlsx表格与该程序放置同一目录下，填写相关学习名单信息，
     其中组织代码pid可通过该程序的模块1可查询，如果是三级组织需填写班级
     信息，若是四级组织不要填写班级信息空着即可。
        填写完成之后运行该程序的模块2即可批量学习！
        若出现问题可前往以下网址提交issu
        
     https://github.com/ygxiuming/QN-big-study
     
 ###########################模块选择################################
 
                        1.青年大学习组织id查询
                        
                        2.青年大学习开始批量学习   
           
 ####################################################################
'''
    agree = input("是否同意以上声明，同意（请输入1），不同意（请输入0） ：")

    if agree == 0:
        print("请关闭软件，出门右走谢谢！")
    else:
        while 1:
            print(model)
            mod = int(input("请输入选择模式序号："))
            if mod == 1 :
                id_getinfo()
                print("已返回模块选择界面！！！")
            else:
                QNstudy()
                print("已经全部学习完成！请查看输出历史记录！")
                print("已返回模块选择界面！！！")
