from Inheritence.Device import Device


class Mobile(Device):

    def OtherThing(self):
        print("Other Thing")
        self.simType = input("Sim Type:")
        self.companyName = input("Company Name:")


