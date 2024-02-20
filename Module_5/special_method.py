
class House:

    def __init__(self):
        self.number = 0

    def start(self, i):
        self.number = i
        print("Номер = ", i)


House().start(8)
