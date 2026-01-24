name = "vijay dinanath chouhan"
word_list = name.split()  # ['vijay', 'dinanath', 'chouhan']

for word in word_list:
    print("line 5 word",word)
    reversed_word = ""
    print("line 7 reverseword",reversed_word)
    for char in word:
        print(" line 8 char",char)
        reversed_word = char + reversed_word
    print(reversed_word, end=" ")

