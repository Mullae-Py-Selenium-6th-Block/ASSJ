# scrapy 패키지 불러오기
import scrapy

# ----------------------------------------------------------------------------------------------------

# NewsItem() 클래스 정의
class NewsItem(scrapy.Item):

    # 크롤링을 통해 저장할 분류, 작성일자, 제목, 내용, URL, 사진 URL, 기자, 뉴스사, 스티커 반응을 정의
    MainCategory = scrapy.Field()
    SubCategory = scrapy.Field()
    WritedAt = scrapy.Field()
    Title = scrapy.Field()
    Content = scrapy.Field()
    URL = scrapy.Field()
    PhotoURL = scrapy.Field()
    Writer = scrapy.Field()
    Press = scrapy.Field()
    Stickers = scrapy.Field()

# ----------------------------------------------------------------------------------------------------

# CommentItem() 클래스 정의
class CommentItem(scrapy.Item):

    # 크롤링을 통해 저장할 URL, 작성일자, 내용을 정의
    URL = scrapy.Field()
    WritedAt = scrapy.Field()
    Content = scrapy.Field()

# ----------------------------------------------------------------------------------------------------

# NewsURLItem() 클래스 정의
class NewsURLItem(scrapy.Item):

    # 크롤링을 통해 저장할 분류, 제목, URL을 정의
    MainCategory = scrapy.Field()
    SubCategory = scrapy.Field()
    Title = scrapy.Field()
    URL = scrapy.Field()