class A:
    _a = 10   #protected variable
    __b = 20  #private variable
    def show(self):
        print("a = :", self._a)
        self._a = 11
        print("a = :", self._a)
        self.__b = 22
        print("b = :", self.__b)


obj = A()
obj.show()
print(A._a)
# print(A.__b)