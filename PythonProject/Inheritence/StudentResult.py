from Inheritence.Student import Student


class StudentResult(Student):

    def getMarks(self):
         self.studentClass = input("Enter Student Class: ")
         print("Enter your subject marks", )
         self.chemistry = input("Enter Chemistry Marks: ")
         self.physics = input("Enter Physics Marks: ")
         self.maths = input("Enter Maths Marks: ")
         self.English = input("Enter English Marks: ")
