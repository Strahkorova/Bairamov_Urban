
class Buiding:

    def __init__(self, floor: int, build: str):
        self.numberOfFloors = floor
        self.buildingType = build

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


b1 = Buiding(5, "этаж")
b2 = Buiding(5, "этаж")
print(b1 == b2)
