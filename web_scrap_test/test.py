import requests

#요청할 URL
url = 'https://news.naver.com/section/104'

#GET 요청 보내기
response = requests.get(url)

#응답 상태 코드 확인 (200은 성공을 의미)
print(response.status_code) # 200

# 응답의 HTML 내용 출력
print(response.text)