try:
    a = int(input("enter a number: "))
    b = int(input("enter another number: "))
    print(a, "/", b, "=", a / b)
except ValueError:
    print("please enter valid number")
except ZeroDivisionError:
    print("cannot divide by zero")
