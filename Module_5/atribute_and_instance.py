import random as ran
class Builiding:
    total = 0

    def __init__(self):
        Builiding.total = self.total + 1


number = ran.randint(40, 65)
while number > Builiding.total:
    Builiding()

print(Builiding.total)