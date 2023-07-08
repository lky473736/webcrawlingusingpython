slist = ['삼성전자', '카카오', '네이버', '신풍제약']

w = open ('textfile.txt', 'w')

for i in slist :
    w.write (i)
    w.write ('\n')

w.close()