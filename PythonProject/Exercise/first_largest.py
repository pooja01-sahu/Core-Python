# number = [10,25,7,89,45]
# largest = max(number)
# print("largest",largest)

number = [10, 25, 7, 89, 45, 68, 58, 99]
largest = number[0]

for num in number:
    if num > largest:
        largest = num

print("largest", largest)
