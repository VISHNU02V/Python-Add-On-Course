
class Myclass:
    def addtwo(self,a,b):
        c=a+b
        return c

c=Myclass()
x=int(input("enter the value of the x:"))
y=int(input("enter the value of the y:"))
print(" SUM OF THE 2 NUMBERS ")
print("The numbers are: ",x," , ",y)
print("sum :",c.addtwo(x,y))

