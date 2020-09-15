# Define here the models for your scraped items
# 크롤링할 데이터를 정의해주는 파일
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#
import scrapy

class CrawledItem(scrapy.Item):
    # define the fields for your item here like:
    reviewTitle = scrapy.Field() # 제목
    reviewText = scrapy.Field() # 리뷰
    # reviewGrade = scrapy.Field() # 평점
    pass
