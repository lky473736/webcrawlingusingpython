# epoch 형식의 시간 다루기 (UNIX 시간)
# dt에 시간 형식이 epoch일 때 
# -> 아래와 같이 하기

'''
import time
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch시간형식/1000)) 
'''

import requests
import json
import time

url = "https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?interval=1H&1691498315072"

data = requests.get(url)

dictionary = json.loads (data.content) # JSON -> dictionary

timelist = list()

for i in range (len(dictionary["body"]["candles"])) :
    timelist.append (dictionary["body"]["candles"][i]["dt"])
    
    realtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timelist[i]/1000)) 
    
    timelist[i] = realtime
    
print (timelist)