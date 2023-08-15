# selenium 목적
# 단순반복, 웹업무 등 자동화
# 구조가 어려운 사이트 (인스타) 크롤링하기

from selenium import webdriver
import selenium.webdriver.common.keys  
import time

driver = webdriver.Chrome()

# error : selenium pip3로 패키지 다운하였으나 vscode에서 인식 안됨 -> 내일 jupyter로 실험
