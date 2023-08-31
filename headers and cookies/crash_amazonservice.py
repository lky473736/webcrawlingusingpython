# python 크롤링을 막아보자 & 뚫어보자
# 아마존 쇼핑사이트는 크롤링 막아둠
# GET을 요청하면 request headers (접속정보)를 아마존에서 볼 수 있게 됨 (IP, user-agent, cookies..., position, language ...)
# -> 아마존이 user-agent를 딱 보고 수상한 첩자다 싶으면 막음

'''import requests
from bs4 import BeautifulSoup

url = r'https://www.amazon.com/s?k=potato+fries&crid=1HSQ3HUPCF4G3&sprefix=potatofries%2Caps%2C258&ref=nb_sb_noss_2'
data = requests.get(url)

print (data.content)

soup = BeautifulSoup(data.content, "html.parser")

print (data.status_code) # 4XX, 5XX 뜸 (GET이 제대로 안되었다는 뜻)
print (soup)'''

# 따라서 아마존 크롤링 방지 시스템을 부수거나 우회해야 함 (해킹 or user-agent 속이기)
# 1) headers 넣기
# 2) cookies 넣기

import requests
from bs4 import BeautifulSoup

cheating_headers = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

cheating_cookies = {'session-id' : '142-3447216-5688468', 
                    'session-id-time' : '2082787201l', 
                    'i18n-prefs' : 'USD',
                    'sp-cdn' : "L5Z9:KR",
                    'skin' : 'noskin',
                    'ubid-main' : '131-5611596-1851305', 
                    'session-token' : 'Nqt30q7UYQOSAg5eDyJzJquqpcUEg53WA8FZbxb2FilhyRLU4OEMU4Wi3sXEhB+W/Dt6Jhqsx5lck7JdEmUq6fQ1kC6UPYskv5BM3j/zEcn8svHmeiCF1+Ydi2gNhbJjn1sh+xMilRr3ldTtT/+jUN3I7v/VAnX+rHi4EksNa5lHBFo3psZld+z0h05ZVS3tyciFY+XAtM8aL7hXGXFtTkUOG+YT3CLsqQY19sM0zba9cjQUOkcHwUe5VJzx06gy3DUokTB4iMQuppdpQ1tUSyFL3Ct6xrLjj5QcWAg7SIKoiLXtGdI47wIKyOT9p4YcbFMVH7Dy2N7q1wYntBTP+K7StDB1Ndcf'}

url = r'https://www.amazon.com/s?k=potato+fries&crid=1HSQ3HUPCF4G3&sprefix=potatofries%2Caps%2C258&ref=nb_sb_noss_2'

data = requests.get (url, headers = cheating_headers, cookies = cheating_cookies) # GET할 때 cookies, headers 정상적인 걸로 갈아끼워서 정상적인 것처럼 속이기 -> 200 됨 (정상)

print (data.content)
print (data.status_code)

soup = BeautifulSoup (data.content, 'html.parser')

infor = soup.select(".a-size-medium")

if infor:
    print(infor)
else:
    print("Information not found.")


'''
try : 
   이거하다가

except : 
   에러나면 이거 하기
   '''