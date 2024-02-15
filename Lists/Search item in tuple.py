num = (1,4,9,16,25,36,49,64,81,100)
search = 36
i = 0
while i < len(num):
    if num[i] == search:
        print("Found ",num[i]," at index", i)
    i += 1