# -*- coding: utf-8 -*-
import scrapy
from ..items import ProductPriceComparisonItem

    

class GpuSpider(scrapy.Spider):

    name = 'gpu'
    allowed_domains = ['village-bd.com'] #  domain name only copied
    start_urls = ['https://www.village-bd.com/search?q=graphics+card'] # link copy from website

    def parse(self, response):


        items=ProductPriceComparisonItem()
      
        items['image']=response.xpath('//*[@class="img-box"]/a/img/@src').extract()
        items['price']=response.xpath('//*[@class="price"]/text()').extract()
        items['link']=response.xpath('//*[@class="img-box"]/a/@href').extract()
        items['titile']=response.xpath('//*[@class="pro-name"]/a/text()').extract()

        yield items



        

       



        

       

        



































































            




  
   

        

           

            



        
