# 필요한 모듈 불러오기
import pandas as pd
import scrapy
from ..items import NewsURLCrawlingItem, NewsArticleItem
import calendar
import datetime
# ----------------------------------------------------------------------------------------------------

# NewsURLSpider() 클래스 정의
class NewsURLSpider(scrapy.Spider):

    # 스파이더 이름 정의
    name = "NewsURLCrawler"

    # 쿼리 스트링(Query String)을 제외한 기본 URL을 base_url에 할당
    base_url = "https://search.naver.com/search.naver"

    # ----------------------------------------------------------------------------------------------------

    # start_requests() 함수 정의
    def start_requests(self):
        """
        크롤링을 수행할 웹 페이지에 HTTPS 요청을 보내고 콜백 함수로서 news_locator() 함수를 호출하는 함수입니다.\n
        scrapy 모듈의 Request 클래스 객체를 반환합니다.
        """
        search_period =  pd.date_range("2022-05-01", "2022-12-21", freq = "D").strftime("%Y%m%d")
        for date in search_period:
            # 크롤링할 페이지를 나타내는 변수 page 초기화
            page = 0
    
            # 쿼리 스트링(Query String)을 query_url에 할당
            query_url = '?where=news&query=서울+아파트+가격&sort=1&mynews=1&nso=p:from{0}to{1}&start={2}1'.format(
                date,
                date,
                page
            )
            print(self.base_url + query_url)
            # 결과 값 반환
            yield scrapy.Request(url = self.base_url + query_url, callback = self.news_locator, cb_kwargs = dict(
                date = date,
                page = page,
                url_list = ['123']
            ))

    # ----------------------------------------------------------------------------------------------------

    # news_locator() 함수 정의
    def news_locator(self, response, date : str, page : int, url_list: list):
        """
        웹 페이지에서 신문사, 뉴스기사 URL, 뉴스기사 날짜를 추출하고 다음 페이지를 호출하는 함수입니다.\n
        scrapy 모듈의 Item 클래스 객체와 Request 클래스 객체를 반환합니다.
        """
        print(date, page)
        # 현재 크롤링을 진행하고 있는 웹 페이지 주소를 출력
        url = response.url
        print(f">>> 다음 URL을 크롤링 중입니다: {url}\n")
        u_list = []        
        news_url_img = response.xpath(f'//*[@id="sp_nws{page * 10 + 1}"]/div/div/a/@href').get()
        news_url = response.xpath(f'//*[@id="sp_nws{page * 10 + 1}"]/div/div/a/@href').get()
        if not news_url_img and not news_url:
            print('내용 없음')
            return
        
        u_list = [news_url_img, news_url]
        if url_list == u_list:
            return
        # 검색결과가 없는 경우 안내 메시지 출력 후 더 이상 크롤링을 수행하지 않도록 설정
        if response.css(".not_found02").get():
            print(">>> 검색 결과가 존재하지 않습니다.")
            yield None

        else:
            # NewsURLCrawlingItem() 클래스를 가져와 변수 item에 할당
            item = NewsURLCrawlingItem()

            # for 반복문을 사용해 각 뉴스 기사에 접근
            for list_num in range(1, 11):
                # 뉴스 기사의 ID에 접근하기 위해 계산
                news_num = list_num + page * 10
                news_url_img = response.xpath("//*[@id='sp_nws{0}']/div[1]/div/div[1]/div[2]/a[2]/@href".format(news_num)).extract()
                news_url  = response.xpath('//*[@id="sp_nws{0}"]/div/div/div[1]/div[2]/a[2]/@href'.format(news_num)).extract()
                # 신문사, 뉴스기사 URL, 뉴스기사 날짜를 추출해 각 열에 저장
                if (not news_url_img) and (not news_url):
                    pass
                else:
                    if news_url_img:
                        item["news_url"] = news_url_img
                        item["date"] = response.xpath("//*[@id='sp_nws{0}']/div/div/div[1]/div[2]/span/text()".format(news_num)).extract()[-1 :]
                    else:
                        item["news_url"] = news_url
                        item["date"] = response.xpath("//*[@id='sp_nws{0}']/div/div/div[1]/div[2]/span/text()".format(news_num)).extract()[-1 :]

            
                # 결과 값 반환
                yield item

            # 다음 페이지로 페이지 수 조정 후 다음 페이지 호출
            page += 1

            # 쿼리 스트링(Query String)을 query_url에 할당
            query_url = '?where=news&query=서울+아파트+가격&sort=1&mynews=1&nso=p:from{0}to{1}&start={2}1'.format(
                date,
                date,
                page
            )

            # 결과 값 반환
            yield scrapy.Request(url = self.base_url + query_url, callback = self.news_locator, cb_kwargs = dict(
                date = date,
                page = page,
                url_list= u_list
            ))

class NewsArticleSpider(scrapy.Spider):
    name = "NewsArticleCrawler"

    # URL에 접속하기 위해 필요한 헤더(Header) 정보를 담은 딕셔너리 headers 초기화
    headers = {"user-agent": "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}


    def start_requests(self):

        # 크롤링을 위해 뉴스 URL을 담은 CSV 파일을 불러와 데이터프레임 생성
        news_df = pd.read_csv("/Users/stillssi/Desktop/ASSJ/crawler/news_article/naver_news_url.csv", header = 0, encoding = "utf-8-sig")

        # for 반복문을 사용하여 데이터프레임의 각 행을 순회
        for idx in news_df.index:

            # 날짜, URL을 가져와 각 변수에 할당
            date = news_df.loc[idx, "date"]
            url = news_df.loc[idx, "news_url"]

            # 결과 값 반환
            yield scrapy.Request(url = url, callback = self.news_parser, headers = self.headers)


    def news_parser(self, response):

        # 현재 크롤링을 진행하고 있는 웹 페이지 주소를 출력
        url = response.url
        print(f">>> 다음 URL을 크롤링 중입니다: {url}\n")

        item = NewsArticleItem()

        item['date'] = response.css(".media_end_head_info_datestamp_time._ARTICLE_DATE_TIME ::text").extract()[0][:11]
        # 뉴스 title
        item['title'] = response.css("#title_area ::text").extract()

        # 뉴스 기사의 내용이 존재하는 두 가지 경우에 따라 내용을 가져와 할당
        if not response.css("#dic_area ::text").extract():
            item["content"] = "".join(response.css("#dic_area .article ::text").extract())
        else:
            item["content"] = "".join(response.css("#dic_area ::text").extract())

        yield item