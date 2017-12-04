# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ItcastPipeline(object):
    def __init__(self):
        self.f=open("itcast_piprline.json","w")

    def process_item(self, item, spider):
        content=json.dumps(dict(item),ensure_ascii=False)+',\n'
        self.f.write(content)
#        self.f.write(str(dict(item)))
        return item

    def close_spider(self,spider):
        self.f.close()
        pass