# -*- coding: utf-8 -*-
import scrapy
from ..items import ProductPriceComparisonItem

    

class GpuSpider(scrapy.Spider):

    name = 'villagebd'
    allowed_domains = ['village-bd.com'] #  domain name only copied
    start_urls = ['https://www.village-bd.com/search?q=graphics+card'] # link copy from website

    def parse(self, response):


        items=ProductPriceComparisonItem()
        all_product=response.xpath('//*[@class="pro-box"]')
        for store in all_product:

            items['image']=store.xpath('.//*[@class="img-box"]/a/img/@src').extract_first()
            items['price']=store.xpath('.//*[@class="price"]/text()').extract_first()
            items['link']=store.xpath('.//*[@class="img-box"]/a/@href').extract_first()
            items['titile']=store.xpath('.//*[@class="pro-name"]/a/text()').extract_first()

            yield items



        

       



        

       

        



































































            




  
   

        

           

            



        
