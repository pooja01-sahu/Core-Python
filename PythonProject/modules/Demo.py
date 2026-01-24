class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


emp = Employee("Niya", 5000)

print(emp.get_name())
print(emp.get_salary())