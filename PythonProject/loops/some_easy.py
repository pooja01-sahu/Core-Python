for i in range(5):
    print("here is i value between 1 to 5 ", i)

# conditional loop
for i in range(1, 11):
    if i % 2 == 0:
        print("even number", i)
    else:
        print("odd number", i)
# nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
# pattern printing
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# conditional
numbers = [1, 2, 7, 6, 8, 9, 6, 50]
total = 0

for num in numbers:
    if num % 2 == 0:
        print("what is number", num)
        total += num
print("total of even number", total)

# control flow loop
for i in range(1,11):
    if i == 5:
        print("value of i",i)
        continue
    if i == 9:
        print("value of i",i)
        break
print("what i value of i",i)
# some list iterate
fruits = ["apple", "banana", "cherry","Mango"]
for fruit in fruits:
    print(fruit)
    if fruit == "cherry":
        print("Found cherry!")
        break
# enumerate
names = ["A", "B", "C"]

for index, value in enumerate(names):
    print(index, value)
