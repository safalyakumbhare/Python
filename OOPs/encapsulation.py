class A:
    _a = 10   #protected variable
    __b = 20  #private variable
    def show(self):
        print("Inside the class a = :", self._a)
        print("Inside the class b = :", self.__b)


obj = A()
obj.show()
A._a = 11
A.__b = 22
print("Outside the class a = ",A._a)
print("Outside the class b = ",A.__b)