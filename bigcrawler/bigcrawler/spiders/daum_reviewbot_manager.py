import scrapy
import os
from bigcrawler.items import CrawledItem
from bigcrawler.utils import MovieCrawler

item = CrawledItem()
utils = MovieCrawler()

class BaseSpider(scrapy.Spider):
    base_url = "https://movie.daum.net/moviedb/grade?movieId="
    middle_url = "&type=netizen&page="

    currentReviewPage = 1
    startIndex = 1
    movingIndex = startIndex
    endIndex = 10

    handle_httpstatus_list = [500]

    def __init__(self):
        pass

    # read data with moving urls
    def start_requests(self):
        yield scrapy.Request(self.base_url + str(self.startIndex) + "&type=netizen&page=" + str(self.startIndex),
                             callback=self.parse_review_n_rank)

    # read datas in one movie review
    def parse_review_n_rank(self, response):
        # is there review
        while self.movingIndex != (self.endIndex):
            if response.status not in self.handle_httpstatus_list:
                if len(response.xpath('//*[@id="mArticle"]/div[2]/div[2]/div[1]/p')) == 0:
                    numOfli = len(response.xpath('//*[@id="mArticle"]/div[2]/div[2]/div[1]/ul/li').extract())
                    for i in range(1, numOfli+1):
                        reviewText = response.xpath('//*[@id="mArticle"]/div[2]/div[2]/div[1]/ul/li[{0}]/div/p/text()'.format(i))
                        reviewTitle = response.xpath('//*[@id="mArticle"]/div[1]/a/h2/text()')
                        reviewTime = response.xpath('//*[@id="mArticle"]/div[2]/div[2]/div[1]/ul/li[{0}]/div/div[2]/span[1]/text()'.format(i))
                        item['reviewTitle'] = reviewTitle.extract()
                        item['reviewText'] = reviewText.extract()
                        item['reviewTime'] = reviewTime.extract()
                        yield item
                    self.currentReviewPage = self.currentReviewPage + 1
                    yield scrapy.Request(self.base_url + "{0}".format(self.movingIndex) + self.middle_url +
                                         "{0}".format(self.currentReviewPage), callback=self.parse_review_n_rank, dont_filter=True)
                    break
                else:
                    self.movingIndex = self.movingIndex + 1
                    self.currentReviewPage = 1
                    yield scrapy.Request(self.base_url + "{0}".format(self.movingIndex) + self.middle_url +
                                         "{0}".format(self.currentReviewPage), callback=self.parse_review_n_rank,
                                         dont_filter=True)
                    break
            else:
                self.movingIndex = self.movingIndex + 1
                self.currentReviewPage = 1
                yield scrapy.Request(self.base_url + "{0}".format(self.movingIndex) + self.middle_url +
                                     "{0}".format(self.currentReviewPage), callback=self.parse_review_n_rank,
                                     dont_filter=True)
                utils.is_error = True
                break

class Childspider1(BaseSpider):
    name = __qualname__
    startIndex = 1
    movingIndex = startIndex
    endIndex = 10000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider2(BaseSpider):
    name = __qualname__
    startIndex = 10001
    movingIndex = startIndex
    endIndex = 20000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider3(BaseSpider):
    name = __qualname__
    startIndex = 30001
    movingIndex = startIndex
    endIndex = 40000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider4(BaseSpider):
    name = __qualname__
    startIndex = 40001
    movingIndex = startIndex
    endIndex = 45000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider5(BaseSpider):
    name = __qualname__
    startIndex = 50001
    movingIndex = startIndex
    endIndex = 60000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider6(BaseSpider):
    name = __qualname__
    startIndex = 60001
    movingIndex = startIndex
    endIndex = 70000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider7(BaseSpider):
    name = __qualname__
    startIndex = 70001
    movingIndex = startIndex
    endIndex = 80000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider8(BaseSpider):
    name = __qualname__
    startIndex = 80001
    movingIndex = startIndex
    endIndex = 90000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider9(BaseSpider):
    name = __qualname__
    startIndex = 90001
    movingIndex = startIndex
    endIndex = 100000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider10(BaseSpider):
    name = __qualname__
    startIndex = 100001
    movingIndex = startIndex
    endIndex = 110000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider11(BaseSpider):
    name = __qualname__
    startIndex = 110001
    movingIndex = startIndex
    endIndex = 120000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider12(BaseSpider):
    name = __qualname__
    startIndex = 120001
    movingIndex = startIndex
    endIndex = 130000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider13(BaseSpider):
    name = __qualname__
    startIndex = 130001
    movingIndex = startIndex
    endIndex = 140000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider14(BaseSpider):
    name = __qualname__
    startIndex = 140001
    movingIndex = startIndex
    endIndex = 150000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider15(BaseSpider):
    name = __qualname__
    startIndex = 150001
    movingIndex = startIndex
    endIndex = 160000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)

class Childspider16(BaseSpider):
    name = __qualname__
    startIndex = 45001
    movingIndex = startIndex
    endIndex = 50000
    fileRangeName = "{0}-{1}".format(startIndex, endIndex)