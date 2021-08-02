
import requests
import json
if __name__ == '__main__':
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    address = input("请输入要查询的地址：")
    data = {
        'cname':'',
        'pid':'',
        'keyword': address,
        'pageIndex': '1',
        'pageSize': '10'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }
    response = requests.post(url=post_url,data=data,headers=headers)
    print(type(response.text))
    KFC_data = response.json()
    fp = open('./KFC_Address.json','w',encoding='utf-8')
    json.dump(KFC_data,fp=fp,ensure_ascii=False)

    print("Test is over!")