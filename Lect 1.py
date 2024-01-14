# Code From Python IDLE Interpreter
Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
var = "Safalya"
print var
SyntaxError: incomplete input
print(var)
Safalya
print("hello")
hello
print("Hello!",var)
Hello! Safalya
type(var)
<class 'str'>
var = 12
type(var)
<class 'int'>
var = true
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    var = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> var = 100
>>> type(var)
<class 'int'>
>>> var = 12.2
>>> var = false
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    var = false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> var = True
>>> type(var)
<class 'bool'>
>>> var = input("Enter your name : ")
Enter your name : Safalya
>>> print("Hello ",var)
Hello  Safalya
>>> var = input("Enter any number ")
Enter any number 8
>>> print("Square ",var * var)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print("Square ",var * var)
TypeError: can't multiply sequence by non-int of type 'str'
>>> x = "Nagpur"

>>> 3*x
'NagpurNagpurNagpur'
>>> var = int(var)
>>> print("Square is ",var * var)
Square is  64
