file = open('textfile3.txt', 'w')

for i in range (9) :
    for j in range (9) :
        file.write (str(i + 1) + '*' + str(j + 1) + '==' + str((i + 1) * (j + 1)) + '\n')
        
file.close()