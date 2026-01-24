from Inheritence.Employee import Employee


class Manager(Employee):

    def getManager(self):
        print("Here is information about Employee")
        print("Employee name: ", self.name)
        print("Employee salary: ", self.salary)
        print("Manager name: ", self.manager)

mn = Manager()
mn.show()
mn.getManager()
