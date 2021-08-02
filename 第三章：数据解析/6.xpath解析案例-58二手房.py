import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
    }
    url = 'https://cn.58.com/ershoufang/?PGTID=0d100000-008d-27d9-5455-5d08aa46a670'
    page_text = requests.get(url=url,headers=headers).text
    #数据解析
    #print(page_text)
    tree = etree.HTML(page_text)

    #存储的是div标签的对象
    div_list = tree.xpath('//section[@class="list"]/div')
    print(div_list)
    fp = open('58.txt','w',encoding='utf-8')
    for li in div_list:
        #局部解析
        title = li.xpath('.//div[@class="property-content-title"]/h3/@title')[0]
        score = li.xpath('.//div[@class="property-extra"]//span[@class="property-extra-text"]/text()')[1]
        print(title+"  "+score)
        fp.write(title+"---"+score+'\n')