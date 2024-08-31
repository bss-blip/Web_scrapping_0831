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
      <a class="menu-item-text" href="https://www.naver.com">네이버로 이동</a>
    </li>
    <li>
      <a class="menu-item-text" href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a class="menu-item-text" href="https://www.daum.net">다음으로 이동</a>
    </li>
    <ul>
</nav>       
"""
#HTML 파싱
bs = BeautifulSoup(html, 'html.parser')

# print(bs.select_one('.menu-item-text')) ->클래스가 "menu-item-text" 인 녀석을 선텍
#print(bs.select_one('.menu-item-text')) ->"menu-item-text" классы бар бирин тандаңыз

# print(bs.select_one('.menu-item-text')) ->id가 "menu-item-text" 인 녀석을 선텍

# find, find_all
# find : 조건과 일치하는 모든 요소중에 검색 된 첫번째 요소를 반환
# Шартка дал келген бардык элементтердин арасынан табылган биринчи элементти кайтарат.
print(bs.find('a', class_='menu-item-text'))

# find_all : 조건과 일치하는 모든 요소의 리스트를 반환
# find_all: Шартка дал келген бардык элементтердин тизмесин кайтарат
print(bs.find_all('a', class_='menu-item-text'))

menu_item_text = bs.find_all('a', class_='menu-item-text')

for idx, el in enumerate(menu_item_text):
  no =idx + 1
  print(f"{no} : {el.get_text()}")
  
print(bs.find(id="menu-box"))  
print(bs.find('nav', attrs={id : "menu-box"}))   
 


'''
#응답 상태 코드 확인 (200은 성공을 의미(Жооптун абалын текшерүү коду (200 ийгиликти билдирет)
print(response.status_code) # 200
# 응답의 HTML 내용 출력 (Жооптун HTML мазмунун басып чыгаруу)
print(response.text)
'''