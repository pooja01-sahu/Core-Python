import random

names = ["Ali", "Sara", "John", "Emma"]
print(random.sample(names, 2))

numbers= [random.randint(1, 100) for i in range(5)]
print(numbers)

number = random.random()  # random float between 0.0 and 1.0
print(number)

number = random.uniform(5, 20)  # random float between 5 and 20
print(number)

items = [10, 20, 30, 40]
print(random.choice(items))

print(random.randrange(1, 20, 2))  # odd numbers only

colors = ["red", "blue", "green"]
print(random.choice(colors))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

random.seed(2)
print(random.randint(1, 100))