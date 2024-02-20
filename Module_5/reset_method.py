
class Buiding:

    def __init__(self, floor: int):
        if not isinstance(floor, int):
            print("Этаж должен быть целым числом")
        self.floors = floor

    def __eq__(self, other):
        return self.floors == other


b1 = Buiding(5)
b2 = Buiding(5)
print(b1 == b2)
