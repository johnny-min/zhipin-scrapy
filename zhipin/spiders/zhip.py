# -*- coding: utf-8 -*-
import json, re

import scrapy

from zhipin.items import ZhipinItem


class ZhipSpider(scrapy.Spider):
    name = 'zhip'
    card_url = 'https://www.zhipin.com/view/job/card.json?jid={jidcard}&lid={lidcard}'

    def start_requests(self):
        url = f'https://www.zhipin.com/c100010000-p100109/?query=python&page=0'
        yield scrapy.Request(url=url, callback=self.parse)
        # yield scrapy.Request(url=self.card_url, callback=self.parse_card)

    def parse(self, response):
        page = response.url[-1:]
        filename = 'quotes-%s.txt' % page
        self.log('Count : %s' % filename)
        position_list = response.xpath('//div[@class="job-primary"]')
        for position in position_list:
            jidcard = position.xpath(".//a/@data-jid").extract_first()
            lidcard = position.xpath(".//a/@data-lid").extract_first()

            #在Request方法中使用meta传递多个参数
            yield scrapy.Request(url=self.card_url.format(jidcard=jidcard, lidcard=lidcard),meta={'position': position},
                                 callback=self.parse_card)

        if response.xpath("//a[@class='next' and @ka='page-next']"):
            url = f'https://www.zhipin.com/' + response.xpath("//a[@class='next']/@href").extract_first()
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_card(self, response):
        result = json.loads(response.text)
        position = response.meta['position']
        if 'html' in result.keys():
            position_info_html = result.get('html')
            pattern = re.compile('<div.*?detail-bottom-text">(.*?)</div>', re.S)
            item = ZhipinItem()
            item['position_name'] = position.xpath(".//div[@class='job-title']/text()").extract_first()
            item['position_salary'] = position.xpath(".//span[@class='red']/text()").extract_first()
            item['position_label'] = position.xpath("./div[@class='info-primary']/p/text()").extract()
            item['company_name'] = position.xpath(".//div[@class='company-text']/h3/a/text()").extract_first()
            item['company_info'] = position.xpath(".//div[@class='company-text']/p/text()").extract()
            old_position_card = re.findall(pattern, position_info_html)[0].strip()
            item['position_card'] = re.sub('<br/>', '', old_position_card)
            yield item
