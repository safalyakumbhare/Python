def rev(num):
    rvs = 0
    while (num > 0):
        dig = num % 10
        rvs = (rvs*10)+dig
        num = num // 10
    print("The reversed Number are ",rvs)

num = int(input("Enter the number : "))
rev(num)