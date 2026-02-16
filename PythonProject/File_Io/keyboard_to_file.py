def KeyboardToFile():
    file = open("C:/Users/Dell/PycharmProjects/PythonProject/Files/keyboardtext.txt", 'w')
    text = input('Enter your message = ')

    while (text != "quit"):
        file.write(text)
        file.write('')
        text = input('')
    file.close()

KeyboardToFile()
