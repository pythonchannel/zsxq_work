# 星球作业6#

import re
import time
import json
import requests

'''
说明步骤:
1. 打开B站，打开搜索框，输入Python,可以看到很多 Python相关视频
2. 可以看到底部有很多分页的按钮,我随便点了几下，发现这里面是有规律的
3. 链接路径都是这样的 https://search.bilibili.com/all?keyword=Python&from_source=banner_search&spm_id_from=333.334.banner_link.1&page=7 ,只有最后一个page数不一样，其它都有一样
4. 构建网页请求路径 for i in range (50)
5. 然后根据网页内容抓取数据
6. 写代码了。
最后：等后面几节内容做完后，我会把代码进行一次大封装，用面向对象思维去编码,欢迎围观!
'''

headers = {
    'Host':'app.bilibili.com',
    'Accept':'*/*',
    'Connection':'keep-alive',
    'Display-ID':'515d8c137a45ff9e8f614a54d7df2958-1534254072',
    'Cookie	':'sid=8volmold',
    'Accept-Language':'zh-cn',
    'User-Agent':'bili-universal/6880 CFNetwork/902.2 Darwin/17.7.0',
    'Buvid':'515d8c137a45ff9e8f614a54d7df2958',
    'Accept-Encoding':'gzip'
    }

url = 'https://app.bilibili.com/x/v2/search?actionKey=appkey&appkey=27eb53fc9058f8c3&build=6880&device=phone&duration=0&from_source=apphistory_search&highlight=1&keyword=Python&mobi_app=iphone&order=default&platform=ios&pn={}&ps=20'

'''
说明：基于win
1. 安装charles 这个抓包工具简单而强大
2. 打开cmd 查看电脑的ip,然后在手机上选择与电脑同一wifi下，手动配置代理
3. 然后需要在手机上安装charles证书
4. 配置好代理后，打开app，就可以在charles上查看数据的动态变化，黄色闪烁就是有数据在变化
5. 记住在真正抓数据的时候，去掉勾选SSL Proxying


'''


for i in range(1, 50):
    request_url = url.format(i)
    print(request_url)
    time.sleep(1)
    print('第{}页'.format(i) + '\n')

    response = requests.get(url=request_url, headers=headers)  # 一定要加headers，规范写法，就像过马路一样穿红灯有时没事，有时要命！
    # print(response.status_code)
    if response.status_code == 200:  # 注意：这里一定要做200判断，
        print(response.content)
        datas = json.loads(response.content).get('data').get('item')
        if len(datas) == 0:
            break

        print(datas)
        for data in datas:
            herf = data['uri']  # 替换掉前面的//
            title = data['title']
            views = data['play']  # 清除左右的空字符串
            author = data['author']
         #   create_time = data['senddate']
            print(title, herf, views, author)
