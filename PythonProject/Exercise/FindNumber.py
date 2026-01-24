list = [10, 11, 5, 13, 17, 88]
number = 15
count = 0

n = list.count(number)
print(n)
if n > 0:
    count += 1
    print("number exist")
else:
    print("number not exist")
# for i in list:
#     if i == number:
#         count += 1
#
# if count == 0:
#     print("number not exist")
# else:
#     print("number exist")
