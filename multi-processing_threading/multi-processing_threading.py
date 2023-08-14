import requests
import json
import time

from multiprocessing.dummy import Pool as ThreadPool

# multiprocessing : multi-processing 가능한 라이브러리
# multiprocessing.dummy : multi-threading까지 가능한 라이브러리 

urllist = [
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000'
]

'''datalist = []

for i in url : 
    data = requests.get (i)
    datalist.append (data)
    
inforlist = []

for i in datalist :
    dict = json.loads(i.content)
    infor = dict['data'][0]['Close']
    inforlist.append (infor)
    
print (inforlist)''' # <--- 이런거는 일일히 하나씩 작업하는 거라서 컴퓨터 시간이 오래 걸림

# 따라서 병렬 작업 시키기 위해선 multi-processing_threading 필요 (파이썬 창을 동시에 띄우는 작업)

# multi-processing : 여러 프롬프트 (실행창) 띄우기
# multi-threading : cpu 병렬 처리

def crawler(url) :
  data = requests.get(url)
  dict = json.loads(data.content)
  return dict['data'][0]['Close']

pool = ThreadPool (4) # ThreadPool (n) : n = 프로세스 띄울 창 수

result = list(pool.map(crawler, urllist)) # 프로세스 진행 시킬 함수 작성

print (result)

# map(함수, 리스트) : 모든 리스트 component에 함수 적용하기 -> 적용된 component로 바꾸기

pool.close() # 프로세스 종료하기
pool.join() # 프로세스 결과 기다리기