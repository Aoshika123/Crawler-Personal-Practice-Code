import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['www.xxx.com']
    #start_urls = ['https://www.zhipin.com/c100010000-p100109/?page=3&ka=page-3']
    start_urls = ['https://www.k8jds.com/index.php/vod/show/id/5/lang/%E5%9B%BD%E8%AF%AD.html']

    url = 'https://www.k8jds.com/index.php/vod/show/id/5/lang/%E5%9B%BD%E8%AF%AD/page/%d.html'
    page_num = 2

    def parse_detail(self,response):
        item = response.meta['item']

        #job_desc = response.xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = response.xpath('/html/body/div[2]/div/div[1]/div[4]/div/div[2]/div/span[1]/text()').extract()
        job_desc = ''.join(job_desc)

        item['job_desc'] = job_desc
        yield item

    #解析首页中的岗位名称
    def parse(self, response):
        with open('./boss.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
        #li_list = response.xpath('//div[@id="wrap"]/div[3]/div/div[2]/ul/li')
        li_list = response.xpath('/html/body/div[2]/div/div[2]/div/div[2]/ul/li')

        for li in li_list:
            item = BossproItem()

            #job_name = li.xpath('.//div[@class="job-title"]/span[1]/a/text()').extract_first()
            job_name = li.xpath('./div/div/h4/a/text()').extract_first()
            item['job_name'] = job_name
            #detail_url = 'https://www.zhipin.com'+li.xpath('.//div[@class="job-title"]/span[1]/a/@href').extract_first()
            detail_url = 'https://www.k8jds.com/'+li.xpath('./div/div/h4/a/@href').extract_first()
            #print(job_name,detail_url)
            #对详情页发请求获取详情页的页面源码数据
            #手动请求的发送
            #请求传参：meta={}，可以将meta字典 传递给请求对应的回调函数

            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

        if self.page_num<=3:
            new_url = format(self.url%self.page_num)
            self.page_num+=1

            yield scrapy.Request(new_url,callback=self.parse)
