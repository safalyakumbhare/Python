class emp:
    def getdata(self):
        self.name = input("Enter the Name : ")
        self.sal = input("Enter the Salary : ")

    def show(self):
        print("Emp Name : ",self.name,"Your Salary : ",self.sal)

e = emp()
e.getdata()
e.show()