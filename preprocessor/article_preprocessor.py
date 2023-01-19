# 필요한 패키지 불러오기
import pandas as pd
import os
import re
from konlpy.tag import Mecab

# ----------------------------------------------------------------------------------------------------

# 해당 파일을 직접 실행하는 경우 CSV 파일 입출력 경로 설정
if __name__ == "__main__":
    IMPORT_DIR = "./../data/"
    EXPORT_DIR = "./../data/"

# 해당 파일을 직접 실행하지 않는 경우 CSV 파일 입출력 경로 설정
else:
    IMPORT_DIR = "./data/"
    EXPORT_DIR = "./data/"

# ----------------------------------------------------------------------------------------------------

# ArticlePreprocessor() 클래스 정의
class ArticlePreprocessor:

    # __init__() 함수 정의
    def __init__(self):
        """
        여러 CSV 파일로 저장된 뉴스 기사 내용을 불러와 전처리를 수행하고 다시 하나의 CSV 파일로 저장하는 클래스 객체입니다.
        """

        # 뉴스 기사의 작성일자, 제목, 본문, URL을 담을 데이터프레임 news_df 초기화
        news_df = pd.DataFrame(columns = ["WritedAt", "Title", "Content", "URL"])

        # listdir() 함수를 사용해 CSV 파일의 경로에 담긴 파일 목록을 리스트 file_list에 할당
        file_list = os.listdir(IMPORT_DIR)

        # for 반복문을 사용해 파일 목록에 담긴 각 파일을 순회
        for file in file_list:

            # 뉴스 기사를 담은 CSV 파일인 경우 데이터프레임 temp_df로 변환
            if "naver_news_article" in file:
                temp_df = pd.read_csv(IMPORT_DIR + file, header = 0, encoding = "utf-8-sig")

                # concat() 함수를 사용해 news_df에 temp_df를 병합
                news_df = pd.concat([news_df, temp_df], axis = 0, ignore_index = True)

        # 전처리 전의 뉴스 기사 데이터를 raw_data 속성에 저장
        self.raw_data = news_df

        # 불용어 목록 파일을 불러와 stopwords 속성에 저장
        with open("./korean_stopwords.txt", "r", encoding = "utf-8-sig") as file:
            self.stopwords = [line.replace("\n", "") for line in file.readlines()]

        # 오타 목록 파일을 불러와 typos 속성에 저장
        with open("./korean_typos.txt", "r", encoding = "utf-8-sig") as file:
            self.typos = [line.replace("\n", "") for line in file.readlines()]

    # ----------------------------------------------------------------------------------------------------

    # fit() 함수 정의
    def fit(self):
        """
        CSV 파일로부터 불러온 raw_data 속성 값을 활용해 전처리 작업을 수행하고 CSV 파일로 저장하는 함수입니다.
        """

        # 전처리된 결과를 담을 preprocessed_data 데이터프레임 초기화
        preprocessed_data = self.raw_data.copy()

        # text_cleanser() 함수를 호출해 불필요한 내용 제거 작업 수행 후 안내 메시지 출력
        preprocessed_data["Content"] = preprocessed_data["Content"].apply(self.text_cleanser)
        print(">>> 뉴스 기사 내용의 클렌징 작업이 완료되었습니다.\n")

        # text_preprocessor() 함수를 호출해 형태소 분석, 품사 태깅, 불용어 제거 작업 수행 후 안내 메시지 출력
        preprocessed_data["Content"] = preprocessed_data["Content"].apply(self.text_preprocessor)
        print(">>> 뉴스 기사 내용의 전처리 작업이 완료되었습니다.\n")

        # dropna() 메서드를 사용해 결측값을 제거 후 안내 메시지 출력
        preprocessed_data.dropna(axis = 0, how = "any", inplace = True)
        print(">>> 뉴스 기사 내용이 결측값인 경우를 제거하였습니다.\n")

        # csv_exporter() 함수를 호출해 전처리 결과를 CSV 파일로 저장하고 안내 메시지 출력
        self.csv_exporter(preprocessed_data)
        print(">>> 네이버 뉴스 기사 전처리 결과가 CSV 파일로 저장되었습니다.\n")

    # ----------------------------------------------------------------------------------------------------

    # text_cleanser() 함수 정의
    def text_cleanser(self, news_text : str) -> str:
        """
        뉴스 기사의 내용이 담긴 문자열을 입력 받아 문장 부호와 불필요한 내용을 제거하는 함수입니다.\n
        전처리된 뉴스 기사 내용이 담긴 문자열(String)을 반환합니다.
        """

        # compile() 함수를 사용해 괄호 안의 모든 문자, 기자명, 이메일, 한글을 제외한 모든 문자를 패턴으로 저장
        parenthesize_pattern = re.compile(r"\([^)]+\)|\[[^]]+\]|\<[^>]+\>|\{[^}]+\}|\〈[^〉]+\〉|\《[^》]+\》|\【[^\】]*\】|\＜[^\＞]*\＞")
        reporter_pattern = re.compile(r"([가-힣]{2,5} 기자)|([가-힣]{2,5}기자)")
        email_pattern = re.compile(r"([a-zA-Z0-9-]+(\@|\.)[a-zA-Z0-9-.]+)")
        no_korean_pattern = re.compile(r"[^가-힣ㄱ-ㅎㅏ-ㅣ ]")

        # sub() 메서드를 사용해 괄호 안의 모든 문자, 기자명, 이메일, 한글을 제외한 모든 문자를 차례로 제거
        news_text = parenthesize_pattern.sub("", news_text).strip()
        news_text = reporter_pattern.sub("", news_text).strip()
        news_text = email_pattern.sub("", news_text).strip()
        news_text = no_korean_pattern.sub("", news_text).strip()

        # replace() 메서드를 사용해 줄바꿈을 제거
        news_text = news_text.replace("\n", "").replace("\t", "")

        # 결과 값 반환
        return news_text

    # ----------------------------------------------------------------------------------------------------

    # text_preprocessor() 함수 정의
    def text_preprocessor(self, news_text : str) -> str:
        """
        뉴스 기사의 내용이 담긴 문자열을 입력 받아 전처리를 수행하는 함수입니다.\n
        전처리된 뉴스 기사 내용이 담긴 문자열(String)을 반환합니다.
        """

        # morpheme_analyzer() 함수를 호출해 형태소 분석을 한 결과를 news_token에 할당
        news_token = self.morpheme_analyzer(news_text)

        # tag_selector() 함수를 호출해 필요한 품사만 남긴 결과를 selected_token에 할당
        selected_token = self.tag_selector(news_token)

        # stopwords_remover() 함수를 호출해 불용어를 제거한 결과를 preprocessed_text에 할당
        preprocessed_text = self.stopwords_remover(selected_token)

        # 결과 값 반환
        return preprocessed_text

    # ----------------------------------------------------------------------------------------------------

    # morpheme_analyzer() 함수 정의
    def morpheme_analyzer(self, news_text : str) -> list:
        """
        뉴스 기사의 내용이 담긴 문자열을 입력 받아 형태소 분석을 하는 함수입니다.\n
        형태소 분석의 결과가 담긴 리스트(List)를 반환합니다.
        """

        # Mecab 형태소 분석기를 tokenizer 변수에 할당
        tokenizer = Mecab()

        # morphs() 메서드를 사용해 형태소 분석을 한 결과를 news_token에 할당
        news_token = tokenizer.morphs(news_text)

        # 결과 값 반환
        return news_token
    
    # ----------------------------------------------------------------------------------------------------

    # tag_selector() 함수 정의
    def tag_selector(self, news_token : list) -> list:
        """
        형태소 분석의 결과가 담긴 리스트를 입력 받아 필요한 품사만 선택하는 함수입니다.\n
        특정 품사에 해당하는 형태소 목록만 담긴 리스트(List)를 반환합니다.
        """

        # 선택된 품사를 담은 딕셔너리 selected_tag_dict 초기화
        selected_tag_dict = {"NNG": "일반명사", "NNP": "고유명사"}

        # Mecab 형태소 분석기를 tokenizer 변수에 할당
        tokenizer = Mecab()

        # pos() 메서드를 사용해 품사 태깅 작업을 수행한 결과를 pos_token에 할당
        pos_token = tokenizer.pos(" ".join(news_token))

        # 리스트 컴프리헨션(List Comprehension)을 사용해 선택된 품사에 해당하는 형태소만 selected_token에 할당
        selected_token = [token[0] for token in pos_token if token[1] in selected_tag_dict.keys()]

        # 결과 값 반환
        return selected_token

    # ----------------------------------------------------------------------------------------------------

    # stopwords_remover() 함수 정의
    def stopwords_remover(self, selected_token : list) -> str:
        """
        형태소 분석의 결과가 담긴 리스트를 입력 받아 불용어를 제거하는 함수입니다.\n
        불용어 목록을 불러와 불용어를 제거하고 리스트를 문자열로 병합해 반환합니다.
        """

        # 불용어 목록에 포함되지 않는 단어만 리스트 컴프리헨션(List Comprehension)으로 반환
        preprocessed_token = [token for token in selected_token if token not in self.stopwords]

        # join() 메서드를 사용해 각 단어 토큰을 하나의 문자열로 병합
        preprocessed_text = " ".join(preprocessed_token)

        # for 반복문 및 replace() 메서드를 사용해 잘못된 띄어쓰기를 수정
        for typo in self.typos:
            preprocessed_text = preprocessed_text.replace(typo.split(" / ")[0], typo.split(" / ")[1])

        # 결과 값 반환
        return preprocessed_text

    # ----------------------------------------------------------------------------------------------------

    # csv_exporter() 함수 정의
    def csv_exporter(self, result_df : pd.DataFrame):
        """
        전처리된 뉴스 기사가 담긴 데이터프레임을 CSV 파일로 저장하는 함수입니다.\n
        저장되는 CSV 파일의 이름은 'preprocessed_naver_news_article.csv'입니다.
        """

        # to_csv() 메서드를 사용해 데이터프레임을 CSV 파일로 저장
        result_df.to_csv(EXPORT_DIR + "preprocessed_naver_news_article.csv", index = False, encoding = "utf-8-sig")

# ----------------------------------------------------------------------------------------------------

# 해당 파일을 직접 실행하는 경우
if __name__ == "__main__":

    # fit() 메서드를 사용해 전처리된 뉴스 기사 내용을 담은 CSV 파일을 생성
    article_preprocessor = ArticlePreprocessor()
    article_preprocessor.fit()