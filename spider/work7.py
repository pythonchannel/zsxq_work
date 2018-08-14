# 星球作业7#

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

'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Cookie':'buvid3=A93D5B77-8C62-443B-B1DA-A2B1375B1042103078infoc; LIVE_BUVID=AUTO8815275931693139; fts=1527593172; sid=kk3ktj5e; finger=edc6ecda',
'Host':'api.bilibili.com',
'Referer':'https://search.bilibili.com/all?keyword=python&page=6',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

for i in range(1, 2):
    request_url = "https://api.bilibili.com/x/web-interface/search/type?jsonp=jsonp&search_type=video&highlight=1&keyword=python&page={}".format(i)
    print(request_url)
    time.sleep(1)
    print('第{}页'.format(i) + '\n')

    response = requests.get(url=request_url, headers=headers)  # 一定要加headers，规范写法，就像过马路一样穿红灯有时没事，有时要命！
    # print(response.status_code)
    if response.status_code == 200:  # 注意：这里一定要做200判断，
        datas = json.loads(response.content).get('data').get('result')
        print(datas)
        for data in datas:
            herf = data['arcurl']  # 替换掉前面的//
            title = data['title']
            views = data['video_review']  # 清除左右的空字符串
            author = data['author']
            create_time = data['senddate']
            print(title, herf, views, author, create_time)
