number = 153
n = number
sum = 0
rem = 0

while n > 0:
    print(n)
    rem = n % 10
    print("rem",rem)
    sum = (sum * 10) + rem
    print("sum",sum)
    n = n // 10

print("Reverse Number:", sum)