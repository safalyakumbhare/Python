num = (1,4,9,16,25,36,49,64,81,100)
search = int(input("Enter any item from the tuple : "))
i = 0
while i < len(num):
    if num[i] == search:
        print("Found ",num[i]," at index", i)
    i += 1