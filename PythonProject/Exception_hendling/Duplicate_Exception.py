# class Duplicate_Exception(Exception):
#
#     def __init__(self, msg):
#         super().__init__(msg)
#
#
# Login_Id = input("Please enter your login id: ").strip()
# password = input("Please enter your password: ").strip()
#
# try:
#     if (Login_Id != "" and password != "") and (Login_Id != "Admin" and password != "Admin"):
#         print("congrtulation you are registered successfully")
#     else:
#         raise Duplicate_Exception("Dulicate User")
# except EOFError:
#     print("No input provided")
# except Duplicate_Exception as d:
#     print(d)


class Duplicate_Exception(Exception):

    def __init__(self, msg):
      super().__init__(msg)

try:
    Login_Id = input("Please enter your login id: ").strip()
    password = input("Please enter your password: ").strip()

    # Handle empty input
    if not Login_Id or not password:
        raise ValueError("Input cannot be empty")

    # Handle duplicate user
    if Login_Id == "Admin" and password == "Admin":
        raise Duplicate_Exception("Duplicate User")

    print("Congratulations! You are registered successfully.")

except EOFError:
    print("No input provided (EOF).")

except ValueError as v:
    print(v)

except Duplicate_Exception as d:
    print(d)

