# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ItcastPipeline(object):
    def __init__(self):
        # 初始化创建一个json文件
        self.f = open('itcast_pipeline.csv','w')

    # 将管道中的item写入创建csv文件中
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii = False)
        # self.f.write(content.encode('utf-8'))
        self.f.write(content)
        return item

    def close_spider(self,spider):
        self.f.close()
