import requests
from bs4 import BeautifulSoup
#需求：爬取三国演义小说所有的章节标题和内容
#url：https://www.shicimingju.com/book/sanguoyanyi.html

if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }
    page_text = requests.get(url=url,headers=headers).content.decode('utf-8')

    #在首页解析出章节的标题和详情页的url
    #实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中去
    soup = BeautifulSoup(page_text,'lxml')
    #解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    print(li_list)
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.string #获取直系文本内容
        detail_url = 'https://www.shicimingju.com'+li.a['href']
        #对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url,headers=headers).content.decode('utf-8')
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        #解析到了章节的内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title+'打印成功！！')
