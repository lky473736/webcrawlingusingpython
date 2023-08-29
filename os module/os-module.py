# os module 
# 대량의 파일을 손쉽게 처리하기 
# ex) 파일 백만개 rename, 파일 백만개 분류 ...

import os

# 1) 괄호 안에 있는 파일명 다 가져오기
slist = os.listdir("os module/test")

# 2) 파일명 변경 (괄호에 경로 포함 파일명, 새로 바꿀 경로 포함 파일명)
for i in range (len(slist)) :
    os.rename('os module/test/test' + str(i + 1) + '.txt', 'os module/test/test' + str(i + 1) + '_new' + '.txt')

# 3) 파일 복사
import shutil

# shutil.copy (1, 2) -> 경로 1에 있는 파일이 경로 2로 복사
# shutil.copy('os module/test', 'os module/test_copied') -> 안됨 (디렉토리 전체를 옮기는 건 안되고 파일 형태로만 하나하나 옮길 수 있음)

for i in range (len(slist)) :
    shutil.copy (f'os module/test/test{i + 1}_new.txt', 'os module/test_copied')
    
    # 중간에 불리언 표현으로 조건식 넣으면 파일 분류 가능
    if '.txt' in os.listdir("os module/test_copied")[i] :
        print ('txt 파일이다')

# 경로 합치기
os.path.join('경로', '경로2') # -> ~~~/경로/경로2

os.getcwd() # 현재 파이썬 경로 알려주기