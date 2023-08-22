# <페이지 이동과 이미지 수집>

# selenium이 꺼지는 현상을 방지하기 위해 option 추가하기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
import time
import urllib.request # image url 알고 있을때 쓰는 라이브러리

# SSL certificate error 방지 옵션
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.instagram.com')
time.sleep(2)

# 어떤 blank에 이것 좀 입력하라는 명령을 하고 싶을 때 : input 찾기
inputid = driver.find_element(By.NAME, 'username')
inputid.send_keys('username') # 글자 입력
inputid.send_keys(Keys.ENTER) # 엔터

inputpw = driver.find_element(By.NAME, 'password')
inputpw.send_keys('password') # 글자 입력
inputpw.send_keys(Keys.ENTER) # 엔터

loginbt = driver.find_element(By.CLASS_NAME, '_aj1-')
loginbt.send_keys(Keys.ENTER)

# 버튼을 클릭하고 싶으면
loginbt.click()

time.sleep(5)

# -----------------

# instagram의 사과 이미지 수집
# 1) 로그인
# 2) #사과 검색 페이지 이동
# 3) 첫 사진 클릭
# 4) 이미지 저장
# 5) 다음 누르고 이미지 저장
# 6) 5 반복

# 페이지 이동 : driver.get 사용
driver.get ('https://www.instagram.com/explore/tags/%EC%82%AC%EA%B3%BC/')
driver.implicitly_wait(10) # 찾는 요소가 없으면 알아서 n초 기다려라

# 첫 사진 클릭
firstpt = driver.find_element(By.CLASS_NAME, '_aagw')
firstpt.click()

# 이미지 저장 후 다음 누르고 또 저장 ~ 반복 -> <img src = ""> 찾기
driver.implicitly_wait(15)

num = int(input("사과 사진을 몇 개 이상 크롤링하시겠습니까? : "))

for l in range (num) :
    time.sleep(3)
    '''xh8yej3_list = driver.find_elements(By.CSS_SELECTOR, 'img.xh8yej3')
    time.sleep(5)
    
    # xh8yej3 클래스에 있는 사진들 중 진짜 뽑기
    urllist = []

    for i in xh8yej3_list :
        j = i.get_attribute('src')
        urllist.append (j)
        
    for k in urllist : 
        print (k) # 2번째가 진짜
    '''
        
    url = driver.find_elements(By.CSS_SELECTOR, 'img.xh8yej3')
    for i in url : 
        print (i.get_attribute('src'))   
        
    urllib.request.urlretrieve(url[l+1].get_attribute('src'), str(l+1) + '.jpg')
             
    '''time.sleep(5)
    urllib.request.urlretrieve(url, str(l + 1) + '.jpg')'''
    driver.find_element(By.CLASS_NAME, '_abl-').click() # 다음 버튼'

'''
driver.find_element_by_css_selector('.class명').click()
driver.find_element_by_css_selector('.class명').send_keys('codingapple_test')
driver.find_element_by_css_selector('.class명').send_keys(Keys.ENTER)  #엔터키입력'''

'''
find.element = 조건에 맞는 component 중 가장 첫번째 꺼 return
find.elements = 조건에 맞는 component 전부를 리스트로 return
'''