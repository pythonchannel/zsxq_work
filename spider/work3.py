# 星球作业3#

import requests

url = 'https://www.bilibili.com/'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'buvid3=A93D5B77-8C62-443B-B1DA-A2B1375B1042103078infoc; LIVE_BUVID=AUTO8815275931693139; fts=1527593172; sid=kk3ktj5e; bsource=seo_google; finger=edc6ecda',
    'Host': 'www.bilibili.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

response = requests.get(url=url, headers=headers)  # 一定要加headers，规范写法，就像过马路一样穿红灯有时没事，有时要命！
if response.status_code == 200:  # 注意：这里一定要做200判断，
    print(response.text)
