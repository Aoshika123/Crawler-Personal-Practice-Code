
'''
需求：破解百度翻译
-post请求(携带了参数)
-响应数据是一组json数据
'''
import requests
import json
if __name__ == '__main__':
    #1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #2.进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }
    #3.post请求参数处理（同get一样）
    word = input("enter a word:")
    data = {
        'kw':word
    }
    #4.发送请求
    response = requests.post(url=post_url,data=data,headers=headers)
    #5.获取响应数据：json（）方法返回的是obj（确定响应类型是json类型的才可以用json（））
    dic_obj = response.json()

    #持久化存储
    FileName = word+".json"
    fp = open(FileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print("over!")