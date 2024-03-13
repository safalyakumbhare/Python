class demo:
    def getdata(self):
        self.name = input("Enter the name :")
        self.roll = int(input("Enter roll number :"))

    def show(self):
        print("Name : ", self.name)
        print("Roll Number :", self.roll)

# create object of class
obj = demo()
obj.getdata()
obj.show()