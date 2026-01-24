print("Single program demonstrating all loops in Python\n")

i = 1

# WHILE loop
while i <= 3:
    print("While loop i =", i)

    # FOR loop
    for j in range(1, 4):

        # CONTINUE statement
        if j == 2:
            continue

        print("  For loop j =", j)

        # PASS statement
        if j == 3:
            pass

    # BREAK statement
    if i == 3:
        break

    i += 1

# DO-WHILE loop (simulated)
print("\nDo-While Loop:")
k = 5

while True:
    print("k =", k)
    k += 1
    if k > 2:
        break
