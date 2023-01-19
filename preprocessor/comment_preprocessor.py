# 필요한 패키지 불러오기
import pandas as pd
import os
import re
from konlpy.tag import Mecab
from typing import Union

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

# CommentPreprocessor() 클래스 정의
class CommentPreprocessor:

    # __init__() 함수 정의
    def __init__(self, category : str = "naver"):
        """
        여러 CSV 파일로 저장된 댓글 내용을 불러와 전처리를 수행하고 다시 하나의 CSV 파일로 저장하는 클래스 객체입니다.\n
        - [인수] category: 가져올 댓글의 종류로 'naver', 'youtube' 중 하나를 입력, 기본값 - 'naver'
        """

        # 댓글의 수집 위치에 따라 데이터프레임 comment_df 초기화
        if category == "youtube": comment_df = pd.DataFrame(columns = ["Title", "Content", "WritedAt", "LikeCount"])
        else: comment_df = pd.DataFrame(columns = ["URL", "WritedAt", "Content"])

        # listdir() 함수를 사용해 CSV 파일의 경로에 담긴 파일 목록을 리스트 file_list에 할당
        file_list = os.listdir(IMPORT_DIR)

        # for 반복문을 사용해 파일 목록에 담긴 각 파일을 순회
        for file in file_list:

            # 유튜브 댓글인 경우
            if category == "youtube":

                # 뉴스 댓글를 담은 CSV 파일인 경우 데이터프레임 temp_df로 변환
                if "youtube_comment" in file:
                    temp_df = pd.read_csv(IMPORT_DIR + file, header = 0, encoding = "utf-8-sig")

                    # concat() 함수를 사용해 news_df에 temp_df를 병합
                    comment_df = pd.concat([comment_df, temp_df], axis = 0, ignore_index = True)

            # 네이버 뉴스 댓글인 경우
            else:

                # 뉴스 댓글를 담은 CSV 파일인 경우 데이터프레임 temp_df로 변환
                if "naver_news_comment" in file:
                    temp_df = pd.read_csv(IMPORT_DIR + file, header = 0, encoding = "utf-8-sig")

                    # concat() 함수를 사용해 news_df에 temp_df를 병합
                    comment_df = pd.concat([comment_df, temp_df], axis = 0, ignore_index = True)

        # 전처리 전의 뉴스 기사 데이터와 댓글 종류를 각 속성에 저장
        self.raw_data = comment_df
        self.category = category

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

        # 유튜브 댓글인 경우
        if self.category == "youtube":

            # 서울 아파트 가격과 무관한 동영상의 인덱스를 unrelated_index에 할당
            unrelated_index = self.raw_data[self.raw_data["Title"].str.contains("서울|집|아파트|가격|값|부동산") == False].index
            
            # drop() 메서드를 사용해 무관한 동영상의 인덱스를 삭제
            self.raw_data.drop(unrelated_index, axis = 0, inplace = True)

            # reset_index() 메서드를 사용해 데이터프레임의 인덱스 재정렬
            self.raw_data.reset_index(inplace = True)

            # 불필요한 내용이 포함된 제목을 지닌 동영상 제거 작업 수행 후 안내 메시지 출력
            print(">>> 분석과 관련 없는 동영상의 댓글이 제거되었습니다.\n")

        # 전처리된 결과를 담을 preprocessed_data 데이터프레임 초기화
        preprocessed_data = self.raw_data.copy()

        # text_cleanser() 함수를 호출해 불필요한 내용 제거 작업 수행 후 안내 메시지 출력
        preprocessed_data["Content"] = preprocessed_data["Content"].apply(self.text_cleanser)
        print(">>> 댓글 내용의 클렌징 작업이 완료되었습니다.\n")

        # 각 함수를 호출해 형태소 분석, 품사 태깅, 불용어 제거 작업 수행 후 안내 메시지 출력
        preprocessed_data["Content"] = preprocessed_data["Content"].apply(self.text_preprocessor)
        print(">>> 댓글 내용의 전처리 작업이 완료되었습니다.\n")

        # dropna() 메서드를 사용해 결측값을 제거 후 안내 메시지 출력
        preprocessed_data.dropna(axis = 0, how = "any", inplace = True)
        print(">>> 댓글 내용이 결측값인 경우를 제거하였습니다.\n")

        # csv_exporter() 함수를 호출해 전처리 결과를 CSV 파일로 저장하고 안내 메시지 출력
        self.csv_exporter(preprocessed_data, self.category)
        print(">>> 댓글 전처리 결과가 CSV 파일로 저장되었습니다.\n")

    # ----------------------------------------------------------------------------------------------------

    # text_cleanser() 함수 정의
    def text_cleanser(self, comment_text : str) -> str:
        """
        댓글의 내용이 담긴 문자열을 입력 받아 문장 부호와 불필요한 내용을 제거하는 함수입니다.\n
        전처리된 댓글 내용이 담긴 문자열(String)을 반환합니다.
        """

        # compile() 함수를 사용해 괄호 안의 모든 문자, 한글을 제외한 모든 문자를 패턴으로 저장
        parenthesize_pattern = re.compile(r"\([^)]+\)|\[[^]]+\]|\<[^>]+\>|\{[^}]+\}|\〈[^〉]+\〉|\《[^》]+\》|\【[^\】]*\】|\＜[^\＞]*\＞")
        no_korean_pattern = re.compile(r"[^가-힣 ]")

        # sub() 메서드를 사용해 괄호 안의 모든 문자, 한글을 제외한 모든 문자를 차례로 제거
        comment_text = parenthesize_pattern.sub("", comment_text).strip()
        comment_text = no_korean_pattern.sub("", comment_text).strip()

        # replace() 메서드를 사용해 줄바꿈을 제거
        comment_text = comment_text.replace("\n", "").replace("\t", "")

        # 결과 값 반환
        return comment_text

    # ----------------------------------------------------------------------------------------------------
    
    # text_preprocessor() 함수 정의
    def text_preprocessor(self, comment_text : str) -> Union[None, str]:
        """
        댓글의 내용이 담긴 문자열을 입력 받아 전처리를 수행하는 함수입니다.\n
        전처리된 댓글 내용이 담긴 문자열(String)을 반환합니다.\n
        단어가 5개 미만인 댓글의 경우 None 값을 반환합니다.
        """

        # morpheme_analyzer() 함수를 호출해 형태소 분석을 한 결과를 comment_token에 할당
        comment_token = self.morpheme_analyzer(comment_text)

        # tag_selector() 함수를 호출해 필요한 품사만 남긴 결과를 selected_token에 할당
        selected_token = self.tag_selector(comment_token)

        # stopwords_remover() 함수를 호출해 불용어를 제거한 결과를 preprocessed_text에 할당
        preprocessed_text = self.stopwords_remover(selected_token)

        # 결과 값 반환
        return preprocessed_text

    # ----------------------------------------------------------------------------------------------------

    # morpheme_analyzer() 함수 정의
    def morpheme_analyzer(self, comment_text : str) -> list:
        """
        댓글의 내용이 담긴 문자열을 입력 받아 형태소 분석을 하는 함수입니다.\n
        형태소 분석의 결과가 담긴 리스트(List)를 반환합니다.
        """

        # Mecab 형태소 분석기를 tokenizer 변수에 할당
        tokenizer = Mecab()

        # morphs() 메서드를 사용해 형태소 분석을 한 결과를 comment_token에 할당
        comment_token = tokenizer.morphs(comment_text)

        # 결과 값 반환
        return comment_token
    
    # ----------------------------------------------------------------------------------------------------

    # tag_selector() 함수 정의
    def tag_selector(self, comment_token : list) -> list:
        """
        형태소 분석의 결과가 담긴 리스트를 입력 받아 필요한 품사만 선택하는 함수입니다.\n
        특정 품사에 해당하는 형태소 목록만 담긴 리스트(List)를 반환합니다.
        """

        # 선택된 품사를 담은 딕셔너리 selected_tag_dict 초기화
        selected_tag_dict = {"NNG": "일반명사", "NNP": "고유명사"}

        # Mecab 형태소 분석기를 tokenizer 변수에 할당
        tokenizer = Mecab()

        # pos() 메서드를 사용해 품사 태깅 작업을 수행한 결과를 pos_token에 할당
        pos_token = tokenizer.pos(" ".join(comment_token))

        # 리스트 컴프리헨션(List Comprehension)을 사용해 선택된 품사에 해당하는 형태소만 selected_token에 할당
        selected_token = [token[0] for token in pos_token if token[1] in selected_tag_dict.keys()]

        # 결과 값 반환
        return selected_token

    # ----------------------------------------------------------------------------------------------------

    # stopwords_remover() 함수 정의
    def stopwords_remover(self, selected_token : list) -> Union[None, str]:
        """
        형태소 분석의 결과가 담긴 리스트를 입력 받아 불용어를 제거하는 함수입니다.\n
        불용어 목록을 불러와 불용어를 제거하고 리스트를 문자열로 병합해 반환합니다.\n
        단어가 5개 미만인 댓글의 경우 None 값을 반환합니다.
        """

        # 불용어 목록에 포함되지 않는 단어만 리스트 컴프리헨션(List Comprehension)으로 반환
        preprocessed_token = [token for token in selected_token if token not in self.stopwords]

        # join() 메서드를 사용해 각 단어 토큰을 하나의 문자열로 병합
        preprocessed_text = " ".join(preprocessed_token)

        # for 반복문 및 replace() 메서드를 사용해 잘못된 띄어쓰기를 수정
        for typo in self.typos:
            preprocessed_text = preprocessed_text.replace(typo.split(" / ")[0], typo.split(" / ")[1])

        # 단어 수가 5개 미만인 댓글인 경우를 제거
        if len(preprocessed_text.split()) < 5:
            return None

        # 결과 값 반환
        return preprocessed_text

    # ----------------------------------------------------------------------------------------------------

    # csv_exporter() 함수 정의
    def csv_exporter(self, result_df : pd.DataFrame, category : str):
        """
        전처리된 댓글이 담긴 데이터프레임을 CSV 파일로 저장하는 함수입니다.\n
        저장되는 CSV 파일의 이름은 'preprocessed_댓글 종류_comment.csv'입니다. (예) preprocessed_naver_news_comment.csv
        """

        # 네이버 뉴스 댓글인 경우 "preprocessed_naver_news_comment.csv" 파일로 저장
        if category == "naver":
            result_df.to_csv(EXPORT_DIR + f"preprocessed_{category}_news_comment.csv", index = False, encoding = "utf-8-sig")

        # 유튜브 댓글인 경우 "preprocessed_youtube_comment.csv" 파일로 저장
        else:
            result_df.to_csv(EXPORT_DIR + f"preprocessed_{category}_comment.csv", index = False, encoding = "utf-8-sig")

# ----------------------------------------------------------------------------------------------------

# 해당 파일을 직접 실행하는 경우
if __name__ == "__main__":

    # fit() 메서드를 사용해 전처리된 네이버 뉴스 댓글 내용을 담은 CSV 파일을 생성
    naver_comment_preprocessor = CommentPreprocessor()
    naver_comment_preprocessor.fit()

    # fit() 메서드를 사용해 전처리된 유튜브 댓글 내용을 담은 CSV 파일을 생성
    youtube_comment_preprocessor = CommentPreprocessor("youtube")
    youtube_comment_preprocessor.fit()