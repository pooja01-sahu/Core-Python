from Inheritence import mobile
from Inheritence.mobile import Mobile


class SmartPhone(Mobile):

    def showDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("sim Type:", self.simType)
        print("companyName:", self.companyName)

s = SmartPhone()
s.getDevice()
s.OtherThing()
s.showDetails()
