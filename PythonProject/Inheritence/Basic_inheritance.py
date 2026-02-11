class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):

    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def display(self):
        print(f"brand: {self.brand},doors: {self.doors}")


c = Car("Toyoto", 4)
c.start()
c.display()
