# 星球作业4#

import requests
from lxml import etree
import time

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
    print('第{}页'.format(i)+'\n')

    response = requests.get(url=request_url, headers=headers)  # 一定要加headers，规范写法，就像过马路一样穿红灯有时没事，有时要命！
    # print(response.status_code)
    if response.status_code == 200:  # 注意：这里一定要做200判断，
        source = etree.HTML(response.text)

        '''方式二:这种直接从浏览器 选中元素，然后检查，右键-copy=> copy xpath 这种比较快，但有的时候并不准,如果不准，还是需要我们自行分析了'''
        divs = source.xpath('//*[@id="server-search-app"]/div[2]/div[2]/div/div[2]/ul/li')

        '''方式一：这种死抠xpath语法就行了，但需要我们自己来分析'''
        divs = source.xpath('//*[@class="video-contain clearfix"]/li')

        for div in divs:
            title = div.xpath('./div/div[1]/a/@title')
            herf = div.xpath('./div/div[1]/a/@href')
            views = div.xpath('./div/div[3]/span[1]/text()')
            author = div.xpath('./div/div[3]/span[4]/a/text()')
            create_time = div.xpath('./div/div[3]/span[3]/text()')

            # 因为得到的数据是列表，这里要做一下长度为空的判断
            title = title[0].strip() if len(title) > 0 else ''
            herf = str(herf[0]).replace('//', '') if len(herf) > 0 else ''
            views = views[0].strip() if len(views) > 0 else ''  # 清除左右的空字符串
            author = author[0].strip() if len(author) > 0 else ''
            create_time = create_time[0].strip() if len(create_time) > 0 else ''

            print(title, herf, views, author, create_time)
