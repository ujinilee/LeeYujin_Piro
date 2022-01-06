#딕셔너리에 데이터가 있는지
class isExistData(Exception):
    pass

#학생데이터가 딕셔너리에 있는지
class isExistStu(Exception):
    pass

#정수인지
class isInt(Exception):
    pass

student=dict()

def Menu1(name,mid,fianl):
    student[name]=[mid,final,None]
    #print(student[name])
    
def Menu2():
    
    for i in range (len(student)):
        student2=list(student.items())
        if(student2[i][1][2]==None):
            avg=(int(student2[i][1][0])+int(student2[i][1][1]))/2
            if(avg>=90):
                garde='A'
            elif(avg>=80 and avg<90):
                grade='B'
            elif(avg>=70 and avg<80):
                grade='C'
            else:
                grade='D'
                
            student[list(student.keys())[i]]=[student2[i][1][0],student2[i][1][1],grade] #mid,final값 다 같아서 수정
    
    #print(student)

def Menu3():
    pv=False
    
    for i in range (len(student)):
        student2=list(student.items())
        if(student2[i][1][2]==None):
            print("There is a student who didn't get grade.")
            pv=False
            break
        else:
            pv=True
            
    if(pv==True):
        print("---------------------")
        print("name mid final grade")       
        print("---------------------")
        
        for i in range (len(student)):
            student2=list(student.items())
            if(student2[i][1][2]!=None):
                #print(student(list(student.keys())[i]))
                #print(list(student.values())[i])
                #print()
                #print(list(student.keys())[i]) #이름출력
                #print()
                #student2=list(student.items())
                #print(int(student2[i][1][0]))
                #print(int(student2[i][1][1]))
                #print(student2[i][1][2])
                
                print(list(student.keys())[i], ' ',int(student2[i][1][0]), ' ',int(student2[i][1][1]), ' ',student2[i][1][2] )
            
            #print(student(list(student.keys())[i]))
            #print(list(student.values())[i])

def Menu4(name):
    student.pop(name)
    print(name,"student information is deleted")
    print(student)
    


print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while(1):
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    
    if choice == "1":
        try:
            name, mid, final=input("Enter name mid-score final-score : ").split(" ")
            
            
            if(mid.isnumeric()!=True or final.isnumeric()!=True):
                raise isInt
            
            else:
                Menu1(name,mid,final)
            #if (name in student) == True:
            #if(name in student == True):
                #raise isExistStu
            
            
        except ValueError:
            print("Num of data is not 3!")
            
        except isInt:
            print("Score is not positive integer!")
            
        except isExistStu:
            print("Already exist name!")
        
    elif choice == "2" :
        #Menu2()
        #print("Grading to all students.")
        try:
            
            if(len(student)==0):
                raise isExistData
            else:
                print("Grading to all students.")
                Menu2()
            
        except isExistData:
            print("No student data!")
        
    elif choice == "3" :
        #Menu3()
        
        try:
            Menu3()
            if(len(student)==0):
                raise isExistData
            
        except isExistData:
            print("No student data!")
        
    elif choice == "4" :
        #name=input("Delete name : ")
        #Menu4(name)
        
        try:
            name=input("Delete name : ")
            Menu4(name)
            if(len(student)==0):
                raise isExistData
            
        except KeyError:
            print("Not exist name!")
            
        except isExistData:
            print("No student data!")
        
    elif choice == "5" :
        print("Exit Program!")
        break

    else :
        print("Wrong number. Choose again.")



