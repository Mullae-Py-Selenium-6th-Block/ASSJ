# scrapy 패키지 불러오기
import scrapy

# ----------------------------------------------------------------------------------------------------

# NewsURLItem() 클래스 정의
class NewsURLItem(scrapy.Item):

    # 크롤링을 통해 저장할 작성일자, URL을 정의
    WritedAt = scrapy.Field()
    URL = scrapy.Field()

# ----------------------------------------------------------------------------------------------------

# NewsArticleItem() 클래스 정의
class NewsArticleItem(scrapy.Item):

    # 크롤링을 통해 저장할 작성일자, 제목, 내용, URL을 정의
    WritedAt = scrapy.Field()
    Title = scrapy.Field()
    Content = scrapy.Field()
    URL = scrapy.Field()

# ----------------------------------------------------------------------------------------------------

# NewsCommentItem() 클래스 정의
class NewsCommentItem(scrapy.Item):

    # 크롤링을 통해 저장할 URL, 작성일자, 내용을 정의
    URL = scrapy.Field()
    WritedAt = scrapy.Field()
    Content = scrapy.Field()