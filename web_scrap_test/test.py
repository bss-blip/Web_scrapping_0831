import requests
from bs4 import BeautifulSoup

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

print("== 헤드라인 뉴스 타이틀 출력 ==")
for idx, news_title in enumerate(news_tit_el):
  no = idx + 1
  print(f"{no} : {news_title.get_text()}")
print("== 헤드라인 뉴스 타이틀 출력 끝 ==")  

# 검색 키워드 추출 시작
search_keyword = "폭염" # 키워드
keyword_news_list = []
for title in news_tit_el:
  if search_keyword in title.get_text():    
    keyword_news_list.append(title.get_text())
# 검색 키워드 추출 끝

# 검색 내용 출력    
print("== 검색 내용 출력 ==")  
for idx, news_title in enumerate(keyword_news_list):
  no = idx + 1
  print(f"{no} : {news_title}")
  