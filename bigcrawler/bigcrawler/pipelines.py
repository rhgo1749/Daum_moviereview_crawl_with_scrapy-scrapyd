# Define your item pipelines here
# 데이터 가공 및 DB저장을 수행하는 파일
# useful for handling different item types with a single interface
# export to csv
from __future__ import unicode_literals
from scrapy.exporters import CsvItemExporter
import re

hangul = re.compile('[^ ㄱ-ㅣ가-힣|0-9|a-z|A-Z]+')
time = re.compile('[^ 0-9|.:]+')
fieldnames = ['reviewTitle', 'reviewText', 'reviewDay', 'reviewTime']

minLengthReview = 8

class TextPipeline(object):
    # export to csv
    def open_spider(self, spider):
        self.file = open("{0}.csv".format(spider.fileRangeName), 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8', fields_to_export=fieldnames)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.file.close()
        pass

    def process_item(self, item, spider):
        # Regulation
        for i in range(1, len(item['reviewText'])):
            item['reviewText'][0] = item['reviewText'][0] + ' ' + item['reviewText'][i]
        for i in range(1, len(item['reviewTime'])):
            item['reviewTime'][0] = item['reviewTime'][0] + ' ' + item['reviewTime'][i]
        item['reviewText'] = [item['reviewText'][0]]
        item['reviewText'][0] = re.sub(r"\n", " ", item['reviewText'][0], flags=re.UNICODE)
        item['reviewText'][0] = hangul.sub('', item['reviewText'][0])
        item['reviewText'][0] = re.sub(r"\s+", " ", item['reviewText'][0], flags=re.UNICODE)
        item['reviewText'][0] = item['reviewText'][0].strip(' ')
        item['reviewTime'] = [item['reviewTime'][0]]
        item['reviewTime'][0] = re.sub(r"\n", " ", item['reviewTime'][0], flags=re.UNICODE)
        item['reviewTime'][0] = time.sub('', item['reviewTime'][0])
        item['reviewTime'][0] = re.sub(r"\s+", " ", item['reviewTime'][0], flags=re.UNICODE)
        item['reviewTime'][0] = item['reviewTime'][0].strip(' ')
        tempList = item['reviewTime'][0].split(' ')
        item['reviewDay'] = tempList[0]
        item['reviewTime'][0] = tempList[1]

        # re-label
        if len(item['reviewText'][0]) < 8:
            pass
        else:
            # export to csv
            self.exporter.export_item(item)
            return item

