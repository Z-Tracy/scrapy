# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    base_url = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [base_url + str(offset)]


    def parse(self, response):
        node_list =  response.xpath("//tr[@class='even']")
        for node in node_list:
            item = TencentItem()
            # 注意点：
            # 1、节点用/ 属性用@
            item['positionName'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['postionLink'] =  node.xpath('./td[1]/a/@href').extract()[0]
            # if len(item['postionType']):
            #     item['postionType'] = node.xpath('./td[2]/text()').extract()[0]
            # else:
            #     item['postionType'] =""
            try:
                item['postionType'] = node.xpath('./td[2]/text()').extract()[0]
            except:
                item['postionType'] = ""

            item['postionNumber'] =  node.xpath('./td[3]/text()').extract()[0]
            item['postionLocation'] =  node.xpath('./td[4]/text()').extract()[0]
            item['publishDate'] =  node.xpath('./td[5]/text()').extract()[0]

            yield item

        # # 翻页方案一：构建url方式
        # if self.offset < 2580:
        #     self.offset +=  10
        #     url = self.base_url + str(self.offset)
        #
        #     yield scrapy.Request(url , callback = self.parse)

        # 翻页方案二：查找判断下一页链接

        if not len(response.xpath("//a[@class='noactive' and @id='next']")):
            print('-----------------------------------------------------------------------------------------')
            url = response.xpath("//a[@id='next']/@href").extract()[0]
            yield scrapy.Request('http://hr.tencent.com/' + url, callback=self.parse)
