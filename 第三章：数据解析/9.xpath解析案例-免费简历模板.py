import requests
import os
from lxml import etree

if __name__ == '__main__':

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }
    url = 'https://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9&issale=&classID=864&page=1'

    if not os.path.exists('./简历模板'):
        os.mkdir('./简历模板')
    response = requests.get(url=url,headers=headers).text
    tree = etree.HTML(response)
    #获取每个简历的下载地址
    url_list = tree.xpath('//div[@id="main"]/div/div')
    print(url_list)
    for i in url_list:
        new_url = 'https:'+ i.xpath('./a/@href')[0]
        page_text = requests.get(url=new_url,headers=headers).text
        new_tree = etree.HTML(page_text)
        #获取下载地址rar压缩包的地址
        rar_list = new_tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li[1]/a/@href')[0]
        #获取文件名
        rar_name = new_tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]+'.rar'
        rar_name = rar_name.encode('iso=8859-1').decode('utf-8')
        #持久化存储
        rar_data = requests.get(url=rar_list,headers=headers).content
        rar_path = '简历模板/'+rar_name
        with open(rar_path,'wb') as fp:
            fp.write(rar_data)
            print(rar_name,'下载成功！！')




