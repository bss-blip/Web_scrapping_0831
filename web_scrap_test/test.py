import requests
from bs4 import BeautifulSoup

#요청할 URL (Сурам үчүн #URL)
url = 'https://news.naver.com/section/104'

#GET 요청 보내기 (GET өтүнүчүн жөнөтүү)
response = requests.get(url)

html = """
<nav class="menu-box-1" id="menu-box">
  <ul>
    <li>
      <a class="never" href="https://www.naver.com">네이버로 이동</a>
    </li>
    <li>
      <a class="google" href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a class="daum" href="https://www.daum.net">다음으로 이동</a>
    </li>
  <ul>
</nav>       
"""
#HTML 파싱
bs = BeautifulSoup(html, 'html.parser')

# select, select_one: 내그, 클래스, id로 HTML을 검색
#bs.select('a') :html 상에 있는 모든 'a' 엘리민드를 검색(a m.n gana chigat)
#print(bs.select('a'))
#print(bs.select_one('.naver'))
 #print(bs)
 
a_tags = bs. select('a')
for a_tag in a_tags:
  print(a_tag.get_text())


'''
#응답 상태 코드 확인 (200은 성공을 의미(Жооптун абалын текшерүү коду (200 ийгиликти билдирет)
print(response.status_code) # 200
# 응답의 HTML 내용 출력 (Жооптун HTML мазмунун басып чыгаруу)
print(response.text)
'''