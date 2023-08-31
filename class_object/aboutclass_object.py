# class, object 이해하기

class classmachine : 
    def __init__ (self) : 
        pass
    
    def choose_f (self, dictionary, key) :
        if isinstance (dictionary, dict) == True :
            print (dictionary[key])
        
        else : 
            exit()
    
    def change_f (self, dictionary, key, wannachange) : 
        if isinstance (dictionary, dict) == True : 
            dictionary[key] = wannachange
            print (dictionary)
            
        else :
            exit()
        

signal = {'1' : 'only-direction', '2' : 'double-direction', '3' : 'all direction'}

model = {'1' : 'learning machine', '2' : 'unlearning machine', '3' : 'reinforcement learning'}

nondictionary = False

sobject = classmachine()
sobject.choose_f (signal, '1')
sobject.change_f (model, '2', 'changed')

'''
1) object 만들기 == class 먼저 만들어야 함
2) init의 용도 == 초기값 설정 (self는 새로 생성될 object를 뜻함 == instance)
'''