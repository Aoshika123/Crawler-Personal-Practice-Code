from selenium import webdriver
from lxml import etree
from time import sleep
#实例化一个浏览器对象（传入浏览器的驱动）
bro = webdriver.Chrome(executable_path = './chromedriver')
#让浏览器发起一个指定url对应请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')

page_text = bro.page_source

#解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
sleep(5)
bro.quit()