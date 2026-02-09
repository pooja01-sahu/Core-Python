a = 10
b = 2

# here if error is coming or not finally block always execute
try:
    c = a / b
    print("division", c)
except ZeroDivisionError as e:
    print(e)
finally:
    print("finally block executed")

# here when there is no error in try block so else block is execute

a = 10
b = 0

try:
    c = a / b
    print("division", c)
except ZeroDivisionError as e:
    print(e)
else:
    print("else block executed")
finally:
    print("finally block executed")
