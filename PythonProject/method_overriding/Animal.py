class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog makes a sound")


# In method overriding on run time behaviour change and on run time firstly compilar check if that method which is call by object if it
# is available in child then it call that otherwise it is call parent method
d = Dog()
d.sound()
