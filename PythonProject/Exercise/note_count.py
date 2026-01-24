notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]

amount = 2526

count = 0

for i in notes:
    count = amount // i
    print("amount",amount)
    print("count",count)
    if count > 0:
        print("line 11 i value",i)
        print(i, " = ", count)
    amount = amount % i