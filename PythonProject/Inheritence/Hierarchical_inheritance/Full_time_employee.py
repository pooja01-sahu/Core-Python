from Inheritence.Hierarchical_inheritance.Employee import Employee


class full_time_employee(Employee):
    def __init__(self, emp_id, name, base_salary, bonus):
        super().__init__(emp_id, name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus
