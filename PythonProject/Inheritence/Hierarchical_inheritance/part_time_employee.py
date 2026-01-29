from Inheritence.Hierarchical_inheritance.Employee import Employee


class part_time_employee(Employee):

    def __init__(self, emp_id, name, base_salary, hours_worked, hourly_rate):
        super().__init__(emp_id, name, base_salary)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

