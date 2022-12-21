import os
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
from googleapiclient.discovery import build

import warnings # 경고창 무시
warnings.filterwarnings('ignore')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# keyword = '서울+아파트+가격'
def get_url_info(keyword: str, after: str, before: str):
    '''
    검색한 단어의 모든 동영상의 제목과 videoId를 크롤링하는 함수\n
    - keyword: 검색 단어. 공백은 +로 구분한다. (ex: '서울+집값')\n
    - after: 이후로 검색할 날짜('yyyy-mm-dd')\n
    - before: 이전으로 검색할 날짜('yyyy-mm-dd')\n
    해당 단어로 검색한 동영상 목록 전체를 크롤링하여 데이터프레임을 반환하고 csv로 저장한다.
    '''

    URL = r'https://www.youtube.com/results?search_query={0}+after%3A{1}+before%3A{2}'.format(keyword, after, before)
    driver.get(URL)

    scroll_pane_height = driver.execute_script('return document.documentElement.scrollHeight')

    # 무한 스크롤 시작
    while True:
        driver.execute_script('window.scrollTo(0,document.documentElement.scrollHeight)')
        # 딜레이 생성
        time.sleep(3)
        new_scroll_pane_height = driver.execute_script('return document.documentElement.scrollHeight')

        message = driver.find_element(By.XPATH, '//*[@id="message"]')

        if message.text == '결과가 더 이상 없습니다.':
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

    video_info = pd.DataFrame(videos, columns=['title', 'videoId'])
    # print(len(video_info))
    PATH = r'youtube_videos{0}~{1}.csv'.format(after, before)
    video_info.to_csv(PATH, encoding='utf-8')

    return video_info

def get_comment_info(after: str, before: str):
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
    file = r'youtube_videos{0}~{1}.csv'.format(after, before)
    if os.path.isfile(file):
        video_info = pd.read_csv(file)
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
                comments.append([title, comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
                # 대댓글이 있는 경우
                if item['snippet']['totalReplyCount'] > 0:
                    for reply_item in item['replies']['comments']:
                        reply = reply_item['snippet']
                        comments.append([title, reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])
        
            if 'nextPageToken' in response:
                response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, pageToken=response['nextPageToken'], maxResults=100).execute()
            else:
                break
    
    comment_info = pd.DataFrame(comments, columns=['title', 'comment', 'author', 'publishedAt', 'likeCount'])
    PATH = r'yotube_comments{0}~{1}.csv'.format(after, before)
    comment_info.to_csv(PATH, encoding='utf-8')

    return comment_info