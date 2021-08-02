import time
from multiprocessing.dummy import Pool
import requests
import re
from lxml import etree
import random
import os
#需求：爬取梨视频的视频数据
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
}
#原则：线程池处理的是阻塞且较为耗时的操作

#对下述url发起请求解析出水平详情页的url和视频的名称
url = 'https://www.pearvideo.com/category_5'
session = requests.session()
page_text = session.get(url=url,headers=headers).text
content_name_url = []
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
for li in li_list:
    detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'

    #因为视频为json动态加载，需要在XHR中查找json数据
    url_2 = 'https://www.pearvideo.com/videoStatus.jsp?'
    headers_1 = {
        'Referer':detail_url,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
    }
    #conId为主页面获取得detail_url后的一串数字
    params = {
        'contId':detail_url.split('_')[-1],
        'mrd': str(random.random())
    }

    each_response = session.get(url=url_2,params=params,headers=headers_1).json()

    #下面为json数据
    # resultCode: "1", resultMsg: "success", reqId: "6c5eac38-53ba-4509-b039-3e334a65b0b8",…}
    # reqId: "6c5eac38-53ba-4509-b039-3e334a65b0b8"
    # resultCode: "1"
    # resultMsg: "success"
    # systemTime: "1627005110892"
    # videoInfo: {playSta: "1", video_image: "https://image2.pearvideo.com/cont/20210722/12033417-164902-1.png",…}
    # playSta: "1"
    # video_image: "https://image2.pearvideo.com/cont/20210722/12033417-164902-1.png"
    # videos: {hdUrl: "", hdflvUrl: "", sdUrl: "", sdflvUrl: "",…}
    # hdUrl: ""
    # hdflvUrl: ""
    # sdUrl: ""
    # sdflvUrl: ""
    # srcUrl: "https://video.pearvideo.com/mp4/third/20210722/1627005110892-12033417-164855-hd.mp4"
    str_1 = each_response['videoInfo']['videos']['srcUrl']
    #srcUrl: "https://video.pearvideo.com/mp4/third/20210722/1627005110892-12033417-164855-hd.mp4"为假的链接，查询结果为404，
    #真正的链接为srcUrl: "https://video.pearvideo.com/mp4/third/20210722/cont-1733139-12033417-164855-hd.mp4"
    cont_str = 'cont-'+detail_url.split("_")[-1]
    re_1 = "(.*)/.*?-(.*)"
    b = re.findall(re_1,str_1)
    new_detail_url = b[0][0]+'/'+cont_str+'-'+b[0][1]
    content_name_url.append({'name':name,'loc':new_detail_url})

#创建文件夹
if not os.path.exists('./梨视频'):
    os.mkdir('./梨视频')

#分装线程池
def get_content(dic):
    #请求数据
    video_data = session.get(url=dic['loc'],headers=headers_1).content
    fp = open('./梨视频/'+dic['name'],'wb')
    fp.write(video_data)
    fp.close()

start_time = time.time()
#实例化Pool，定个数
pool = Pool(len(content_name_url))
#多线程运行
pool.map(get_content,content_name_url)
#关闭线程
pool.close()
#等待所有线程结束
pool.join()
end_time = time.time()
print(end_time-start_time)