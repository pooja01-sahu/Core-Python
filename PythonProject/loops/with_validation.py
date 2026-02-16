total = 0

while True:
    user_input = input("enter number between 1 to 100(if you enterd 0 then you get sum of number): ")

    # check input is number or not
    if not user_input.isdigit():
        print("invalid input! please enter valid input")
        continue

    num = int(user_input)

    #    stop condition
    if num == 0:
        break

    #    check range
    if num < 1 or num > 100:
        print("please enter number between only 1 to 100")
        continue

    total += num

print("Total sum is.", total)
