# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy


#class TrafficintoscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass


import scrapy

class TrafficInfoItem(scrapy.Item):
    #URL = scrapy.Field()
    #title = scrapy.Field()
    index = scrapy.Field()
    contents = scrapy.Field()
    pass
