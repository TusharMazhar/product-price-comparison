# -*- coding: utf-8 -*-
import scrapy
from ..items import ProductPriceComparisonItem


class StarttechSpider(scrapy.Spider):
    name = 'startech'
    page_number=2
    allowed_domains = ['startech.com.bd']
    start_urls = ['https://www.startech.com.bd/product/search?&search=graphics+card&category_id=0&page=1']

    def parse(self, response):

        items=ProductPriceComparisonItem()
        all_product=response.xpath('//*[@class="col-xs-12 col-md-12 product-layout list"]')
        for store in all_product:
            items['image']=store.xpath('.//*[@class="img-holder"]/a/img[@src]').extract_first()
            items['price']=store.xpath('.//*[@class="price"]/span/text()').extract_first()
            items['link']=store.xpath('.//*[@class="product-name"]/a/@href').extract_first()
            items['titile']=store.xpath('.//*[@class="product-name"]/a/text()').extract_first()

            yield items
        
        next_page='https://www.startech.com.bd/product/search?&search=graphics+card&category_id=0&page='+str(StarttechSpider.page_number)+'/'
        if StarttechSpider.page_number <=20:
            StarttechSpider.page_number +=1
            yield response.follow(next_page,callback=self.parse)



        
