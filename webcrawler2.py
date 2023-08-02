import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/item/sise.nhn?code=005930'
data = requests.get ('https://finance.naver.com/item/sise.nhn?code=005930')

soup = BeautifulSoup (data.content, 'html.parser')

print (soup)


# 1) 데이터의 글자들이 해체되어 있는 경우 : 더 큰 범위에 있는 (에워싸는) class 확인해보기

soup_componentlist = soup.find_all('em', class_ = "no_down")

for i in soup_componentlist :
    print (i.text)
    
print ("*" * 10)
print ("해체된 주가 통합 결과 : ", soup_componentlist[0].text)


# 2) class, id가 하나도 없는 요소 : css selecter 사용
# 찾고 싶은 글자의 상위 태그 찾기 -> 상위 태그의 속성 찾기
# -> 상위 태그의 속성 찾아서 그 안에 있는 태그 찾아라라고 명령

soup.select ('.f_down') # class명이 f_down인 것을 찾아라
soup.select ('#tah') # id명이 tah인 것을 찾아라
soup.select ('strong#_nowVal') # 태그명이 strong이면서 id가 _nowVal인 것을 찾아라
soup.select ('strong.f_down') # 태그명이 strong이면서 class가 f_down인 것을 찾아라
soup.select ('strong') # 태그명이 strong인 것을 찾아라
soup.select ('.f_down em') # 띄어쓰기 : 내부요소 (class명이 f_down인 것 안에 em태그를 찾아라

print (soup.select ('.f_down em')[0].text)


# 3) 이미지 수집 : 그대로

img = soup.select ('img#img_chart_area')[0]
print (img['src']) # 주식 차트