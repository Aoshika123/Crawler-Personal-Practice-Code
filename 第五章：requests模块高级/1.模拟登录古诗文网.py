import requests
from lxml import etree
from hashlib import md5

#封装识别验证码图片的函数
def getCodeText(username,password,appId,imgUrl):
    class Chaojiying_Client(object):

        def __init__(self, username, password, soft_id):
            self.username = username
            password =  password.encode('utf8')
            self.password = md5(password).hexdigest()
            self.soft_id = soft_id
            self.base_params = {
                'user': self.username,
                'pass2': self.password,
                'softid': self.soft_id,
            }
            self.headers = {
                'Connection': 'Keep-Alive',
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
            }

        def PostPic(self, im, codetype):
            """
            im: 图片字节
            codetype: 题目类型 参考 http://www.chaojiying.com/price.html
            """
            params = {
                'codetype': codetype,
            }
            params.update(self.base_params)
            files = {'userfile': ('ccc.jpg', im)}
            r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
            return r.json()

        def ReportError(self, im_id):
            """
            im_id:报错题目的图片ID
            """
            params = {
                'id': im_id,
            }
            params.update(self.base_params)
            r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
            return r.json()


    if __name__ == '__main__':
        chaojiying = Chaojiying_Client(username, password, appId)	#用户中心>>软件ID 生成一个替换 96001
        im = open(imgUrl, 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        print(chaojiying.PostPic(im, 1902))												#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
        img_code = chaojiying.PostPic(im,1902)['pic_str']
        return img_code


if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
    }
    #创建一个session对象
    session = requests.Session()
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    page_text = session.get(url=url,headers=headers).text
    #解析验证码图片img中的src值
    tree = etree.HTML(page_text)
    code_img_src = 'https://so.gushiwen.org'+tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_data = session.get(url=code_img_src,headers=headers).content
    #将验证码图片保存到了本地
    with open('./code.jpg','wb') as fp:
        fp.write(img_data)

    #调用平台的示例程序进行验证码图片的数据识别
    result = getCodeText('aoshika','123456','919778','./code.jpg')
    print(result)

    #post请求的发送（模拟登录）
    login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

    # 获取动态变化的请求值
    __VIEWSTATE = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
    __VIEWSTATEGENERATOR = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]


    data = {
        '__VIEWSTATE': __VIEWSTATE,
        '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '415294978@qq.com',
        'pwd': '123456',
        'code': result,
        'denglu': '登录',
    }
    #使用session进行post请求的发送
    response = session.post(url = login_url,headers=headers,data=data)
    print(response.status_code)
    login_page_text = response.text

    with open('./gushiwen.html','w',encoding='utf-8') as fp:
        fp.write(login_page_text)

    new_url = 'https://so.gushiwen.cn/user/collectbei.aspx?sort=t'
    #手动cookie处理
    # headers = {
    #     'Cookie':'xxx'
    # }
    #使用携带了cookie的session进行get请求的发送
    detail_page_text = session.get(url=new_url,headers=headers).text
    with open('./aoshika.html','w',encoding='utf-8') as fp:
        fp.write(detail_page_text)