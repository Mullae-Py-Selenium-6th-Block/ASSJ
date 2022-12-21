# 필요한 패키지 불러오기
import pandas as pd
from datetime import datetime
import requests
import json

result=[]

headers = {
    'authority': 'apis.naver.com',
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ab.storage.userId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22browser-1625985144309-6%22%2C%22c%22%3A1626101500089%2C%22l%22%3A1626101500089%7D; ab.storage.deviceId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%224cbe130c-6edd-d4aa-a78d-290b003c3592%22%2C%22c%22%3A1626101500094%2C%22l%22%3A1626101500094%7D; ASID=7992e0220000017aaa36664e0000004e; _ga=GA1.2.612969395.1626832328; ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%2228148006-e01d-7623-b7d1-b4fff0f59b4e%22%2C%22e%22%3A1627919390179%2C%22c%22%3A1627908091281%2C%22l%22%3A1627917590179%7D; MM_NEW=1; NFS=2; NNB=RDIIILNX6JCWE; nx_ssl=2; nid_inf=1665554565; NID_AUT=tP3V5ox533EjyAgkJ1JaqWEnPOhXs2hr3teD39pK972fuXqDWQZXoIOMzICJpa1A; NID_JKL=d393brIzilbjw+7TVvG0OW6Eo22+WIhQAfihItUdgbY=; _naver_usersession_=SPdJTrlTMrn8Udkyn58eo6HL; NID_SES=AAABwJaKJ5FjUAETXL8SAX2HKMUSTt3l8pPu49OSzbGzgKEEMN/ckpP4DbQVHQwTV1hVPWtbpP7Nomg0CbD8TtCpyOYbeq8+OpHb5eWbDsXXCeLHO4epgthLtbQHiBE8spXqEtx/h0D6MzxsIlN4pa8gz51jV+oWzQQNnpQCeaKKLaxcpMfhGXnZv4BK1Rg+TAgUFE9RtExcKjteTL2hB9tKT41C7antdQdhLfVXWUbsJ/q5b62iDZnnZUAANXHnWp/9RI2YyKSn70SVu4Bag+fxA/23OqjCHSbK5RMiNOQKV+Bs7uugaAsMKkH6lGBBIbNDkTXGZ4n1+KbqFwe1kV9oCaPJ+siwXESEqvY0jaLVNAqUATQZjnIMFIYwARw41FTuduxW1IOF7MdP7R3EqOvnqNir2lXW1UfRlHlOtMC4w/tXk8xqJR/HVlZrnltKkMZB5zfyDNvnt02jbOKJcORjmOeVvL+xoCdSXwZclfJzRkC31l43+9jSu4X8RPUfuJILRMHf2e1A0NU7Mwds7h+S//5AD0yUJlPtFFzLvriuD1SMTRXiSwN4pNWBi6UIsPzScRpyLMc8hUE8Bi8jJtGk4e0=; NDARK=N; page_uid=hrKUflprvN8ssNc4Muwssssss3R-382317; BMR=',
    'referer': 'https://n.news.naver.com/article/028/0002595736',
    'sec-ch-ua': '"Whale";v="3", " Not;A Brand";v="99", "Chromium";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.108 Whale/3.15.136.18 Safari/537.36',
}

def comment(url_list):
    total_comment = [] # 댓글 내용을 담는 리스트
    comment_date=[] # 댓글 작성일을 담는 리스트
    for url_ex in url_list:
        try:
            url = url_ex
            url = url.split('?')[0]
            oid_1 = url.split('/')[-1]
            oid_2 = url.split('/')[-2]
            i = 1
        except:
            pass
        # df = pd.DataFrame(columns=['댓글'])

        while True:
            params = {
                'ticket': 'news',
                'templateId': 'default_society',
                'pool': 'cbox5',
                'lang': 'ko',
                'country': 'KR',
                'objectId': f'news{oid_2},{oid_1}',
                'pageSize': '100',
                'indexSize': '10',
                'page': str(i),
                'currentPage': '0',
                'moreParam.direction': 'next',
                'moreParam.prev': '10000o90000op06guicil48ars',
                'moreParam.next': '1000050000305guog893h1re',
                'followSize': '100',
                'includeAllStatus': 'true',
            }

            response = requests.get('https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json', params=params, headers=headers)
            response.encoding = "UTF-8-sig"
            res = response.text.replace("_callback(","")[:-2]
            temp=json.loads(res) 
            # print(temp)

            try : 
                comment = temp['result']['commentList']

                # print(comment)
                for j in range(len(comment)):
                    total_comment.append(comment[j]['contents'])
                    comment_date.append(comment[j]['regTime'].split('T')[0])
                if len(comment)<97: 
                    break 
                else: 
                    i+=1
            except :
                break    

    return comment_date, total_comment

url_csv=pd.read_csv('naver_news_url.csv')
url_list=url_csv['news_url'].to_list()
comment_date, total_comment= comment(url_list)

data = {"WritedAt" : comment_date,"Content":total_comment}
df = pd.DataFrame(data)
df.to_csv('naver_comment.csv', index=False)
# print(df)