marks1 = int(input("Enter the Marks of Subject 1 "))
marks2 = int(input("Enter the Marks of Subject 2 "))
marks3 = int(input("Enter the Marks of Subject 3 "))
per = (marks1 + marks2 + marks3) /3
if(per>=80):
    print("Grade : A")
elif(per>=70 and per<80):
    print("Grade : B")
elif(per>=60 and per<70):
    print("Grade : C")
else:
    print("Grade :D")