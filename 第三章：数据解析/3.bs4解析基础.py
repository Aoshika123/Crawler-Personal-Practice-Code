
from bs4 import BeautifulSoup

if __name__ == '__main__':
    #将本地的html文档中的数据加载到该对象中
    fp = open('./text.html','r',encoding='utf-8')
    soup = BeautifulSoup( fp,'lxml')
    print(soup.select('.tang > ul > li > a')[0]['href'])
    #print(soup.a['href'])
