# Program to check largest no. among given three numbers , by using logical operator.
a = int(input("Enter First number :"))
b= int(input("Enter Second number :"))
c = int(input("Enter Third number :"))
print("Your Entered Numbers are :",a,b,c)
if(a>b and b>c) :
    print(a,"is the Largest Number among three numbers")
elif(b>a and a>c):
    print(b,"is the Largest Number among three numbers")
else:
    print(c,"is the Largest Number among three numbers")