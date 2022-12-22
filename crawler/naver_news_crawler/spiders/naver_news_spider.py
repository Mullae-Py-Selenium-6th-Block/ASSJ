# 필요한 패키지 불러오기
import scrapy
import pandas as pd
from ..items import NewsURLItem, NewsItem, CommentItem
from datetime import datetime
import requests
import json
import re

# ----------------------------------------------------------------------------------------------------

# NaverNewsCommentCrawler() 클래스 정의
class NaverNewsCommentCrawler(scrapy.Spider):

    # 스파이더 이름 정의
    name = "NaverNewsCommentCrawler"

    # 접근 차단을 막기 위한 시간 지연 설정
    download_delay = 0.15

    # URL에 접속하기 위해 필요한 헤더(Header) 정보를 담은 딕셔너리 headers 초기화
    headers = {"user-agent": "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

    # ----------------------------------------------------------------------------------------------------

    # start_requests() 함수 정의
    def start_requests(self):
        """
        크롤링을 수행할 웹 페이지에 HTTPS 요청을 보내고 콜백 함수로서 comment_parser() 함수를 호출하는 함수입니다.\n
        scrapy 모듈의 Request 클래스 객체를 반환합니다.
        """

        # 크롤링을 위해 뉴스 URL을 담은 CSV 파일을 불러와 데이터프레임 생성
        news_df = pd.read_csv("./../data/naver_news_url.csv", header = 0, encoding = "utf-8-sig")
        
        # for 반복문을 사용하여 데이터프레임의 각 행을 순회
        for idx in news_df.index:

            # URL을 가져와 각 변수에 할당
            url = news_df.loc[idx, "URL"]

            # 결과 값 반환
            yield scrapy.Request(url = url, callback = self.comment_parser, headers = self.headers)

    # ----------------------------------------------------------------------------------------------------

    # comment_parser() 함수 정의
    def comment_parser(self, response):
        """
        네이버 뉴스 웹 페이지에서 URL, 댓글 작성일자, 댓글 내용을 추출하는 함수입니다.\n
        scrapy 모듈의 Item 클래스 객체를 반환합니다.
        """

        # 현재 크롤링을 진행하고 있는 웹 페이지 주소를 출력
        url = response.url
        print(f">>> 다음 URL을 크롤링 중입니다: {url}\n")

        # CommentItem() 클래스를 가져와 변수 item에 할당
        item = CommentItem()

        # 댓글이 존재하는 쿼리 스트링 제거 URL을 comment_base_url에 할당
        comment_base_url = "https://cbox5.apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json"

        # 쿼리 스트링(Query String)에 사용할 값을 추출 및 정의
        press_id = url.split("/")[5]
        article_id = url.split("/")[6].split("?")[0]
        section_id = url.split("=")[1]

        # 딕셔너리 headers에 "referer" 값 추가
        self.headers["referer"] = f"https://n.news.naver.com/mnews/article/comment/{press_id}/{article_id}?sid={section_id}"

        # 쿼리 스트링(Query String)을 comment_query_url에 할당
        comment_query_url = f"?ticket=news&pool=cbox5&lang=ko&objectId=news{press_id}%2C{article_id}&pageSize=100&pageType=more"

        # while 반복문을 사용해 각 댓글 페이지를 차례로 순회
        while True:
            
            # get() 함수를 사용해 스티커 반응 정보를 요청해 변수 res에 할당
            res = requests.get(comment_base_url + comment_query_url , headers = self.headers)

            # loads() 함수를 사용해 JSON 문자열을 객체로 변환해 json_res에 할당
            json_res = json.loads(re.search("\((.*)\)\;", res.text).group(1))["result"]["commentList"]

            # for 반복문을 사용해 각 댓글을 순회
            for comment in json_res:

                # 뉴스 URL, 댓글 작성일자, 내용을 가져와 각 열에 할당
                item["URL"] = url
                item["WritedAt"] = self.writed_at_transformer(comment["regTime"])
                item["Content"] = comment["contents"]

                # 결과 값 반환
                yield item

            # 다음 댓글의 ID를 추출해 변수 next_comment에 할당
            next_comment = json.loads(re.search("\((.*)\)\;", res.text).group(1))["result"]["morePage"]["next"]

            # 마지막 댓글의 ID를 추출해 변수 end_comment에 할당
            end_comment = json.loads(re.search("\((.*)\)\;", res.text).group(1))["result"]["morePage"]["end"]

            # 다음 댓글과 마지막 댓글이 같을 경우 댓글 크롤링 중단
            if next_comment == end_comment:
                break

            # 다음 페이지의 쿼리 스트링(Query String)을 comment_query_url에 새로 할당
            comment_query_url = f"?ticket=news&pool=cbox5&lang=ko&objectId=news{press_id}%2C{article_id}&pageSize=100&pageType=more&moreParam.next={next_comment}"

    # ----------------------------------------------------------------------------------------------------

    # writed_at_transformer() 함수 정의
    def writed_at_transformer(self, time : str) -> str:
        """
        댓글의 작성일자 문자열을 입력받아 작성일자를 추출해 변환하는 함수입니다.\n
        '연-월-일'로 구성된 문자열(String) 객체를 반환합니다.
        """

        # ① strptime() 메서드를 사용해 datetime 객체로 변환
        # ② strftime() 메서드를 사용해 데이터베이스에 들어가야 할 양식의 문자열 객체로 변환해 변수 writed_at_date에 할당
        writed_at_date = datetime.strptime(time.split('+')[0], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")

        # 결과 값 반환
        return writed_at_date