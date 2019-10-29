# -*- coding: utf-8 -*-
import scrapy


class GpuSpider(scrapy.Spider):
    name = 'gpu'
    allowed_domains = ['village-bd.com'] #  domain name only copied
    start_urls = ['https://www.village-bd.com/search?q=graphics+card'] # link copy from website

    def parse(self, response):

        smartBdGpuInfoBox=response.xpath('//*[@class="pro-box"]')
        for smartBdGpu in smartBdGpuInfoBox:
            image=smartBdGpu.xpath('//*[@class="img-box"]/a/img/@src').extract_first()  
            titile=smartBdGpu.xpath('//*[@class="pro-name"]/a/text()').extract_first()
            link=smartBdGpu.xpath('//*[@class="img-box"]/a/@href').extract_first() 
            price=smartBdGpu.xpath('//*[@class="price"]/text()').extract_first()  
            print('\n')
            print(image)
            print(titile)
            print(link)
            print(price)
            print('\n')




































































            




      

        

           

            



        
