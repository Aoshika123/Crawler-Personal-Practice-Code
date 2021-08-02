
import requests
import json
#药监局url是  url = 'http://scxk.nmpa.gov.cn:81/xk/'
#首页中对应的企业信息是通过ajax动态请求到的
'''
-url的域名都是一样的，只有携带的参数（id）不一样
-id值可以从首页对应的ajax请求到的json串中获取
-域名和id值拼接处一个完整的企业对应的详情页的url
-详情页的企业险情数据也是动态加载出来的
 观察后发现：
    -所有的post请求的url都是一样的，只有参数id值是不同的
    -如果我们可以批量获取多家企业的id后，就可以将url和id形成一个完整的详情页对应详情数据的ajax请求的url
'''
if __name__ == '__main__':
    #批量获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }
    id_list = []#存储企业的id
    all_data_list = []#存储所有企业详情数据
    #参数的封装
    for page in range(1,6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':''
        }

        #获取企业的id值
        json_ids = requests.post(url=url,data=data,headers=headers).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    #获取企业详情数据
    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(url=url,data=data,headers=headers).json()
        all_data_list.append(detail_json)
    #持久化存储
    fp = open('./AllData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)

    print("------------取得企业详情数据完毕--------------")
