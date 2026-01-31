#wap to find greatest of three numbers assuming all are different
a=int(input("Enter first number: "))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a>b and a>c):
    print(a,"is greatest") 
elif(b>a and b>c):
    print(b,"is greatest")
else:
    print(c,"is greatest")