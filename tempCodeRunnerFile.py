import time

def countdown_generator():
    num = 10
    while num >= 1:
        yield num
        time.sleep(1)
        num -= 1

# Using a for loop to print the countdown
for number in countdown_generator():
    print(number)
