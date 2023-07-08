import re # regular expression 사용 선언

# re.search() : 매개 변수를 문자열 내에서 검색하는 함수
# re.findall() : 정해진 패턴을 만족하면 그것을 return

hand = open('mbox-short.txt')

for line in hand : 
    line = line.rstrip()
    if re.search('^X.*:', line) : 
        print (line)
        
    else : 
        print ("no")
        exit()
        
# ^ : 한 줄의 시작
# . : 아무 문자와도 매칭
# *\