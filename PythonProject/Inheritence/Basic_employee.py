class Employee:
    def calculate_salary(self):
        print("Base salary calculation")


class Devloper(Employee):

    def calculate_salary(self):
        print("Devloper Salary: Base + Coding bonus")


class Manager(Employee):

    def calculate_salary(self):
        print("Manager Salary: Base + Manegment bonus")


employees = [Devloper(), Manager()]

for e in employees:
    e.calculate_salary()
