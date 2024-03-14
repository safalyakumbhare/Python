#Recursion means a function callng it self repeatedly

def num(n):
    if(n==0): #Base it is like giving condition to a loop
        return 
    print(n)  
    num(n-1)

num(10)