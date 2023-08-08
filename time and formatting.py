# 자주 쓰는 시간 및 포맷팅 문법

import time 


# epoch 시간 출력
a = time.time() # epoch로 출력 (1970년부터 몇초가 흘렀는가)

10000 * 10000

b = time.time()

print(b - a) # 중간에 코드가 실행된 시간을 출력


# 현재 ctime 출력

epoch = time.time()
ctime = time.ctime(epoch) # 재할당
print (ctime)


# localtime()으로 세부 항목만 출력

localtime = time.localtime()
print (localtime)
print ("현재 연도는 " + str(localtime.tm_year))


# strftime()으로 시간표시형식 맘대로 바꾸기
# time.strftime ('formatting 문법', localtime)

strftime = time.strftime ('%Yyear %mmonth %dday', localtime)
print (strftime)


# 문자 formatting (문자 중간에 변수/문자넣기)

name = 'lim'
print (f"안녕하세요 {name}")
print ("안녕하세요 %s" %name)


# 시간 출력할 때 단순하게 하려면 datetime

import datetime

infor = datetime.datetime (2022, 10, 1)
print (infor)