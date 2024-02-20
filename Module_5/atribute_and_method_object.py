class House:
    def __init__(self):
        self.numberOfFloors = 10

    def start(self):
        i = 0
        while self.numberOfFloors >= i:
            print("Текущий этаж равен = ", i)
            i += 1


House().start()
