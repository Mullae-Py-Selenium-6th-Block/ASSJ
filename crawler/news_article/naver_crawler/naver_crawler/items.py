# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class NewsURLCrawlingItem(scrapy.Item):

    # 크롤링을 통해 저장할 뉴스사, 뉴스 웹 페이지 주소, 작성일자를 속성으로 정의
    news_url = scrapy.Field()
    date = scrapy.Field()