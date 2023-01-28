ls =  ["Red", "Green", "Blue", "Yellow", "Green"]    #List 
print(type(ls))
print(ls[0])    #list index for Accessing list items   
print(ls[1])    #list index for Accessing list items
print(ls[2])    #list index for Accessing list items
print(ls[3])    #list index for Accessing list items
print(ls[4])    #list index for Accessing list items

print()
#"Converting negative index to positive :")
print(ls[-3])   #negative index
print(ls[len(ls)-3])    # Positive index
print(ls[5-3])          #Positive index
print(ls[2])            #Positive index

print()
#"Check whether given item is present in list :")
if "Red" in ls:
    print("Yes it is present ")
else:
    print("It is not present")

print()
#Range of index is to print items by specifying where to start and end
print(ls[2:4])
print(ls[1:4:2])

print()
names = ["Anush" , "Ansh", "Rose" , "Lokesh" , "Pilu"]
namesWith_0 = [item for item in names if "u" in item]
print(namesWith_0)

