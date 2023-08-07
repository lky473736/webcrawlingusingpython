import requests
from bs4 import BeautifulSoup

data = requests.get ("https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=31&query=%EC%8B%9C%EB%82%98%EB%AA%A8%EB%A1%A4&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22shopping_top%22%7D%2C%22sub%22%3A%5B%7B%22name%22%3A%22shopping%22%7D%5D%7D%7D&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=61&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=02131102&fgn_region=&fgn_city=&lgl_lat=37.4407396&lgl_long=127.1261517&abt=&_callback=viewMoreContents") # 31~60번째 게시물 도착

soup = BeautifulSoup (data.text.replace('\\', ""), "html.parser")
print (soup) 
# class에 백슬래시가 들어가 있는 경우가 있음 (데이터 전송 과정 중에서 trivial data임) -> soup 과정 시에 data.text.replace ('\\', '') 적용

# 블로그 제목 수집하기

slist = soup.select("a.api_txt_lines")

for i in range (len(slist)) :
    print (str(i), " : ", slist[i].text)
    
print (slist[14].text)

# 블로그 제목에 맞는 주소 알고 싶을 때 -> 인덱싱 옆에 ['href']

print (slist[14]['href'])
