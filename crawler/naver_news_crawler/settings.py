# scrapy 프로젝트에서 실행되는 봇 이름 설정
BOT_NAME = "NaverNewsCrawler"

# scrapy에서 스파이더(Spider)를 찾을 모듈의 목록을 리스트로 저장
SPIDER_MODULES = ["naver_news_crawler.spiders"]

# genspider 명령어를 사용해 새로운 스파이더를 생성할 위치를 지정
NEWSPIDER_MODULE = "naver_news_crawler.spiders"

# robots.txt 정책을 존중할지 설정
ROBOTSTXT_OBEY = False

# 사용할 아이템 파이프라인과 순서를 지정
ITEM_PIPELINES = {
   "naver_news_crawler.pipelines.MultiCSVItemPipeline": 100
}

# 웹 사이트에서 각 값을 가져오기 위해 대기할 시간을 설정
DOWNLOAD_DELAY = 0.15

# 로그 파일을 생성 및 덮어쓰기 설정
LOG_FILE = "naver_news_crawler.log"
LOG_FILE_APPEND = False

# Request Fingerprinter() 클래스에 사용할 알고리즘 버전 설정
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

# Reactor 객체를 불러올 경로 설정
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"