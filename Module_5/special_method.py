
class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, i):
        self.numberOfFloors = i
        print("Номер = ", self.numberOfFloors)


class House1:
    numberOfFloors = 0

    def setNewNumberOfFloors(self, i):
        self.numberOfFloors = i
        print("Номер1 = ", self.numberOfFloors)

House1().setNewNumberOfFloors(5)
House().setNewNumberOfFloors(8)
