# -*- coding: utf-8 -*-
import scrapy
from zhipin.items import ErshoufangItem

class ErshoufanSpider(scrapy.Spider):
    name = 'ershoufan'
    allowed_domains = ['xa.anjuke.com']
    start_urls = ['https://xa.anjuke.com/sale/rd1/?kw=&from=sugg']

    def parse(self, response):
        house_list = response.xpath("//li[@class='list-item']")
        for house in house_list:
            item = ErshoufangItem()

            item['house_title'] = house.xpath(".//div[@class='house-title']/a/text()").extract_first().strip()
            item['details_item1'] = house.xpath(".//div[@class='details-item'][1]/span/text()").extract().strip()
            item['details_item2'] = house.xpath(".//div[@class='details-item'][2]/span/text()").extract().strip()
            item['pro_price'] = (house.xpath(".//div[@class='pro-price']/span/strong/text()").extract_first()+ \
                                house.xpath(".//div[@class='pro-price']/span/text()").extract_first()+ \
                                house.xpath(".//div[@class='pro-price']/span/text()").extract()[1]).strip()

            yield item

            if not response.xpath("//i[@class='iNxt']"):
                url = response.xpath("//a[@class='aNxt']/@href").extract_first()
                yield scrapy.Request(url=url, callback=self.parse)
