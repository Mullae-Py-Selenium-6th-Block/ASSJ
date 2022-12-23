# 필요한 패키지 불러오기
import pandas as pd
import os
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from googleapiclient.discovery import build

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
        각 월별로 유튜브 동영상 ID(Video ID)를 크롤링해 연도별로 CSV 파일로 결과를 저장하는 함수입니다.
        """

        # 각 월별 
        month_count = 0
        after = self.start_year

        while month_count != len(self.after_list) // 12: 
            
            result_df = pd.DataFrame()

            # 1년치 데이터만 하나의 데이터프레임에 담아 csv파일로 추출
            for period in range(0 + (12 * month_count), 12 + (12* month_count)):
                temp_df = self.video_id_collector(self.keyword, self.after_list[period], self.before_list[period])
                result_df = pd.concat([result_df, temp_df], axis = 0, ignore_index = True)

            # 서울 아파트 가격과 관련 없는 동영상 제목들 drop
            drop_index = result_df[result_df['title'].str.contains('서울|집|아파트|가격|값|부동산')==False].index
            new_df = result_df.drop(drop_index, axis=0)
            self.csv_exporter(new_df, after)

            after += 1
            month_count += 1

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
        검색 결과로 나오는 모든 동영상의 제목과 URL로 사용되는 영상 ID(Video ID)를 크롤링해 판다스(pandas) 데이터프레임(Dataframe)을 반환합니다.\n

        """

        # 크롤링의 시작을 알리는 메시지를 출력
        print(">>> [{0}]부터 [{1}]까지 검색어 [{2}]에 대한 유튜브 영상을 검색합니다.".format(after, before, keyword.replace("+", " ")))

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options = options, service = ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.youtube.com/results?search_query={0}+after%3A{1}+before%3A{2}".format(keyword, after, before))

        scroll_pane_height = driver.execute_script('return document.documentElement.scrollHeight')

        # 무한 스크롤 시작
        while True:
            driver.execute_script('window.scrollTo(0,document.documentElement.scrollHeight)')
            # 딜레이 생성
            time.sleep(2)
            new_scroll_pane_height = driver.execute_script('return document.documentElement.scrollHeight')

            message = driver.find_element(By.XPATH, '//*[@id="message"]')

            if message.text == "결과가 더 이상 없습니다.":
                print('결과가 더 이상 없습니다.')
                break

            scroll_pane_height = new_scroll_pane_height
        
        datas = driver.find_elements(By.XPATH, r'//*[@id="video-title"]')

        videos = []
        for data in datas:
            url = data.get_attribute('href')
            title = data.text
            
            if url == None:
                pass
            # 쇼츠 동영상 제외
            elif 'shorts' in url:
                pass
            else:
                # api 사용을 위해 videoId만 저장
                videos.append([title, url.split('=')[1]])

        driver.close()
        video_info = pd.DataFrame(videos, columns=['title', 'videoId'])

        return video_info
# ----------------------------------------------------------------------------------------------------

    def csv_exporter(self, df : pd.DataFrame, after : int):
        """
        video_id가 담긴 df를 받아 csv로 저장하는 함수입니다.\n
        파일 이름: youtube_comment_특정연도.csv (ex: youtube_comment_2013.csv)
        """

        PATH = "./data/"
        df.to_csv(PATH + f"youtube_video_{after}.csv", encoding='utf-8')

        return None

    # ----------------------------------------------------------------------------------------------------

def get_comment_info(self, year : int):
        '''
        video_id정보를 활용하여 유튜브 댓글 크롤링하는 함수\n
        기간을 정하면 그 기간내 영상정보 csv파일을 불러와 video_id를 이용해 댓글을 크롤링한다.\n
        유튜브 api를 사용하여 댓글 정보 크롤링 데이터프레임을 반환하고 csv로 저장한다.
        '''
        comments = list()

        # API키 config파일에서 불러오기
        # developerKey=APIKey (따옴표 없이 저장)
        with open('./.config', 'r') as f:
            for l in f.readlines():
                devloperKey = l.split('=')[1]
        
        api_obj = build('youtube', 'v3', developerKey=devloperKey)
                
        # csv파일 불러오기
        PATH = './data/'
        # 해당연도의 csv파일을 불러온다
        file = f'youtube_video_{year}.csv'

        if os.path.isfile(PATH + file):
            video_info = pd.read_csv(PATH + file)
        else:
            print('Nothing in directory. Please check the file name.')
        
        for title, video_id in zip(video_info['title'], video_info['videoId']):
            try:
                response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, maxResults=100).execute()
            except: # 댓글 중지 상태인 경우
                continue # 다음 비디오로 넘어가야 함

            while response:
                for item in response['items']:
                    comment = item['snippet']['topLevelComment']['snippet']
                    comment_pubished_at = comment['publishedAt'].split('T')[0]
                    comments.append([title, comment['textDisplay'], comment_pubished_at, comment['likeCount']])
                    # 대댓글이 있는 경우
                    if item['snippet']['totalReplyCount'] > 0:
                        for reply_item in item['replies']['comments']:
                            reply = reply_item['snippet']
                            reply_published_at = reply['publishedAt'].split('T')[0]
                            comments.append([title, reply['textDisplay'], reply_published_at, reply['likeCount']])
            
                if 'nextPageToken' in response:
                    response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, pageToken=response['nextPageToken'], maxResults=100).execute()
                else:
                    break
        
        comment_info = pd.DataFrame(comments, columns=['title', 'comment', 'publishedAt', 'likeCount'])
        file_name = f'yotube_comments_{year}.csv'
        comment_info.to_csv(PATH + file_name, encoding='utf-8')

        return comment_info

# 해당 파일을 직접 실행하는 경우
if __name__ == "main":
    url_crawler = YoutubeURLCrawler("서울+아파트+가격", 2013, 2013)
    url_crawler.search()