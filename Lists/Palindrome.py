li = []
for i in range (5):
    li.append(input("Enter the Number to check whether it is a Palindrome or not : "))

print ("The list entered by the user are:",li)
lic = li.copy()

li.reverse()

if lic == li:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome") 