w = open ('textfile.txt', 'w') # 이미 textfile.txt가 있으면 덮어쓰기 됨

w.write ('삼성전자\n')
w.write ('카카오\n')
w.write ('네이버\n')
w.write ('신풍제약')

w.close() # closing : 버그 방지


a = open ('textfile.txt', 'a') # mode a : append (추가)
# 기존 파일이 있을 경우 append됨 (덮어쓰기 x)
a.write ('\n셀트리온')

a.close()


r = open ('textfile.txt', 'r')

print(r.read())

r.close()


# 참고 : mode wb : binary형으로 오픈 (이미지 파일)