# 네이버 로그인 CAPTCHA 우회하기 
# 네이버는 selenium을 막기 위해 자동화 봇을 많이 설정해놓음 -> selenium 안 들키게 해야함
# sol 1) 복사 붙여넣기 이용 (send_keys로 그냥 입력하게 하는게 아니라 어떤 문자를 ctrl+v해서 입력하게 하기) -> 뚫리다가 안뚫리다가 함
# sol 2) 실제 브라우저처럼 꾸미기 (chromedriver는 좀 불안정해서 네이버가 그걸 알아차리지 않게 드라이버를 꾸미면 됨)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import time

import pyperclip # 복붙 가능하게 하는 라이브러리

# 옵션 여러개 쓸 때, 굳이 옵션 하나하나 따로 설정해서 할 필요 없음 -> 그냥 add_argument 계속 해도 됨
'''# 첫 번째 옵션 (selenium 중간에 안꺼지게 함)
option1 = webdriver.ChromeOptions()
option1.add_experimental_option("detach", True)

# 두 번째 옵션
# add_argument로 평소에 크롬 브라우저에서 썼던 사용자 정보처럼 꾸미기
# -> option.add_argument(r'user-data-dir=크롬 프로필 경로')
option2 = webdriver.ChromeOptions()
option2.add_argument("user-data-dir=/Users/alphastation/Library/Application Support/Google/Chrome/Default")''' 

soption = webdriver.ChromeOptions() # 옵션은 바로 위에 설명 있음
soption.add_argument(r"user-data-dir=/Users/alphastation/Library/Application Support/Google/Chrome/Default")  
soption.add_experimental_option("detach", True) 

# WebDriver 생성
driver = webdriver.Chrome(options=soption)

try:
    # 페이지 열기 (모바일 전용 페이지가 컴퓨터 전용 페이지보다 selenium 적용하기 쉬움)
    driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/')
    
    time.sleep(2)
    
    '''inputid = driver.find_element(By.ID, 'id')
    inputid.send_keys('username') # 글자 입력
    inputid.send_keys(Keys.ENTER) # 엔터
    
    time.sleep(2)
    
    inputpw = driver.find_element(By.ID, 'pw')
    inputpw.send_keys('password') # 글자 입력''' # 이렇게 하면 네이버가 알아챔 -> 복사 붙여넣기 방법으로 전환 (pyperclip 이용)
    
    pyperclip.copy('username') # 아이디 복사
    inputid = driver.find_element(By.ID, 'id')
    time.sleep(1)
    inputid.send_keys(Keys.CONTROL, 'v') # 컨트롤 키 누른 상태로 v 키보드에 누르기 (시스템 안에서)
    
    time.sleep(1)
    
    pyperclip.copy('password') # 비밀번호 복사
    inputpw = driver.find_element(By.ID, 'pw')
    time.sleep(1)
    inputpw.send_keys(Keys.CONTROL, 'v') # 컨트롤 키 누른 상태로 v 키보드에 누르기 (시스템 안에서)

    time.sleep(1)
    
    inputpw.send_keys(Keys.ENTER)
    
    
    # 프로그램이 종료되지 않도록 대기
    input("프로그램을 종료하려면 엔터 키를 누르세요...")

except Exception as e:
    print("오류 발생:", e)

finally:
    # WebDriver 종료
    driver.quit()