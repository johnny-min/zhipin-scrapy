# -*- coding: utf-8 -*-
import scrapy

from zhipin.items import DownloadimgItem


class DownloadimgSpider(scrapy.Spider):
    name = 'downloadimg'
    allowed_domains = ['www.google.com']
    start_urls = ['https://xa.anjuke.com/sale/#filtersort']


    def parse(self, response):
        img_list = response.xpath("//li[@class='list-item']//img/@src").extract()
        self.log(f'img_list is {img_list}')
        if img_list:
            item = DownloadimgItem()
            item['img_urls'] = img_list
            yield item
