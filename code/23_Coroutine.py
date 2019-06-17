#Coroutines

#Consumer Function
'''
def Consumer():
    try:
        while True:
            val= (yield)
            print(val,',',val**3)
    except GeneratorExit:
        print("===Consumer Closed Coroutine===")

def Filter():
    try:
        while True:
            val,coroutine = (yield)
            if val%2==0:
                coroutine.send(val)
                #print(val)
    except GeneratorExit:
        print("===Filter Closed Coroutine===")    
                
#Producer Function
def Produce(n,coroutine,consume):
    for i in range(n):
        coroutine.send((i,consume))
    
    coroutine.close()
        

consume = Consumer()
filt = Filter()
consume.__next__()
filt.__next__()

Produce(10,filt,consume)
'''


def Consume(statement):
    try:
        while True:
            pattern = (yield)
            for word in statement.split():
                if word.endswith(pattern):
                    print(word)
    except:
        print("===Closed Coroutine===") 

    
stmt = '''consumer producer comming going running playing 
finding discussing, junping entertainer'''

cor1 = Consume(stmt)
cor1.__next__()

cor1.send('ing')
cor1.send('er')
cor1.close()




def Consume(pattern):
    try:
        while True:
            statement = (yield)
            for word in statement.split():
                if word.endswith(pattern):
                    print(word)
    except:
        print("===Closed Coroutine===") 



stmt = '''consumer producer comming going running playing 
finding discussing, junping entertainer'''


cor_for_ing = Consume('ing')
cor_for_er = Consume('er')
cor_for_ing.__next__()
cor_for_er.__next__()
cor_for_ing.close()
cor_for_er.close()




#ContextManager and Metaclasses






