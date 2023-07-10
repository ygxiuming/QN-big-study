<h1 align="center">江西青年大学习批量过后台</h1>
<h1 align="center">适用于2023新版青年大学习善德教育系统</h1>
<p align="center">
    <a href="https://github.com/ygxiuming/QN-big-study/issues" style="text-decoration:none">
        <img src="https://img.shields.io/github/issues/ygxiuming/QN-big-study.svg" alt="GitHub issues"/>
    </a>
    <a href="https://github.com/ygxiuming/QN-big-study/stargazers" style="text-decoration:none" >
        <img src="https://img.shields.io/github/stars/ygxiuming/QN-big-study.svg" alt="GitHub stars"/>
    </a>
    <a href="https://github.com/ygxiuming/QN-big-study/network" style="text-decoration:none" >
        <img src="https://img.shields.io/github/forks/ygxiuming/QN-big-study.svg" alt="GitHub forks"/>
    </a>
    <a href="https://github.com/ygxiuming/QN-big-study/blob/master/LICENSE" style="text-decoration:none" >
        <img src="https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg" alt="GitHub license"/>
    </a>
</p>
<h3 align="center">不断更新中....</h3>


 ### 环境：
    requests<br>
    xlrd == 1.2.0 //最新版xlrd==2.0.1不支持xlsx文件的读取<br>
    python3.6以上<br>

<br>
<h2>功能：</h2>
<p> 新设团委id查询</p>
<p> 批量学习(不限制学校，班级，全自动化)</p>
理论上江西省所有学校所有专业都适用，请自行测试
<p> 增加青年大学习学习截图功能，可供选择批量产生截图</p>
<p> 添加docker在GitHub action 定时运行</p>
<p> accesstoken可以在记录后台获取，目前正在写批量获取脚本，目前先自行获取。<p>
<p>后台地址：http://106.225.141.143:8103  然后按F12可以找得到，也可以自行抓包获取，填入对应excel中即可<p>
<p> 仅仅测试少量数据，若有问题，请发issue<p>
<br>
<br>

<h2>更新记录</h2>
2022/05/20 发布青年大学习单人学习<br>
2022/05/22 发布青年大学习多人学习版本<br>
2022/05/23 更新青年大学习脚本（江西共青团服务器更新）<br>
2022/09/26 关于xlrd模块版本说明<br>
2022/09/27 打包版本发布(仅仅适用于windows系统)<br>
2022/11/13 Cnlomou添加docker启动以及定时任务<br>
2022/11/14 推出单个学习截图以及批量导出学习截图功能<br>
2022/11/14 解决python版本对于xlrd不兼容问题     <br>   
2022/12/20 解决无法获取最新一期青年大学习的问题<br>   
2023/07/02 解决增加accesstoken验证  请使用study_20230702.py
2023/07/10 增加多线程，加快处理速度！

<br>
<br>
<br>

## GitHub action 定时运行使用说明
- 1.fork仓库到自己的仓库
- 2.下载仓库的`名单.xls`文件
- 3.按照下面的使用说明填写相关内容在`名单.xls`文件中，保存并上传至你fork的仓库。 [不会填写参数](#peizhi)
- 4.设置定时时间。   [怎么设置时间参数?](https://docs.github.com/cn/actions/using-workflows/events-that-trigger-workflows#schedule)
- 5.修改你fork 仓库内的`QN-big-study/blob/main/.github/workflows/docker-image.yml`内的文件(默认是每周3晚上9点多定时执行)
~~~
on:
   schedule:
    - cron: "20 13 * * 3"  #这里是每周3晚上9点多 
~~~
- 6.接下来可以关闭你的电脑，每周都会根据你的时间设定自动学习默认是每周3晚上9点多定时执行()。

<br>
<h2>使用说明：</h2>

### 将整个项目 Fork到自己仓库/拉取到本地/下载到本地
### pip3 install -r requirements.txt 安装依赖
<br>

<h3>step1:下载本仓库所有代码，运行QN_study.py程序，如下图所示</h3>
    <a href="https://github.com/ygxiuming/QN-big-study/tree/main/assets" style="text-decoration:none" >
        <img src="assets/1.png" alt="启动页面"/>
    </a>

<p id="peizhi">一共有两个模块，其中需要查询班级的组织id进行配置，请输入`1`进入`青年大学习组织id查询`如下图</p>
<a href="https://github.com/ygxiuming/QN-big-study/tree/main/assets" style="text-decoration:none" >
        <img src="assets/组织PID.png" alt="id查询页面"/>
</a>

<p>后方一串数字即为组织id，继续选择下去，直到班级。例如：N00130001******，记住他</p>

<h3>step2：配置相关学习数据，打开名单.xlsx，填入相关信息</h3>

<a href="https://github.com/ygxiuming/QN-big-study/tree/main/assets" style="text-decoration:none" >
        <img src="assets/excel.png" alt="配置页面"/>
</a>

<p>把刚刚记住的填入组织代码处，若是三级组织需要填写班级，若是四级组织，班级空着即可，不需要填写。保存即可</p>

<br>
<p>tips：excel文件一定要与程序位于同一个目录下，否则会出错！！！</p>

<h3>step3：再次打开程序，选择批量学习，即可完成学习！</h3>

<a href="https://github.com/ygxiuming/QN-big-study/tree/main/assets" style="text-decoration:none" >
        <img src="assets/study.png" alt="学习页面"/>
</a>


## 特别鸣谢
* [@Cnlomou](https://github.com/Cnlomou/QN-big-study)「Cnlomou」
<br>
1、接决依赖缺少问题
<br>
2、添加定时任务
<br>
3、添加docker启动


<br>

## &#8627; Stargazers

[![Stargazers repo roster for @ygxiuming/QN-big-study](https://reporoster.com/stars/ygxiuming/QN-big-study)](https://github.com/ygxiuming/QN-big-study/stargazers)

<br>

## &#8627; Forkers
[![Forkers repo roster for @ygxiuming/QN-big-study](https://reporoster.com/forks/ygxiuming/QN-big-study)](https://github.com/ygxiuming/QN-big-study/network/members)

<br>

<h1>程序打包资源</h1>

<p>
<a href ='https://wwd.lanzoum.com/b01pvee8j'>蓝奏云</a>
https://wwd.lanzoum.com/b01pvee8j 密码：8888


有问题请发issue，看到会回复！

<h1>最后的最后，可以给我一个star吗？万分感谢！</h1>
