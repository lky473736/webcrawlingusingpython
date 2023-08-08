# 이더리움의 시간 당 가격 수집하기 (차트)
# -> 차트 가격정보가 html 안에 없음
# -> network 탭에 있는 모든 데이터파일에서 찾기
# -> requests.get

import requests
from bs4 import BeautifulSoup

import json

url = "https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?interval=1H&1691498315072"

data = requests.get(url)

# 자료형이 {'' : ''}이라면 딕셔너리
# 자료형이 {"" : ""}이라면 JSON (웹상에서의 딕셔너리, 글자취급받음)
# JSON -> dictionary하기 위해서 import json 과정 필요

dictionary = json.loads (data.content) # JSON -> dictionary

print (dictionary)

# 복잡한 JSON 다루기 -> data.json에 복붙하여서 format document -> 집합관계 따져서 data 뽑기

print (dictionary["body"]["candles"][0]["close"])

# 전체 이더리움 값에서 시간당 클로즈 포지션 추출하기

closepositionlist = list()

for i in range (len(dictionary["body"]["candles"])) :
    closepositionlist.append (dictionary["body"]["candles"][i]["close"])
    
    closepositionlist[i] = float(closepositionlist[i])
    
print (closepositionlist)