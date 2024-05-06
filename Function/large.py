def large(a,b,c):
    print("The Number is ",a,b,c)

    if(a>b and b>c):
        print(a," is largest")
    elif (b>a and a>c):
        print(b," is Largest")
    else:
        print(c," is Largest")

a = int(input("Enter the First Number : "))
b = int(input("Enter the second Number : "))
c = int(input("Enter the third Number : "))

large(a,b,c)