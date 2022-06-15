ch='y'
while(ch=='y' or ch=='Y'):
    a=int(input("enter the number :"))
    b=int(input("enter the number :"))
    print(" M E N U")
    print(" 1. add")
    print(" 2.sub")
    print(" 3.mul")
    print(" 4,div")
    c=int(input("enter your chose(1/2/3/4):"))
    if(c==1):
        print(" A D D I T I O N ")
        print(a," + ",b," = ",a+b)
    elif(c==2):
        print(" S U B S T R A C T I O N ")
        print(a," - ",b," = ",a-b)
    elif(c==3):
        print(" M U L T I P I C A T I O N ")
        print(a," * ",b," = ",a*b)
    elif(c==4):
        print(" D I V I S I O N ")
        print(a," / ",b," = ",a/b)
    else:
        print("invalid entery")
        
    ch=input("do you want to continue:")

    
print("THANK YOU ")
