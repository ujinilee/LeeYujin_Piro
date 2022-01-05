import random

def brGame():
    num=0
    score=0
    player=True

    while(score!=31):
        while(1):
            if(player==True):
                num=input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능):")
            
            if(player==True and num.isnumeric()!=True):
                print("정수를 입력하세요")
            elif(player==True and int(num)!=1 and int(num)!=2 and int(num)!=3):
                print("1,2,3 중 하나를 입력하세요")    
            else:
                if(player==False):
                    num=random.randint(1,3)
                for i in range(1,int(num)+1):
                    score+=1
                    if(score==31):
                        if(player==True):
                            print('player : ',score)
                            print("computer win!")
                        else:
                            print('computer : ',score)
                            print("player win!")
                        break
                    
                    if(player==True):
                        print('player : ',score)
                    else:
                        print('computer : ',score)
                
                player=not player
                break
            
        if(score==31):
            break

        
brGame()