# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductPriceComparisonItem(scrapy.Item):
    
    image= scrapy.Field()
    titile= scrapy.Field()
    link= scrapy.Field()
    price= scrapy.Field()

    # define the fields for your item here like:
    
    pass
