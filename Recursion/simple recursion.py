#Recursion means a function callng it self repeatedly

def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1);
num = int(input("Enter a number : "))
print("The Factorial is of ",num,"is ",fact(num))