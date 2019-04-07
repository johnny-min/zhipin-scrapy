# -*- coding: utf-8 -*-
import scrapy


class ZhiSpider(scrapy.Spider):
    name = 'zhi'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['http://www.zhipin.com/']

    def parse(self, response):
        filename = 'D:\work\code\zhipin\zhipin.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

