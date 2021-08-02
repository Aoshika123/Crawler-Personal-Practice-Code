
# UA User-agent （请求载体的身份标识）
#UA伪装 ：让爬虫对应的请求载体身份标识伪装成某一款浏览器
#UA伪装：将对应的User-Agent封装到一个字典中
import requests

if __name__ == '__main__':
    url='https://www.sogou.com/web'
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }
    response = requests.get(url=url,params=param,headers=headers)
    FileName = kw+'.html'
    with open(FileName,'w',encoding='utf-8') as fp:
        fp.write(response.text)
    print(FileName+'输入完毕！')


