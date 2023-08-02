import requests
from bs4 import BeautifulSoup

file = open ("/Users/alphastation/Desktop/repository/webscrapingusingpython/webcrawler4 (homework)/homework.txt", 'w')

def crawler_currentprice (code) :
    url = "https://finance.naver.com/item/sise.nhn?code=" + code
    # 포맷팅하여 글자 중간에 변수를 넣으려면 f'글자{변수}글자'
    # url = f"https://finance.naver.com/item/sise.nhn?code={code}"
    data = requests.get (url)
    soup = BeautifulSoup(data.content, 'html.parser')
    
    currentprice = soup.find_all ('em', class_="no_down")[0].text
    
    return currentprice

codelist = ['005930', '066575', '005380', '035720', '034220', '003490']

for i in range (len(codelist)) :
    file.write(crawler_currentprice(codelist[i]) + '\n')

file.close()