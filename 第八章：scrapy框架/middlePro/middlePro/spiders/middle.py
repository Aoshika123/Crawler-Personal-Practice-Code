import scrapy


class MiddleSpider(scrapy.Spider):
    #爬取百度
    name = 'middle'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response):
        page_text = response

        with open('./ip.html','w',encoding='utf-8') as fp:
            fp.write(page_text)
