for num in range(1, 50):
    if num % 2 != 0:
        print(num)

# sum of number
total = 0
for num in range(1, 100):
    total += num

print("total sum of number", total)

# reverse string
text = input("please enter any text which is provide you in reverse form: ")
reverse_text = ""
for ch in text:
    reverse_text = ch + reverse_text

print("Reversed String is", reverse_text)

# pattern print
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# user input number give total when user inter zero

total = 0

while True:
    num = int(input("please enter number between 1 to 100 (if you entered 0 you get sum number): "))
    if num == 0:
        break

    total += num
print("total sum is", total)


