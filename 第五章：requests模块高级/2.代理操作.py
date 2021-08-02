#需求：
import requests
url = 'http://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
}
page_text = requests.get(url=url,headers=headers,proxies={'https':'217.175.35.72'}).text
with open('./ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)