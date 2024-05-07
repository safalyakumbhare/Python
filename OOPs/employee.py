class Employee:
    def __init__(self, emp_id,emp_name,emp_salary,emp_department):
        self.EmpId = emp_id
        self.Name= emp_name
        self.Salary = emp_salary
        self.Department = emp_department

    def print_employee_details(self):
        print("The Employee Id : ",self.EmpId)
        print("The Employee Name : ",self.Name)
        print("The Employee Salary : ",self.Salary)
        print("The Employee Department : ",self.Department)

obj = Employee(1,"Safalya",50000,"IT")
obj.print_employee_details()