# hard-coding -> refactoring using loopstation

gugudan = open('textfile2.txt', 'w')

for k in range (10) :
    for j in range (10) :
        gugudan.write (str((k + 1) * (j + 1)))
        gugudan.write ("\n")
        
        # refactoring below
        # gugudan.write (str((k + 1), * (j + 1)) + '\n')

gugudan.close()

