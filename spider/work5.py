# 星球作业5#

import time

import requests
from bs4 import BeautifulSoup

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

for i in range(1,51):
    request_url = "https://search.bilibili.com/all?keyword=Python&page={}".format(i)
    print(request_url)
    time.sleep(1)
    print('第{}页'.format(i) + '\n')

    response = requests.get(url=request_url, headers=headers)  # 一定要加headers，规范写法，就像过马路一样穿红灯有时没事，有时要命！
    # print(response.status_code)
    if response.status_code == 200:  # 注意：这里一定要做200判断，
        html = response.text
        soup = BeautifulSoup(html, 'lxml')


        '''说明:bs4用法
        
        find_all是查找全文 
        find是查找第一个
        
        下面代码:
        find_all 这里是查找全部的li 标签，且属性class为video matrix的元素
        
        find 再进一步查找 前一个是标签,
        查a 标签下的属性class为 title的内容  
        get('herf') get('title') 这里是取标签内的元素
        get_text() 是取标签内的文本
        
        做的时候多想一下，每一句代码是啥意思
        
        '''


        items = soup.find_all('li', {'class': 'video matrix'})  # 查找标签为li，且属性为video matrix的元素
        for item in items:
            href = item.find('a', {'class': 'title'}).get('href').replace('//', '') # 去掉//
            title = item.find('a', {'class': 'title'}).get('title')
            views = item.find('span', {'class': 'so-icon watch-num'}).get_text().strip()    # 去掉空格
            create_time = item.find('span', {'class': 'so-icon time'}).get_text().strip().replace("('", "").replace(
                "',)", "") # 除去左右两边的括号
            author = item.find('a', {'class': 'up-name'}).get_text()

            print(href, title, views, create_time, author)
