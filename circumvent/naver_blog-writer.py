# 네이버 블로그 자동 글발행 봇 개발 (셀레니움 연습)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import time

import pyperclip # 복붙 가능하게 하는 라이브러리

soption = webdriver.ChromeOptions() # 옵션은 바로 위에 설명 있음
soption.add_argument(r"user-data-dir=/Users/alphastation/Library/Application Support/Google/Chrome/Default")  
soption.add_argument('--no-sandbox')
soption.add_argument('--disable-dev-shm-usage')
soption.add_experimental_option("detach", True) 

# WebDriver 생성
driver = webdriver.Chrome(options=soption)

try:
    # 페이지 열기 (모바일 전용 페이지가 컴퓨터 전용 페이지보다 selenium 적용하기 쉬움)
    driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/')
    
    time.sleep(2)
    
    # pyperclip이 붙여넣기 하려고 할 때 커서가 웹페이지로 향해 있어야 얘가 작동하는 것 같음 (그니까 pyperclip 하기 전에 웹페이지 어디든 한번 눌러줘야 한다는 것임 그래야 커서가 웹으로 향하니깐)
    readyclick_for_copypaste = driver.find_element (By.ID, 'find_wrap_KR')
    readyclick_for_copypaste.click()
    time.sleep(1)
    
    # pyperclip을 쓸 때 .copy('문자열')은 작동 안됨. 항상 .copy(변수)로 하고 앞에 변수(복붙하고 싶은 문자열로) 선언해주기
    username = 'username' 
    pyperclip.copy(username) # 아이디 복사 
    inputid = driver.find_element(By.ID, 'id')
    time.sleep(1)
    inputid.send_keys(Keys.COMMAND, 'v') # 컨트롤 키 누른 상태로 v 키보드에 누르기 (시스템 안에서) - 맥은 커맨드겠지?
    
    time.sleep(1)
    
    password = 'password'
    pyperclip.copy(password) # 비밀번호 복사
    inputpw = driver.find_element(By.ID, 'pw')
    time.sleep(1)
    inputpw.send_keys(Keys.COMMAND, 'v') # 컨트롤 키 누른 상태로 v 키보드에 누르기 (시스템 안에서)

    time.sleep(1)
    
    inputpw.send_keys(Keys.ENTER)
    
    # 로그인 성공 후 네이버 블로그 글 발행 버튼 찾기
    # 블로그 버튼 찾아서 접속
    time.sleep(1)
    appbuttons = driver.find_elements(By.CSS_SELECTOR, '.sa_t')
    
    '''appbuttons_urllist = []
    
    for i in appbuttons :
        appbuttons_urllist.append (str(i.get_attribute('href')))'''
        
    print (appbuttons)
    appbuttons[2].click() # blogbutton.click()
    
    # 네이버 블로그 접속 후에 글 발행 버튼 찾기
    time.sleep(1)
    mymenubutton = driver.find_element(By.CSS_SELECTOR, '.icon_my_menu__RkEHg')
    mymenubutton.click()
    
    time.sleep(1)
    functionbuttons = driver.find_elements(By.CLASS_NAME, 'icon___T7KP')
    print (functionbuttons)
    functionbuttons[5].click()
    
    # 글 발행
    time.sleep(1)
    inputs = driver.find_elements(By.CSS_SELECTOR, '.se_textarea')
    print (inputs)
    
    time.sleep(2)
    titleinput = inputs[0]
    titleinput.send_keys('test using selenium')
    
    time.sleep(2)
    contentinput = driver.find_element(By.CSS_SELECTOR, '.is-empty')
    contentinput.send_keys('test using selenium : it works')
    
    time.sleep(2)
    applybutton = driver.find_element(By.CLASS_NAME, 'btn_applyPost')
    applybutton.send_keys(Keys.ENTER)
    
    # 성공 (https://m.blog.naver.com/jimmysteven/223194989085?afterWebWrite=true)
    
    # 프로그램이 종료되지 않도록 대기
    input("프로그램을 종료하려면 엔터 키를 누르세요...")

except Exception as e:
    print("오류 발생:", e)

finally:
    # WebDriver 종료
    driver.quit()