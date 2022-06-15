a=int(input("enter the number to be reversed"))
rev=0
while(a!=0):
    b=a%10
    a=int(a/10)
    rev=rev*10+b
print("reversed number is:",rev)
