class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.base_salary}")