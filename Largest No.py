# Program to check largest no. among given three numbers , by using logical operator.
a = int(input("Enter First number :"))
b= int(input("Enter Second number :"))
c = int(input("Enter Third number :"))
print("Your Entered Numbers are :",a,b,c)
if(a>b and b>c) :
    print(a,"is Largest")
elif(b>a and a>c):
    print(b,"is Largest")
else:
    print(c,"is Largest")