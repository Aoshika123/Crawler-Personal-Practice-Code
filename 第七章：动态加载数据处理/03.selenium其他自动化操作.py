from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://www.taobao.com/')

#标签定位
search_input = bro.find_element_by_id('q')
#标签交互
search_input.send_keys('iphone')

#执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
btn = bro.find_element_by_css_selector('.tb-bg')#btn-search tb-bg 两者之间有空格，选择其一就行
btn.click()

bro.get('https://www.baidu.com')
sleep(2)
#回退
bro.back()
#前进
bro.forward()

sleep()
bro.quit()
