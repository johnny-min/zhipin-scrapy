# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo,json
import scrapy
from scrapy.conf import settings
from scrapy.exceptions import DropItem


class ZhipinPipeline(object):
    def __init__(self):
        # 链接数据库
        client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄
        # 数据库登录需要帐号密码的话
        self.db.authenticate(settings['MONGO_USER'], settings['MONGO_PWD'])


    # def __int__(self, mongo_url, mongo_db, mongo_user, mongo_pwd):
    #     self.mongo_url = mongo_url
    #     self.mongo_db = mongo_db
    #     self.mongo_user = mongo_user
    #     self.mongo_pwd = mongo_pwd
    #
    # @classmethod
    # def from_crawler(cls):
    #     return cls(
    #         mongo_url = settings.get('MONGO_URL'),
    #         mongo_db = settings.get('MONGO_DB'),
    #         mongo_user = settings.get('MONGO_USER'),
    #         mongo_pwd = settings.get('MONGO_PWD')
    #     )
    #
    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.mongo_url)
    #     self.db = self.client(self.mongo_db)
    #     self.db.authenticate(self.mongo_user, self.mongo_pwd)

    def process_item(self, item, spider):

        self.coll.update_one({'position_name': dict(item)['position_name'], 'position_salary':
            dict(item)['position_salary'], 'company_name': dict(item)['company_name']}, {'$set': dict(item)}, True)

        return item

    # def close_spider(self, spider):
    #     self.client.close()
# """
# jl格式的存储
# """
#     # def open_spider(self, spider):
#     #     self.f = open('position.jl', 'a', encoding='utf-8')
#     #
#     # def process_item(self, item, spider):
#     #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#     #     self.f.write(line)
#     #     return item
#     #
#     # def close_spider(self, spider):
#     #     self.f.close()
#
#
# class ErshoufangPipeline(object):
#
#     def open_spider(self, spider):
#         self.f = open('house.jl', 'a', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False)
#         self.f.write(line)
#         return item
#
#     def close_spider(self, spider):
#         self.f.close()


# from scrapy.pipelines.images import ImagesPipeline
#
#
# class DownloadimgPipeline(ImagesPipeline):
#
#     def get_media_requests(self, item, info):
#         for img_urls in item['img_urls']:
#             yield scrapy.Request(img_urls)
#
#     def item_completed(self, results, item, info):
#         img_paths = [x['path'] for ok,x in results if ok]
#         if not img_paths:
#             raise DropItem('Item contains no img')
#         item['img_paths'] = img_paths
#         return item
# class ZhipinPipeline(object):
#     """
#     jl格式的存储
#     """
#     def open_spider(self, spider):
#         self.f = open('position.jl', 'a', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.f.write(line)
#         return item
#
#     def close_spider(self, spider):
#         self.f.close()