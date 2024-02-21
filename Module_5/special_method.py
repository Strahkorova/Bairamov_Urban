
class House:
    def __init__(self):
        self.number = 0

    def start(self, i):
        self.number = i
        print("Номер = ", self.number)


class House1:
    number = 0

    def start(self, i):
        self.number = i
        print("Номер1 = ", self.number)

House1().start(5)
House().start(8)
