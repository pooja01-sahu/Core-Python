# num = int(input("Enter a number: "))
# total = 0
#
# while num > 0:
#     digit = num % 10
#     total += digit
#     num //= 10
#
# print("Sum of digits:", total)
# Reverse number
num = 123456
reverse_num = 0

while num > 0 :
    print("firstly num is",num)
    digit = num % 10
    print("after persentage",digit)
    reverse_num = reverse_num * 10 + digit
    print("reverse number",reverse_num)
    num //= 10

print("Reverse number", reverse_num)

# count vowels
text = "Artificial Inteligence"
count = 0
vowels = "aeiou"

for char in text:
    if char in vowels:
        count += 1

print("Vowels",count)
# correct password

correct_password = "phython#2026"


