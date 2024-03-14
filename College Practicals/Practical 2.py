sub1 = int(input("Enter your Marks in Python : ") )
sub2 = int(input("Enter your Marks  in Marketing Management : "))
sub3 = int(input("Enter your Marks in Advance Java : "))

total = sub1+sub2+sub3
per = total/3
print("Your Total Marks are : ",total)
print("Your Percentage is : ", per)
if per >=80:
    print("You got A Grade")
elif per>=70 and per<80:
    print("You got B Grade")
elif per>=60 and per<70:
    print("You got C Grade")
elif per>=40 and per<60:
    print( "You got D Grade")
elif per<40:
    print("You got E Grade")

