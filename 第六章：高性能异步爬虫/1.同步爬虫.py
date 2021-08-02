import requests

urls = {
        'http://www.kfc.com.cn/kfccda/diet.html',
        'http://www.kfc.com.cn/kfccda/duty.html',
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
}

def get_content(url):
    print('正在爬取:',url)
    #get方法是一个阻塞的方法
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200 :
        return response.content

def parse_content(content):
    print('响应数据的长度为:',len(content))

for url in urls:
    content = get_content(url)
    parse_content(content)