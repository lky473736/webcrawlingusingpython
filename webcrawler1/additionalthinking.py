import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/item/sise.nhn?code=005930'
data = requests.get ('https://finance.naver.com/item/sise.nhn?code=005930')

soup = BeautifulSoup (data.content, 'html.parser')


# id uniquancy

print (soup.find_all('span', id="_quant"))
print (soup.find_all('span', id="_quant")[0].text)


# class로 찾을 때엔 class_= ~~~

print (soup.find_all('span', class_="tah")[5].text)
