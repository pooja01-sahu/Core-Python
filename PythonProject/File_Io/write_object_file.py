import pickle


class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def disply(self):
        print(self.id, "\t", self.name, "\t", self.salary)

with open("C:/Users/Dell/PycharmProjects/PythonProject/Files/employee.txt", 'wb') as file:
        emp = Employee(1, "Tanvi", 70000)
        pickle.dump(emp, file)
