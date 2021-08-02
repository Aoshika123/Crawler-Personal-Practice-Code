import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    #解析到热门城市和所有城市对应的a标签
    #//div[@class="bottom"]/ul/li/         热门城市a标签的层级关系
    #//div[#class="bottom"]/ul/div[2]/li/a     全部城市a标签的层级关系
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names,len(all_city_names))