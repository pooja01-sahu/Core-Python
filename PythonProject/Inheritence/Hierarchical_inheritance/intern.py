from Inheritence.Hierarchical_inheritance.Employee import Employee
from Inheritence.Hierarchical_inheritance.Full_time_employee import full_time_employee
from Inheritence.Hierarchical_inheritance.part_time_employee import part_time_employee


class Intern(Employee):

    def __init__(self, emp_id, name, base_salary, stipend):
        super().__init__(emp_id, name, base_salary)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


pt = part_time_employee(101, "Alice", 0, 20, 500)
ft = full_time_employee(102, "Bob", 30000, 5000)
intern = Intern(103, "Charlie", 0, 8000)

pt.display_info()
print("Part-time Salary:", pt.calculate_salary())

ft.display_info()
print("Full-time Salary:", ft.calculate_salary())

intern.display_info()
print("Intern Salary:", intern.calculate_salary())
