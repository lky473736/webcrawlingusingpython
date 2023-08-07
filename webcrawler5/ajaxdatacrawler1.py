# 웹페이지가 나누어져있을 때
# -> url 분석 시 page = ~ 형태를 이용하여 페이지마다 GET 요청

# 스크롤이 무한일 때 (구글, 네이버 블로그 ...)
# -> 그냥 GET하면 맨 처음 사이트 캡처본만 데이터화됨 
# -> network탭 이용 -> search로 특정 url 찾기 -> headers에서 GET 요청 url 찾아서 requests.get하기

import requests
from bs4 import BeautifulSoup

requests.get ("https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=31&query=%EC%8B%9C%EB%82%98%EB%AA%A8%EB%A1%A4&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22shopping_top%22%7D%2C%22sub%22%3A%5B%7B%22name%22%3A%22shopping%22%7D%5D%7D%7D&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=61&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=02131102&fgn_region=&fgn_city=&lgl_lat=37.4407396&lgl_long=127.1261517&abt=&_callback=viewMoreContents") # 31~60번째 게시물 도착

requests.get ("https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=61&query=%EC%8B%9C%EB%82%98%EB%AA%A8%EB%A1%A4&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22shopping_top%22%7D%2C%22sub%22%3A%5B%7B%22name%22%3A%22shopping%22%7D%5D%7D%7D&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=61&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=02131102&fgn_region=&fgn_city=&lgl_lat=37.4407396&lgl_long=127.1261517&abt=&_callback=viewMoreContents") # 61~90번째 게시물 도착

