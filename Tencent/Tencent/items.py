# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionName = scrapy.Field()
    postionLink = scrapy.Field()
    postionType = scrapy.Field()
    postionNumber = scrapy.Field()
    postionLocation = scrapy.Field()
    publishDate = scrapy.Field()
    pass
