class Login_exception(Exception):

    def __init__(self,msg):
        super().__init__(msg)

Login_id = "Admin"
Password = "Admin"

try:
    if Login_id == "admin" and Password == "Admin":
        print("Login Successful")
    else:
        raise Login_exception("Login Failed")
except Login_exception as e:
    print(e)
