#Check the count of student scored a specified number of CGPA.
score = (9,8,8,9,5,7,7,9,7,8,8,6)
CGPA = int(input("Enter the CGPA : "))
count = score.count(CGPA)
print("There are ",count,"students Scored ",CGPA," CGPA")