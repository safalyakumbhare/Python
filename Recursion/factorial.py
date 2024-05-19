def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")
