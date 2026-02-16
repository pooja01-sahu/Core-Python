import pickle
from write_object_file import Employee

with open("C:/Users/Dell/PycharmProjects/PythonProject/Files/employee.txt", 'rb') as file:
    obj = pickle.load(file)

    print("Printing employee information after unplucking")
    obj.disply()
