print("** Welcome to Kaun Banega Crorepati **")
print()
print("Rules : Enter your options in A B C D format ")
print("Your Options must be entered in upper case")
print()
q1 = [
  "Q.1 Which one of the following is the correct extension of the Python file ?",
  "A. py", "B. python", "C. p", "D. None of these", "A"
]

q2 = [
  "Q.2 Which character is used in Python to make a single line comment ?",
  "A. /", "B. //", "C. #", "D. !", "C"
]

q3 = [
  "Q.3 Which of the following concepts is not a part of Python?", "A. Pointer",
  "B. Loop", "C. Dynamic Typing", "D. All of These", "A"
]

a = ["A", "B", "C", "D"]
p = 0
p1 = 1000
for i in range(3):
  if (i == 0):
    print(q1[0])
    print(q1[1])
    print(q1[2])
    print(q1[3])
    print(q1[4])
    a = input("Enter Your Option :")
    if (a == q1[5]):
      print("Congratulation You won Rs")
      prize = p + p1
      print(prize)
      print()
    else:
      print()
      print("Sorry You are Wrong")
      print("The Correct Option is A ")
      print()
      break
