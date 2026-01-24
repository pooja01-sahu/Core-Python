# name = "vijay dinanath chouhan"
#
# for ch in "abcdefghijklmnopqrstuvwxyz":
#     print(ch)
#     count = 0
#     for letter in name:
#         if ch == letter:
#             count = count + 1
#
#             if count != 0:
#                 print(letter)

name = "vijay dinanath chouhan"

for ch in "abcdefghijklmnopqrstuvwxyz":
    c = name.count(ch)
    if c != 0:
        print(ch, "count =", c)