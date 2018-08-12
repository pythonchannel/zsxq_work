# 星球作业6#

import re
import time

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

request_url = "https://search.bilibili.com/all?keyword=Python&from_source=banner_search&spm_id_from=333.334.banner_link.1&page={}"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'finger=edc6ecda; buvid3=A3A829DB-C0C6-4A4F-B7D5-2BD1407EE7F06721infoc; LIVE_BUVID=AUTO5315316677538879; fts=1531668311; sid=i1gej45n',
    'Host': 'search.bilibili.com',
    'Referer': 'https://www.bilibili.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'

}

for i in range(1, 51):
    request_url = "https://search.bilibili.com/all?keyword=Python&page={}".format(i)
    print(request_url)
    time.sleep(1)
    print('第{}页'.format(i) + '\n')

    response = requests.get(url=request_url, headers=headers)  # 一定要加headers，规范写法，就像过马路一样穿红灯有时没事，有时要命！
    # print(response.status_code)
    if response.status_code == 200:  # 注意：这里一定要做200判断，
        html = response.text

        # 需要仔细分析一下，知道用什么连接，查找,不熟的朋友，记得自己去查一下正则怎么使用
        str = '<li.*?video matrix.*?href="(.*?)".*?title="(.*?)".*?icon-playtime"></i>(.*?)</span>.*?icon-date"></i>(.*?)</span>.*?up-name">(.*?)</a>.*?</div>'
        pattern = re.compile(str, re.S)
        subjects = re.findall(pattern, html)  # 注意这里是全文查找，得到的对象是一个列表

        for sub in subjects:
            herf = sub[0].replace('//', '')  # 替换掉前面的//
            title = sub[1].strip()
            views = sub[2].strip()  # 清除左右的空字符串
            author = sub[3].strip()
            create_time = sub[4].strip()
            print(title, herf, views, author, create_time)
