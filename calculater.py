def ADDISTION(x,y):
    return x+y

def SUBTRACTION(x,y):
    return x-y

def MULTIPLYCATION(x,y):
    return x*y

def DIVISION(x,y):
    return x/y

n1=int(input('enter number1:'))
n2=int(input('enter number2:'))

while(1):
    print('1.ADDISTION')
    print('2.SUBTRACTION')
    print('3.MULTIPLYCATION')
    print('4.DIVISION')
    print('0.STOP')
    print('=@=@=@=@=@=@')
    ch=input('enter your choice (0+04):')
    if ch=='1':
        print(ADDISTION(n1,n2))
    elif ch=='2':
        print(SUBTRACTION(n1,n2))
    elif ch=='3':
        print(MULTIPLYCATION(n1,n2))
    elif ch=='4':
        print(DIVISION(n1,n2))
    elif ch=='0':
        break
    print('=@=@=@=@=@=@=@')





    
