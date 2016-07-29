# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class BrewtoadPipeline(object):
    def process_item(self, item, spider):
        return item



class JsonExportPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        import pdb; pdb.set_trace()
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
