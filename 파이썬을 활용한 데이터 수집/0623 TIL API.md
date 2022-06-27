# 0623 TIL

- 웹 스크래핑 기초
- API 불러오기
  - import requests

```python
import requests

URL = 'https://finance.naver.com/site/'

response = requests.get(URL).text
print(response) # 
```

- BeautifulSoup4
  - HTML과 XML 파일들의 데이터를 가져오는 파이썬 라이브러리
  - pip install beautifulsoup4
  - from bs4 import BeautifulSoup4 (Quick Start)
- 선택자 활용
  - 우클릭 > 검사 > 소스코드 우클릭 > Copy > copy selector (#KOSPI_now)

```python
# 위에 소스코드 이어서
data = BeautifulSoup(response, 'html.parser')
print(data) # response와 결과 똑같음
print(type(data), type(response)) # 뷰티풀숩, str (다름)

# 선택자
data.select_one('#KOSPI_now') # 뷰티풀숩 공식문서에서 selector 검색
print(kospi.text)
```



