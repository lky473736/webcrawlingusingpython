# requests를 이용하여 GET 요청과 함께 COVID-19 실시간 상황 크롤링하기 (time 사용)

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
# 처음 불러오는 html에서는 0으로 뜸 -> 무한스크롤