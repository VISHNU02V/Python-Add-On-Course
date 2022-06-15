
b=int(input("enter the number of records"))
l=[]
flag=0
for i in range(b):
    name=input("enter the name of student:")
    class1=input("enter the class of the student:")
    mark=input("enter the marks:")
    student={"name":name,"class":class1,"mark":mark}
    l.append(student)
c=input("enter the name :")
for i in l:
    if (i["name"]==c):
        print("name:",i["name"])
        print("class:",i["class"])
        print("mark:",i["mark"])
        flag=0
        
if(flag == 1):
    print("student not found")
