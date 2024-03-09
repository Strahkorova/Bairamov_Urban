
class Buiding:

    def __init__(self, floor: int):
        self.floors = floor

    def __eq__(self, other):
        return self.floors == other


b1 = Buiding(5)
b2 = Buiding(5)
#print(b1 == b2)


class Clock:
    def __init__(self, seconds: int):
        self.seconds = seconds

    def __eq__(self, other):
        sc = other
        return self.seconds == sc


c1 = Clock(1000)
c2 = Clock(1000)
print(c1 == c2)
