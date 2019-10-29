# -*- coding: utf-8 -*-
import scrapy


class GpuSpider(scrapy.Spider):

    name = 'gpu'
    allowed_domains = ['village-bd.com'] #  domain name only copied
    start_urls = ['https://www.village-bd.com/search?q=graphics+card'] # link copy from website

    def parse(self, response):



       
        image=response.xpath('//*[@class="img-box"]/a/img/@src').extract()
        titile=response.xpath('//*[@class="pro-name"]/a/text()').extract()
        link=response.xpath('//*[@class="img-box"]/a/@href').extract()
        price=response.xpath('//*[@class="price"]/text()').extract()

        length=len(image)
        i=1
        while i<=length:
            print('\n')
            print("  Product-Name :",titile[i],"\n"," Price :",price[i],"\n"," Image :",image[i],"\n"," Link :",link[i])
            
            print('\n')  
            i=i+1


        

        
        


































































            




  
"""
        
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


"""       

        

           

            



        
