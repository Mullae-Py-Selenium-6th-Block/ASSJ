# 필요한 패키지 불러오기
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import json
from googleapiclient.discovery import build
import os

# ----------------------------------------------------------------------------------------------------

# YoutubeURLCrawler() 클래스 정의
class YoutubeURLCrawler:

    # __init__() 함수 정의
    def __init__(self, keyword : str, start_year : int, end_year : int):
        """
        검색어, 검색할 기간의 시작연도, 종료연도를 입력받아 크롤링을 수행하는 클래스 객체입니다.\n
        - [인수 ①] keyword: 검색어, 공백은 +로 구분해 입력 (예) '서울+아파트+가격'\n
        - [인수 ②] start_year: 검색할 기간의 시작연도, 'yyyy'의 형식으로 입력 (예) 2013\n
        - [인수 ③] end_year: 검색할 기간의 종료연도, 'yyyy'의 형식으로 입력 (예) 2022
        """

        # 입력 받은 검색어, 검색 기간 시작연도, 종료연도를 각 속성에 저장
        self.keyword = keyword
        self.start_year = start_year
        self.end_year = end_year

        # month_separator() 함수를 실행해 검색 기간을 한 달 단위로 분할한 각 시점의 리스트를 속성으로 저장
        self.after_list, self.before_list = self.month_separator()

    # ----------------------------------------------------------------------------------------------------

    # search() 함수 정의
    def search(self):
        """
        각 월별로 유튜브 동영상 ID(Video ID)를 크롤링해 연도별 CSV 파일로 결과를 저장하는 함수입니다.
        """

        # 각 연도를 12개월로 구분하기 위한 year_count 변수 초기화
        year_count = 0

        # 입력받은 검색 시작연도를 변수 year에 할당
        year = self.start_year

        # 크롤링의 시작을 알리는 안내 메시지 출력
        print(">>> 유튜브 동영상 ID 크롤링을 시작합니다.\n")

        # while 반복문을 사용해 각 12개월을 순회
        while year_count != len(self.after_list) // 12: 

            # 크롤링한 결과를 담을 데이터프레임 result_df 초기화
            result_df = pd.DataFrame(columns = ["Title", "VideoID"])

            # for 반복문을 사용해 1년의 각 달을 순회
            for period in range(0 + (12 * year_count), 12 + (12 * year_count)):

                # video_id_collector() 함수를 호출해 크롤링한 결과를 데잍터프레임 temp_df에 할당
                temp_df = self.video_id_collector(self.keyword, self.after_list[period], self.before_list[period])

                # concat() 함수를 사용해 result_df에 temp_df를 병합
                result_df = pd.concat([result_df, temp_df], axis = 0, ignore_index = True)

                # 크롤링의 완료를 알리는 안내 메시지 출력
                print(">>> {0}년 {1}월 유튜브 동영상 ID 크롤링이 완료되었습니다.\n".format(year, period % 12 + 1))

            # csv_exporter() 함수를 호출해 해당 연도의 크롤링 결과를 CSV 파일로 저장하고 안내 메시지 출력
            self.csv_exporter(result_df, year)
            print(">>> {0}년 유튜브 동영상 ID 수집 결과가 CSV 파일로 저장되었습니다.\n".format(year))

            # CSV 파일로 저장할 연도와 year_count 변수 각각 조정
            year_count += 1
            year += 1
    
    # ----------------------------------------------------------------------------------------------------

    # month_separator() 함수 정의
    def month_separator(self) -> tuple:
        """
        검색 기간 시작연도, 종료연도를 기준으로 각 월별로 기간을 분할하는 함수입니다.\n
        매월 첫 날과 마지막 날이 각각 담긴 리스트(List)로 구성된 튜플(Tuple)을 반환합니다.
        """
    
        # date_range() 함수를 사용하여 수집할 한 달 간의 날짜를 담은 after_list, before_list 리스트 생성
        after_list = pd.date_range(f"{self.start_year}-01-01", f"{self.end_year}-12-31", freq = "MS").strftime("%Y-%m-%d").tolist()
        before_list =  pd.date_range(f"{self.start_year}-01-01", f"{self.end_year}-12-31", freq = "M").strftime("%Y-%m-%d").tolist()

        # 결과 값 반환
        return after_list, before_list

    # ----------------------------------------------------------------------------------------------------

    # video_id_collector() 함수 정의
    def video_id_collector(self, keyword : str, after : str, before : str) -> pd.DataFrame:
        """
        유튜브(Youtube)에서 특정 기간 내에서 특정 검색어로 검색한 결과를 수집하는 함수입니다.\n
        검색 결과로 나오는 모든 동영상의 제목과 URL로 사용되는 영상 ID(Video ID)를 크롤링해 판다스(pandas) 데이터프레임(Dataframe)을 반환합니다.
        """

        # 크롤링의 시작을 알리는 메시지를 출력
        print(">>> [{0}]부터 [{1}]까지 검색어 [{2}]에 대한 유튜브 영상을 검색합니다.\n".format(after, before, keyword.replace("+", " ")))

        # 백그라운드 사용 및 불필요한 오류 메시지 출력 방지 설정
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        # 크롬(Chrome) 웹 드라이버를 변수 driver에 할당
        driver = webdriver.Chrome(options = options, service = ChromeService(ChromeDriverManager().install()))

        # get() 메서드를 사용해 검색 결과 URL 웹 페이지를 불러오기
        driver.get("https://www.youtube.com/results?search_query={0}+after%3A{1}+before%3A{2}".format(keyword, after, before))

        # while 반복문을 사용해 스크롤바를 계속해서 이동
        while True:

            # execute_script() 메서드를 사용해 스크롤 바를 웹 페이지의 높이만큼 이동
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")

            # sleep() 함수를 사용해 2초간 시간 지연으로 웹 드라이버가 새 목록을 불러올 시간 확보
            time.sleep(2)

            # find_element() 메서드를 사용해 더 이상 검색 결과가 없음을 알려주는 메시지를 변수 end_message에 할당
            end_message = driver.find_element(By.ID, "message")

            # 더 이상 결과가 없음을 알려주는 메시지가 나타난 경우 안내 메시지 출력 후 스크롤 중단
            if end_message.text == "결과가 더 이상 없습니다.":
                print(">>> 검색 결과를 모두 불러왔습니다.\n")
                break
        
        # find_elements() 메서드를 사용해 동영상 목록을 추출하고 video_list에 할당
        video_list = driver.find_elements(By.ID, "video-title")

        # 추출한 결과를 저장할 리스트 result 초기화
        result = []

        # for 반복문을 사용해 동영상 목록의 각 동영상 순회
        for video in video_list:

            # 동영상 제목과 ID를 추출해 각 변수에 할당
            video_title = video.text
            video_url = video.get_attribute("href")
            
            # URL이 존재하지 않는 경우 해당 동영상을 제외
            if video_url == None: continue

            # 유튜브 쇼츠(Youtube Shorts) 동영상을 제외
            if "shorts" in video_url: continue
        
            # append() 메서드를 사용해 동영상 제목과 ID를 리스트에 추가
            result.append([video_title, video_url.split("=")[1]])

        # 동영상 제목과 ID를 데이터프레임으로 변환해 result_df에 할당
        result_df = pd.DataFrame(result, columns = ["Title", "VideoID"])

        # close() 메서드를 사용해 크롬 웹 드라이버를 종료
        driver.close()

        # 결과 값 반환
        return result_df

    # ----------------------------------------------------------------------------------------------------

    # csv_exporter() 함수 정의
    def csv_exporter(self, result_df : pd.DataFrame, year : int):
        """
        동영상 ID(Video ID)가 담긴 데이터프레임을 CSV 파일로 저장하는 함수입니다.\n
        저장되는 CSV 파일의 이름은 'youtube_url_특정연도.csv'입니다.
        """

        # CSV 파일을 저장할 경로를 export_dir에 할당
        export_dir = "./../../data/"

        # to_csv() 메서드를 사용해 데이터프레임을 CSV 파일로 저장
        result_df.to_csv(export_dir + f"youtube_url_{year}.csv", index = False, encoding = "utf-8-sig")

# ----------------------------------------------------------------------------------------------------

# YoutubeCommentCrawler() 클래스 정의
class YoutubeCommentCrawler:

    # __init__() 함수 정의
    def __init__(self, start_year : int, end_year : int):
        """
        검색할 기간을 입력받아 CSV 파일로 저장된 동영상 주소에서 유튜브 댓글 크롤링을 수행하는 클래스 객체입니다.\n
        - [인수 ①] start_year: 검색할 기간의 시작연도, 'yyyy'의 형식으로 입력 (예) 2013\n
        - [인수 ②] end_year: 검색할 기간의 종료연도, 'yyyy'의 형식으로 입력 (예) 2022
        """

        # 입력 받은 댓글을 가져올 시작연도와 종료연도를 각 속성에 저장
        self.start_year = start_year
        self.end_year = end_year

    # ----------------------------------------------------------------------------------------------------

    # get() 함수 정의
    def get(self):
        """
        각 연도별로 유튜브 동영상 댓글을 크롤링해 CSV 파일로 결과를 저장하는 함수입니다.
        """

        # 크롤링의 시작을 알리는 안내 메시지 출력
        print(">>> 유튜브 댓글 크롤링을 시작합니다.\n")

        # for 반복문을 사용해 시작연도부터 종료연도까지 순회
        for year in range(self.start_year, self.end_year + 1):

            # comment_collector() 함수를 호출해 크롤링한 결과를 데이터프레임 result_df에 할당
            result_df = self.comment_collector(year)

            # 크롤링의 완료를 알리는 안내 메시지 출력
            print(">>> {0}년 유튜브 댓글 크롤링이 완료되었습니다.\n".format(year))

            # csv_exporter() 함수를 호출해 해당 연도의 크롤링 결과를 CSV 파일로 저장하고 안내 메시지 출력
            self.csv_exporter(result_df, year)
            print(">>> {0}년 유튜브 댓글 수집 결과가 CSV 파일로 저장되었습니다.\n".format(year))

    # ----------------------------------------------------------------------------------------------------

    # comment_collector() 함수 정의
    def comment_collector(self, year : int) -> pd.DataFrame:
        """
        동영상 ID(Video ID)가 저장된 CSV 파일정보를 활용하여 유튜브 댓글을 크롤링하는 함수입니다.\n
        YouTube Data API를 사용하여 각 동영상의 댓글을 수집한 결과를 담은 판다스(pandas) 데이터프레임(Dataframe)을 반환합니다.
        """

        # API 키(Key)를 api_config.json 파일에서 가져와 api_key 변수에 할당
        with open("./api_config.json", "r") as file:
            data = json.load(file)
            api_key = data["API-KEY"]

        # build() 함수를 사용해 API 객체를 youtube_api에 할당
        youtube_api = build(serviceName = "youtube", version = "v3", developerKey = api_key)

        # CSV 파일을 불러올 경로를 import_dir에 할당
        import_dir = "./../../data/"

        # 동영상 ID가 담긴 CSV 파일이 존재하는 경우 불러와 데이터프레임 video_df에 할당
        if os.path.isfile(import_dir + f"youtube_url_{year}.csv"):
            video_df = pd.read_csv(import_dir + f"youtube_url_{year}.csv", header = 0, encoding = "utf-8-sig")
        
        # 동영상 ID가 담긴 CSV 파일이 존재하지 않는 경우 오류 메시지 출력
        else:
            raise Exception(">>> 동영상 ID가 담긴 CSV 파일이 존재하지 않습니다. 먼저 동영상 ID 크롤링을 수행했는지 확인해 주십시오.\n")

        # 추출한 결과를 저장할 리스트 result 초기화
        result = []

        # for 반복문을 사용해 video_df의 각 행을 순회
        for title, video_id in zip(video_df["Title"], video_df["VideoID"]):

            # 댓글 사용 중지 상태가 아닌 경우 commentThreads().list() 메서드를 사용해 댓글 목록을 가져와 response에 할당
            try: response = youtube_api.commentThreads().list(part = "snippet,replies", videoId = video_id, maxResults = 100).execute()

            # 댓글 사용 중지 상태인 경우 다음 동영상으로 이동
            except: continue

            # while 반복문을 사용해 댓글 목록을 100개씩 차례로 순회
            while response:

                # for 반복문을 사용해 각 아이템을 순회하며 영상 제목, 댓글 내용, 댓글 작성시간, 좋아요 수를 추출해 리스트 result에 추가
                for item in response["items"]:
                    content = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                    writed_at = item["snippet"]["topLevelComment"]["snippet"]["publishedAt"].split("T")[0]
                    like_count = item["snippet"]["topLevelComment"]["snippet"]["likeCount"]
                    result.append([title, content, writed_at, like_count])

                    # 댓글의 댓글이 존재하는 경우 영상 제목, 댓글 내용, 댓글 작성시간, 좋아요 수를 추출해 리스트 result에 추가
                    if "replies" in item.keys():
                        for reply_item in item["replies"]["comments"]:
                            reply_content = reply_item["snippet"]["textDisplay"]
                            reply_writed_at = reply_item["snippet"]["publishedAt"].split("T")[0]
                            reply_like_count = reply_item["snippet"]["likeCount"]
                            result.append([title, reply_content, reply_writed_at, reply_like_count])

                # 다음 페이지가 존재하는 경우, 다음 페이지를 호출해 response에 할당            
                if "nextPageToken" in response:
                    response = youtube_api.commentThreads().list(
                        part = "snippet,replies",
                        videoId = video_id,
                        pageToken = response["nextPageToken"],
                        maxResults = 100
                    ).execute()

                # 다음 페이지가 존재하지 않는 경우 while 반복문 탈출
                else: break
        
        # 동영상 제목과 댓글 내용, 댓글 작성일자, 댓글 좋아요 수를 데이터프레임으로 변환해 result_df에 할당
        result_df = pd.DataFrame(result, columns = ["Title", "Content", "WritedAt", "LikeCount"])

        # 결과 값 반환
        return result_df

    # ----------------------------------------------------------------------------------------------------

    # csv_exporter() 함수 정의
    def csv_exporter(self, result_df : pd.DataFrame, year : int):
        """
        유튜브 댓글이 담긴 데이터프레임을 CSV 파일로 저장하는 함수입니다.\n
        저장되는 CSV 파일의 이름은 'youtube_comment_특정연도.csv'입니다.
        """

        # CSV 파일을 저장할 경로를 export_dir에 할당
        export_dir = "./../../data/"

        # to_csv() 메서드를 사용해 데이터프레임을 CSV 파일로 저장
        result_df.to_csv(export_dir + f"youtube_comment_{year}.csv", index = False, encoding = "utf-8-sig")

# ----------------------------------------------------------------------------------------------------

# 해당 파일을 직접 실행하는 경우
if __name__ == "__main__":

    # search() 메서드를 사용해 URL을 담은 CSV 파일을 생성
    url_crawler = YoutubeURLCrawler("서울+아파트+가격", 2013, 2022)
    url_crawler.search()

    # get() 메서드를 사용해 댓글을 담은 CSV 파일을 생성
    comment_crawler = YoutubeCommentCrawler(2013, 2022)
    comment_crawler.get()