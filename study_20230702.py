import asyncio
import json
import time
import urllib.parse
from datetime import datetime

import xlrd
from numpy.core.defchararray import isdigit
from rich.progress import Progress
from tqdm import tqdm

import config
import requests
from rich import print as print

from rich import pretty
from rich import print as print
from rich.console import Console as console
from rich.table import Table

pretty.install()
requests.packages.urllib3.disable_warnings()#清除出现https安全警告


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
import threading

# 定义一个线程类
class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def get_mes(pid):
    url = f"http://www.jxqingtuan.cn/pub/pub/vol/config/organization?pid={pid}"

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
    if len(response) == 0 :
        print(f"当前选择选项PID为        {pid}")
        return {},0
    else:
        # print = response
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

def gettittle():
    global datas
    url = config.url['get_title']
    res = requests.get(url,timeout=5).text
    res = json.loads(res)["list"][0]
    # print(res)
    id = res["id"]
    tittle = res["title"]
    url = res["url"]
    t = "第{}期".format(id) + tittle
    print("第{}期".format(id) + "青年大学习标题：" + tittle + "\n" + "青年大学习学习链接：" + url)
    return id, tittle, url

def get_person_info(token):
    info = {}
    url = config.url['get_person_info'] + token
    response = requests.request("GET", url, headers=config.headers,timeout=5)
    res = json.loads(response.text)
    # print(res)

    for key, value in res["vo"].items():

        info[key] = value
    # info['user_id'] = res['vo']['id']
    # info['name'] = res['vo']['username']
    # # address = res['vo']['address']
    # info['zhibu'] = res['vo']['danwei'] + res['vo']['zhibu']
    # info['openid'] = res['vo']['openid']
    # info['score'] = res['vo']['score']
    # info['wxname'] = res['vo']['wxname']
    # info['sex'] = res['vo']['sex']
    # info['brithday'] = res['vo']['brithday']
    # # print(res)


    try:
        user_id = res['vo']['id']
        name = res['vo']['username']
        return user_id, name, info
    except : print("错误！！！")



def get_score_viery(token,userid,title,info):
    url = f"http://www.jxqingtuan.cn/pub/pub/vol/classrecord/index?openid={token}&userId={userid}&page=1&pageSize=10"
    response = requests.request("GET", url, headers=config.headers,timeout=5)
    if len(json.loads(response.text)['vo']) > 0:
        res = json.loads(response.text)['vo'][0]
        # console.print_json(data = res)
        study_tittle = res['title']
        # print(res)
        if title == study_tittle:
            # console.print(f"[bold green]{study_tittle} 学习完成！[/bold green]")
            state = "success"
        else:
            # console.print("[bold red]Error:[/bold red] 学习失败!，请联系作者：lzmpt@qq.com")
            state = "false"
    else:
        console.print("[bold red]Error:[/bold red] 未查询到学习记录！")
        state = "false"

    table = Table(show_header=True, header_style="bold")

    # 添加表头
    table.add_column("标题", style="dim")
    table.add_column("内容", style="dim")

    # 添加数据行
    for key,value in info.items():
        table.add_row(str(key),str(value))

    table.add_row("学习标题", str(study_tittle))
    table.add_row("学习时间", str(res['addtime']))
    table.add_row("学习状态", str(state))
    table.add_row("仓库网址", str("https://github.com/ygxiuming/QN-big-study"))
    table.add_row("作者邮箱", str("lzmpt@qq.com"))

    # 打印表格
    console.print(table)






def addScoreInfo(token, userid,url):
    session = requests.session()
    session.headers.update(config.headers)

    payload = {
        "check":1,
        "type": 3,
        'title':"青年大学习",
        "url": url,
        "openid":token,
        "userId":userid
    }

    url = config.url['addscore']

    session.headers = {
        'Host': 'www.jxqingtuan.cn',
        'Connection': 'keep-alive',
        'Content-Length': '195',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; 23013RK75C Build/TKQ1.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5127 MMWEBSDK/20230604 MMWEBID/8031 MicroMessenger/8.0.38.2400(0x28002639) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
        'openid': f'{token}',
        'content-type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'http://www.jxqingtuan.cn',
        'X-Requested-With': 'com.tencent.mm',
        'Referer': f'http://www.jxqingtuan.cn/html/?accessToken={token}',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    encoded_payload = urllib.parse.urlencode(payload)
    response = session.post(url, data=encoded_payload)

    print(response.text)

def QN_study(accessToken,token,id,nid,name,subOrg):
    if len(subOrg) > 0:payload = {"accessToken": token,"course": id, "nid": nid, "cardNo": name, "subOrg": subOrg}
    else:payload = {"accessToken": token,"course": id,"subOrg": "0","nid": nid,"cardNo": name}
    payload = json.dumps(payload)
    print(payload)
    url = f"http://www.jxqingtuan.cn/pub/pub/vol/volClass/join?accessToken={accessToken}"
    headers = config.headers
    headers['openid'] = accessToken
    response = requests.request("POST", url, headers=headers, data=payload,timeout=5)
    print(response.text)
    # res = json.loads(response.text)
    if response.status_code == 200:
        return '青年大学习学习成功！！！'
    else:
        text = ("提交大学习导致未知错误：" + response.text)
        return text


def get_excel_info():
    data = []
    data_excel = xlrd.open_workbook('名单.xls')
    table = data_excel.sheets()[0]  # 通过索引顺序获取
    nid_list = table.col_values(colx=0)
    for i in range(1, len(nid_list)):
        info = {}
        text = table.row_values(i, start_colx=0, end_colx=None)
        if text[2] == '':
            sub = '四级组织'
        else:
            sub = '三级组织'
        info['nid'] = text[0]
        info['name'] = text[1]
        info['subOrg'] = text[2]
        info['token'] = text[3]
        data.append(info)
    return data


def main(token,nid,name,id,tittle,subOrg,url):
    global error
    print(f'{tittle}\nNID: {nid}\nName: {name}\n{subOrg}\n')
    try:
        userid, name,info = get_person_info(token)
        addScoreInfo(token, userid,url)
        QN_study(token, token, id, nid, name, subOrg)
        get_score_viery(token, userid,tittle,info)
    except Exception as e:
        print("main 函数出现错误，错误为：",e)
        info_list = {}
        info_list['nid'] = nid
        info_list['name'] = name
        info_list['error'] = e
        error.append(info_list)



if __name__ == '__main__':
    console = console(color_system='256', style=None)
    console.rule("江西青年大学习学习交流脚本")
    print(tittle)
    agree = int(input("是否同意以上声明，同意（请输入1），不同意（请输入0） ："))
    error = []
    model = '''
####################################################################
         使用说明：
             将名单.xlsx表格与该程序放置同一目录下，填写相关学习名单信息，
         其中组织代码pid可通过该程序的模块1可查询，如果是三级组织需填写班级
         信息，若是四级组织不要填写班级信息空着即可。
            填写完成之后运行该程序的模块2即可批量学习！
            若出现问题可前往以下网址提交issu
        
         https://github.com/ygxiuming/QN-big-study

####################################################################

                            1.青年大学习组织id查询

                            2.青年大学习开始批量学习   

####################################################################
    '''
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
                # data = get_excel_info()
                # id, tittle, url = gettittle()
                # for i in tqdm(data):
                #     token = i['token']
                #     nid = i['nid']
                #     name = i['name']
                #     subOrg = i['subOrg']
                #     console.rule()
                #     main(token,nid,name,id,tittle,subOrg,url)
                #     console.rule()

                data = get_excel_info()
                id, tittle, url = gettittle()

                processes = []
                for i in tqdm(data):
                    token = i['token']
                    nid = i['nid']
                    name = i['name']
                    subOrg = i['subOrg']
                    thread = threading.Thread(target=main, args=(token, nid, name, id, tittle, subOrg,url))
                    processes.append(thread)
                    thread.start()
                    # 等待线程完成
                    processes[-1].join()

                print(error)



    time.sleep(1000)
