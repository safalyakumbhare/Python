marks1 = int(input("Enter the Marks of Subject 1 :"))
marks2 = int(input("Enter the Marks of Subject 2 :"))
marks3 = int(input("Enter the Marks of Subject 3 :"))
per = (marks1 + marks2 + marks3) / 3
print("The Total Percentage is :", per)
if per >= 80:
    print("Grade : A")
elif per >= 70 and per < 80:
    print("Grade : B")
elif per >= 60 and per < 70:
    print("Grade : C")
elif per >= 40 and per < 60:
    print("Grade : D")
else:
    print("Grade : E")
