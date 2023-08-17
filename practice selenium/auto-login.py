# selenium이 꺼지는 현상을 방지하기 위해 option 추가하기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
import time

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

bt = driver.find_element(By.CLASS_NAME, '_aj1-')
bt.send_keys(Keys.ENTER)

# 버튼을 클릭하고 싶으면
bt.click()

'''
driver.find_element_by_css_selector('.class명').click()
driver.find_element_by_css_selector('.class명').send_keys('codingapple_test')
driver.find_element_by_css_selector('.class명').send_keys(Keys.ENTER)  #엔터키입력'''