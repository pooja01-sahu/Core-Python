n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
sum = 0

while temp > 0:
    print(temp)
    digit = temp % 10
    print("9 line", digit)
    sum = sum + digit ** digits
    print("11 line",sum)
    temp = temp // 10
    print("last temp",temp)

if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
