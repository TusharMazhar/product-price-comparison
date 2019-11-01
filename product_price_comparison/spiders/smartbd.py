# -*- coding: utf-8 -*-
import scrapy
from ..items import ProductPriceComparisonItem




class SmartbdSpider(scrapy.Spider):
    name = 'smartbd'
    page_number=2
    allowed_domains = ['smartbd.com']
    start_urls = ['https://smartbd.com/catalogsearch/result/index/?p=1&q=graphics+card']

    def parse(self, response):

        
        items=ProductPriceComparisonItem()
        all_product=response.xpath('//*[@class="ma-box-content"]')
        for store in all_product:
            items['image']= store.xpath('.//*[@class="product-image"]/img/@src').extract_first()   


            price=store.xpath('.//*[@class="regular-price"]/span/text()').extract_first()
            priceSignRemoved=price.replace('BDT','')
            convertedprice=float(priceSignRemoved.replace(",",''))
            items['price']= convertedprice

            items['link']=store.xpath('.//*[@class="product-name"]/a/@href').extract_first()
            items['titile']=store.xpath('.//*[@class="product-name"]/a/text()').extract_first()

            yield items
        next_page='https://smartbd.com/catalogsearch/result/index/?p='+str(SmartbdSpider.page_number)+'&q=graphics+card'
        if SmartbdSpider.page_number <=20:

            SmartbdSpider.page_number +=1
            yield response.follow(next_page,callback=self.parse)
        
      

        
