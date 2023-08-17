'''# requests를 이용하여 GET 요청과 함께 COVID-19 실시간 상황 크롤링하기 (time 사용)

import requests
from bs4 import *

url = "https://coronaboard.kr/"
data = requests.get (url)
cleandata = BeautifulSoup (data.content, "html.parser")

classposition_list = ["confirmed number", "death red number", "released number"]

def crawler (classposition) : 
    infor = cleandata.find_all ("p", class_ = classposition)[0].text
    
    return infor

for i in classposition_list :
    print (crawler(i))
        
# 사이트 GET 시에 수치가 들어옴
# 처음 불러오는 html에서는 0으로 뜸 -> 무한스크롤'''

# 이제 selenium으로 가능함

from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()

driver.get ('https://coronaboard.kr/')

# 공백은 마침표로 대체
infor1 = driver.find_element (By.CSS_SELECTOR, ".confirmed.number").text
infor2 = driver.find_element (By.CSS_SELECTOR, ".death.red.number").text
infor3 = driver.find_element (By.CSS_SELECTOR, ".released.number").text

slist = []

slist.append (infor1)
slist.append (infor2)
slist.append (infor3)
    
print (slist)