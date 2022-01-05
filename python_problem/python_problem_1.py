num=0

while(1):    
    num=input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능):")
    
    if(num.isnumeric()!=True):
        print("정수를 입력하세요")
    elif(int(num)!=1 and int(num)!=2 and int(num)!=3):
        print("1,2,3 중 하나를 입력하세요")    
    else:
        break