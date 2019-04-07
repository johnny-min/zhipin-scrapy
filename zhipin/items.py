# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhipinItem(scrapy.Item):
    # define the fields for your item here like:

    #职位名称
    position_name = scrapy.Field()
    # 职位薪资
    position_salary = scrapy.Field()
    # 职位标签
    position_label = scrapy.Field()
    # 职位卡片
    position_card = scrapy.Field()
    # 公司名称
    company_name = scrapy.Field()
    # 公司信息
    company_info = scrapy.Field()


class ErshoufangItem(scrapy.Item):

    #item_img
    # item_img = scrapy.Field()
    #house_title
    house_title = scrapy.Field()
    # details_item
    details_item1 = scrapy.Field()
    # details_item
    details_item2 = scrapy.Field()
    # pro_price
    pro_price = scrapy.Field()

class DownloadimgItem(scrapy.Item):

    img_urls = scrapy.Field()
    imgs = scrapy.Field()
    img_paths = scrapy.Field()

