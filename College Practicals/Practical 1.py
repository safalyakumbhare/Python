choice = input("What do you want to convert Farenheit or Celsius : ")

if(choice == "farenheit"):
    temp = float(input("Enter the Farenheit : "))
    celsius = (temp - 32)* 5/9
    print("The Temperature in Celsius is : ",celsius)

if(choice =="celsius"):
    temp = float(input("Enter the Celsius : "))
    farenheit = (temp * 9/5)+32
    print("The Temperature in Fahrenheit is : ",farenheit)