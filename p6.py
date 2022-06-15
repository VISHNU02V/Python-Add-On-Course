a=int(input("enter the number"))
rev=0
temp=a
while(a!=0):
    b=a%10
    a=int(a/10)
    rev=rev+b*b*b
if(temp==rev):
    print("is an armstrong")
else:
    print("is not an armstrong")
