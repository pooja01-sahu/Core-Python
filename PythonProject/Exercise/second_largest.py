number = [25, 36, 98, 45, 78, 45, 125]
highest = 0
second_highest = 0

for n in number:
    if n > highest:
        second_highest = highest
        highest = n

    elif n > second_highest and n != highest:
        second_highest = n

print("The highest number is", highest)
print("The second highest number is", second_highest)
