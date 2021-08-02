from hashlib import md5
import requests
from time import sleep
from selenium import webdriver
import base64
from selenium.webdriver import ActionChains

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
        return chaojiying.PostPic(im, 9004)['pic_str']										#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()

if __name__ == '__main__':

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
    }

    bro = webdriver.Chrome(executable_path='./chromedriver')
    bro.get('https://kyfw.12306.cn/otn/resources/login.html')

    a_tag = bro.find_elements_by_class_name('login-hd-account')[0]
    print(a_tag)
    a_tag.click()


    img_src = bro.find_element_by_id('J-loginImg')
    img_src_el = bro.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[4]/img')
    detail_img_src = img_src.get_attribute("src")#获得验证码图片的src，注意是base64类型，需要进行转化
    #img_data = requests.get(url=detail_img_src,headers=headers).content
    detail_img_src1 = detail_img_src.split("64,")[-1]#只需要获得64，的字符
    print(detail_img_src1)
    imgdata = base64.b64decode(detail_img_src1)#进行转码

    #将验证码图片保存到了本地
    with open('./code.jpg','wb') as fp:
        fp.write(imgdata)

    result = getCodeText('aoshika','123456','919778','./code.jpg')
    all_list = []#要存储即将被点击的点的坐标[[x1,y1],[x2,y2]]
    if '|' in result:
        list_1 = result.split('|')
        count_1 = len(list_1)
        for i in range(count_1):
            xy_list = []
            x = int(list_1[i].split(',')[0])
            y = int(list_1[i].split(',')[1])
            xy_list.append(x)
            xy_list.append(y)
            all_list.append(xy_list)
    else:
        xy_list = []
        x = int(result.split(',')[0])
        y = int(result.split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
    print(all_list)
    #遍历列表，使用动作链对每一个列表元素对应的x，y指定的位置进行点击操作
    for l in all_list:
        x=l[0]
        y=l[1]

        ActionChains(bro).move_to_element_with_offset(img_src,x,y).click().perform()

    bro.find_element_by_id('J-userName').send_keys('xxxxx')
    sleep(2)
    bro.find_element_by_id('J-password').send_keys('xxxxxx')
    sleep(2)
    bro.find_element_by_id('J-login').click()
    sleep(2)
    bro.quit()
