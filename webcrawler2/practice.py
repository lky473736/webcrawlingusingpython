# 삼성전자, LG전자의 현재주가 비교 프로그램

import requests
from bs4 import BeautifulSoup

url1 = "https://finance.naver.com/item/main.naver?code=005930"
url2 = "https://finance.naver.com/item/main.naver?code=066570"

data1 = requests.get (url1)
data2 = requests.get (url2)

print ("삼성전자 주가 크롤러 작동 코드 : ", data1.status_code)
print ("LG전자 주가 크롤러 작동 코드 : ", data2.status_code)

soup1 = BeautifulSoup (data1.content, 'html.parser')
soup2 = BeautifulSoup (data2.content, 'html.parser')

now1 = soup1.find_all ('em', class_="no_down")[0].text
now2 = soup2.find_all ('em', class_="no_down")[0].text

print ("*" * 10)
print ("현재 삼성전자의 주가 : ", now1)
print ("현재 LG전자의 주가 : ", now2)
