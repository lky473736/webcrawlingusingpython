# selenium 목적 :
# 1) 단순반복, 웹업무 등 자동화
# 2) 구조가 어려운 사이트 (인스타) 크롤링하기

# 인스타그램 자동 로그인 / 데이터 크롤링하기

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# url 적으면 파이썬으로 접속
driver.get('https://instagram.com')

# 글자나 component가 아직 사이트에서 뜨지 않았는데 가져오는거는 불가능 -> 따라서 time으로 로딩시간 다 맞춰서 해줘야함 (어떤 글자 뜨고 난 다음에 크롤링)
# 잠깐 코드 실행 정지 (로딩시간)
time.sleep(5)

# 아래처럼 쓰면 안됨 (selenium 3에서만 가능)
'''# css selector로 element 가져오기 (안에 클래스 또는 id)
infor = driver.find_element_by_class_name('ab25')
# 클래스 : .


driver.find_element_by_css_selector('.class명')
driver.find_element_by_css_selector('#id명')
driver.find_element_by_css_selector('태그명[속성이름="속성명"]')
'''

# https://velog.io/@thovy/selenium-AttributeError-Webdriver-object-has-no-attribute-findelementbyid <-- selenium 4부터는 find_element("***", "&&&") 형식으로 작성
# arkjh7764.tistory.com/141 <-- 문법

infor = driver.find_element (By.CSS_SELECTOR, "._ab25").text

print (infor)

# 클래스명이 두 블록 이상의 띄어쓰기로 되어있을 때 : 다양한 클래스가 중첩된 것 -> 그럴때는 맨 마지막 하나만 element