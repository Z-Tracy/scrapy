
# -*- coding:utf-8 -*-
import scrapy
# 导入上级目录item中的类
from Itcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains =['http://www.itcast.cn']
    start_urls =['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self,response):

        node_list = response.xpath("//div[@class='li_txt']")
        # 用来存储所有的item字段
        items = []
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item = ItcastItem()
            # 用.extract()将xpath对象转化为Unicode字符串
            name = node.xpath('./h3/text()').extract()
            title = node.xpath('./h4/text()').extract()
            info = node.xpath('./p/text()').extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            # items.append(item)

            # 返回item数据给管道文件处理，同时回来继续执行后面的代码
            yield item
        # return 给引擎
        # return items

