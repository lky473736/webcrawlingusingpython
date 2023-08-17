# https://scribblinganything.tistory.com/100
# https://aplab.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%82%AC%EC%9A%A9%EB%B2%95-%ED%8A%B9%EC%A0%95-%EC%9A%94%EC%86%8C%EB%A5%BC-%EC%84%A0%ED%83%9D%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%80

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.instagram.com')
time.sleep(5)

# 입력 필드에 입력한 값을 가져오기 위해 .get_attribute('value')를 사용
username = driver.find_element(By.NAME, 'username')
print('Username:', username)

aria_label_value = driver.find_element(By.CSS_SELECTOR, '._ac4d') # 인풋
print('Input:', aria_label_value)

driver.quit()