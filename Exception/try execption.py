date = int(input("Enter Your Date of Birth :"))
try:
    if date>31:
        raise  ('Invalid Day')
except ValueError as e:
    print("Invalid Date")
# finally:
#     print("Enter the Date Again")