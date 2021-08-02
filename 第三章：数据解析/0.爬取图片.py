
import requests
if __name__ == '__main__':
    #如何爬取图片数据
    url = 'https://pic.qiushibaike.com/system/pictures/12452/124526438/medium/V7GVE070GVDJRO3F.jpg'
    #content返回的是二进制形式的图片数据
    #text（字符串） content（二进制） json（）(对象)
    img_data = requests.get(url=url).content

    with open('./qiutu.jpg','wb') as fp:
        fp.write(img_data)
