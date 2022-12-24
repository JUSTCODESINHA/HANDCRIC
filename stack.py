stack = []
top = None

def isEmpty(stk):
    if(stk == []):
        return True
    else:
        return False


def PUSH(stk,item):
    stk.append(item)
    top = len(stk) - 1


def POP(stk):
    if(isEmpty(stk)):
        return("UnderFlow !")
    else:
        pop_ele = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = top - 1
    return pop_ele



def PEEK(stk):
    if isEmpty(stk):
        return("Underflow !")
    
    else:
        top = len(stk) - 1
        return stk[top]

def DISPLAY(stk):
    if isEmpty(stk):
        print("STACK IS EMPTY !")
    
    else:
        top = len(stk) - 1
        print(stk[top],"<---top")

        for i in range(top-1,-1,-1):
            print(stk[i])
    



#stack implementations 

while True:
    print('STACK IMPLEMENTATON !')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display')
    print('5. Exit')

    
    OPR = input("ENTER THE TYPE OF OPERATION :")
    
    if OPR == '1':
        ENTRY = input("ENTER THE ELEMENT => ")
        PUSH(stack,ENTRY)

    if OPR == '2':
        POP(stack)

    if OPR == '3':
        PEEK(stack)

    if OPR == '4':
        DISPLAY(stack)

    if OPR == '5':
        exit()

    