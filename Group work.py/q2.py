class Employee:  
    def __init__(self, name, emp_id):  
        self.name = name  
        self.emp_id = emp_id  

    def __str__(self):  
        return f"ID: {self.emp_id}, Name: {self.name}"  


class Department:  
    def __init__(self, department_name):  
        self.department_name = department_name  
        self.employees = []  # Initialize an empty list to hold employees  

    def add_employee(self, employee):  
        """Add an employee to the department."""  
        self.employees.append(employee)  
        print(f"{employee.name} has been added to the {self.department_name} department.")  

    def remove_employee(self, employee):  
        """Remove an employee from the department."""  
        if employee in self.employees:  
            self.employees.remove(employee)  
            print(f"{employee.name} has been removed from the {self.department_name} department.")  
        else:  
            print(f"{employee.name} is not in the {self.department_name} department.")  

    def list_employees(self):  
        """List all employees in the department."""  
        print(f"Employees in the {self.department_name} department:")  
        for employee in self.employees:  
            print(employee)  

    def transfer_employee(self, employee, new_department):  
        """Transfer an employee to another department."""  
        if employee in self.employees:  
            self.remove_employee(employee)  # Remove from current department  
            new_department.add_employee(employee)  # Add to new department  
            print(f"{employee.name} has been transferred to the {new_department.department_name} department.")  
        else:  
            print(f"{employee.name} is not in the {self.department_name} department.")  


# Example usage  
# Creating departments  
dept_sales = Department("Sales")  
dept_marketing = Department("Marketing")  

# Creating employees  
emp1 = Employee("Roman", 101)  
emp2 = Employee("Seth", 102)  
emp3 = Employee("Jay", 103)  

# Adding employees to the Sales department  
dept_sales.add_employee(emp1)  
dept_sales.add_employee(emp2)  

# Listing employees in Sales  
dept_sales.list_employees()  

# Transferring an employee from Sales to Marketing  
dept_sales.transfer_employee(emp1, dept_marketing)  

# Listing employees in both departments after transfer  
dept_sales.list_employees()  
dept_marketing.list_employees()