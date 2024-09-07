import sys


class Vehicle:

    vehicleType = ["Two-Wheeler", "Four-Wheeler"]
    percentage = [2, 6]

    def __init__(self):
        self.__id = None
        self.__type = None
        self.__cost = None
        self.__premium = None

    def setId(self, i):
        self.__id = i

    def getId(self):
        return self.__id

    def setType(self, t):
        if t in Vehicle.vehicleType:
            self.__type = t
        else:
            print("Invalid type")
            sys.exit(0)
        self.__type = t

    def getType(self):
        return self.__type

    def setCost(self, c):
        self.__cost = c

    def getCost(self):
        return self.__cost

    def setPremium(self, p):
        self.__premium = p

    def getPremium(self):
        return self.__premium

    def calculatePremium(self):
        t = self.getType()
        i = Vehicle.vehicleType.index(t)
        per = Vehicle.percentage[i]
        ct = self.getCost()
        amount = ct*(per/100)
        self.setPremium(amount)


v = Vehicle()
v.setId(input("Enter Vehicle ID: "))
v.setType(input("Enter Vehicle Type: "))
v.setCost(int(input("Enter Vehicle Cost: ")))

v.calculatePremium()
print("----------------------------------------")
print("Vehicle ID: ", v.getId())
print("Vehicle Type: ", v.getType())
print("Vehicle Cost: ", v.getCost())
print("Premium amount: ", v.getPremium())


'''
Output: -
Enter Vehicle ID: 1HGCM82633A004352
Enter Vehicle Type: Four-Wheeler
Enter Vehicle Cost: 15782000
----------------------------------------
Vehicle ID:  1HGCM82633A004352
Vehicle Type:  Four-Wheeler
Vehicle Cost:  15782000
Premium amount:  946920.0
'''
