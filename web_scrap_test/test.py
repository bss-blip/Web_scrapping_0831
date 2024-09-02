import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

# 요청할 URL
url = 'https://news.naver.com/section/103'
# GET 요청 보내기
resp = requests.get(url)
# 응답 상태 코드 확인 (200은 성공을 의미)
result_status = resp.status_code
if result_status == 200:
  # HTML 파싱
  bs = BeautifulSoup(resp.text, 'html.parser')

news_tit_el = bs.select('.sa_text_strong')

news_title_list = [] # 전체 뉴스 제목 저장소
print("== 헤드라인 뉴스 타이틀 출력 ==")
for idx, news_title in enumerate(news_tit_el):
  no = idx + 1
  print(f"{no} : {news_title.get_text()}")
  news_title_list.append(news_title.get_text())
print("== 헤드라인 뉴스 타이틀 출력 끝 ==")  

# 검색 키워드 추출 시작
search_keyword = "폭염"     # 키워드
keyword_news_list = []        # 키워드로 출력한 뉴스 기사 제목 저장소
for title in news_tit_el:
  if search_keyword in title.get_text():    
    keyword_news_list.append(title.get_text())
# 검색 키워드 추출 끝
    
# 검색 내용 출력    
print("== 검색 내용 출력 ==")  
for idx, news_title in enumerate(keyword_news_list):
  no = idx + 1
  print(f"{no} : {news_title}")
  

# 저장할 데이터
data = {
  '전체 뉴스 제목' : news_title_list,    
}

data2 = {
  '키워드 뉴스 제목' : keyword_news_list,    
}

# 추출한 데이터를 엑셀에 저장
df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

# 엑셀 파일로 저장
df.to_excel('C:\work\python_projects\뉴스_기사.xlsx', index=False) 
df2.to_excel('C:\work\python_projects\뉴스_기사2.xlsx', index=False)