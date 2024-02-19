num = (1,4,9,16,25,36,49,64,81,100)
search = int(input("Enter any item from the tuple : "))
i = 0
# while i < len(num):
#     if num[i] == search:
#         print("Found ",num[i]," at index", i)
#     i += 1

for j in (1,len(num)-1):
    if(num[j]== search):
        print(f"The element {search} is present at index {j}")