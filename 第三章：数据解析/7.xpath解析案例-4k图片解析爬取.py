import requests
import os
from lxml import etree
if __name__ == '__main__':

    url = 'https://pic.netbian.com/4kmeishi/index_%d.html'

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }
    #创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    for num in range(1,3):
        new_url=format(url%num)
        page_text = requests.get(url=new_url,headers=headers).text
        #手动设定响应数据的编格式
        #response.encoding = 'utf-8'

        #数据解析:src的属性值  alt属性
        print(page_text)
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]/ul/li')
        print(li_list)


        for li in li_list:
            img_src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
            #通用处理中文乱码的解决方案
            img_name = img_name.encode('iso=8859-1').decode('gbk')

            #请求图片进行持久化存储
            img_data = requests.get(url=new_url,headers=headers).content
            img_path = 'picLibs/'+img_name
            with open(img_path,'wb') as fp:
                fp.write(img_data)
                print(img_name,img_src,'下载成功！！！')