class student:
    def getdata(self):
        self.name = input("Enter the Name : ")
        self.roll = int(input("Enter the Roll no. : "))

class studdata(student):
    def display(self):
        print("Your Name : ",self.name)
        print("Your Roll : ",self.roll)

s = studdata()
s.getdata()
s.display()