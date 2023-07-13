import requests # 웹사이트 접속
from bs4 import BeautifulSoup # html 웹문서 분석

# 파이썬으로 데이터 들어있는 웹사이트 접속 (html 도착)
# -> html 속에서 필요한 정보 뽑기

url = 'https://finance.naver.com/item/sise.nhn?code=005930' # <- 삼성전자
data = requests.get (url)

print (data) # data 통신이 잘 되는가
print (data.content) # data의 전체 html 데이터 출력 (한글 깨져서 나옴 -> 따라서 bs4에 잠깐 넣었다가 빼면 됨)
print (data.status_code) # 200 : 정상 / 400 or 500 : 차단당함

cleandata = BeautifulSoup (data.content, 'html.parser')
# html 깨짐 개선 -> 개선된 data == soup 
# 이때 soup는 .content로써 html 파일임

print (cleandata)

# class와 id를 찾아 컴퓨터에게 그것들을 지표로 시켜 크롤링 시킴
# ~~~~.find_all('태그명', 속성명) : 태그명과 속성명이 일치하는 data들을 list 형태로 보여줌
# 속성 : class 또는 id 이름

print (cleandata.find_all('strong', id="_nowVal"))
# [<strong class="tah p11" id="_nowVal">71,900</strong>]

print (cleandata.find_all('strong', id="_nowVal")[0])
# <strong class="tah p11" id="_nowVal">71,900</strong>

print (cleandata.find_all('strong', id="_nowVal")[0].text)
# 71,900