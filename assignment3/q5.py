# 5. Write a Python class Employee with attributes like emp_id, emp_name,  
# emp_salary, and emp_department and methods like calculate_emp_salary,  
# emp_assign_department, and print_employee_details. 
# Sample Employee Data: 
# "ADAMS", "E7876", 50000, "ACCOUNTING" 
# "JONES", "E7499", 45000, "RESEARCH" 
# "MARTIN", "E7900", 50000, "SALES" 
# "SMITH", "E7698", 55000, "OPERATIONS"
# • Use 'assign_department' method to change the department of an  employee. 
# • Use 'print_employee_details' method to print the details of an  employee. 
# • Use 'calculate_emp_salary' method takes two arguments: salary and  hours_worked,
#  which is the number of hours worked by the employee.  
# If the number of hours worked is more than 50, the method computes  overtime and 
# adds it to the salary. Overtime is calculated as following  formula: 
# • overtime = hours_worked - 50 
# Overtime amount = (overtime * (salary / 50)) 

class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary
        return total_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Salary: {self.emp_salary}")
        print(f"Department: {self.emp_department}")

employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")

employee1.emp_assign_department("MARKETING")
employee1.print_employee_details()

hours_worked = 55
print(f"Total salary after overtime: {employee1.calculate_emp_salary(hours_worked)}")


