# 회사 코드를 입력만 하면 그 회사의 주식 현재가를 알려주는 프로그램

import requests
from bs4 import BeautifulSoup

def crawler_currentprice (code) :
    url = "https://finance.naver.com/item/sise.nhn?code=" + code
    # 포맷팅하여 글자 중간에 변수를 넣으려면 f'글자{변수}글자'
    # url = f"https://finance.naver.com/item/sise.nhn?code={code}"
    data = requests.get (url)
    soup = BeautifulSoup(data.content, 'html.parser')
    
    currentprice = soup.find_all ('em', class_="no_down")[0].text
    
    return currentprice

while True : 
   askcode = input("회사 코드를 입력 (1 입력 시 종료) : ")
   
   if askcode == 1 :
       quit()
       
   print ("현재가 : ", crawler_currentprice(askcode))
   
