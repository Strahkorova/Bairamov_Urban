class Car:
    price = 1000000
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} Марка {}'.format(self.__class__.__name__, self.name)

    def horse_powers(self, power):
        return ("Количество лошадинных сил = " + str(power) + ". Стомость машины = " + str(self.price))

class Nissan(Car):
    price = 50000

    def horse_powers(self, power):
        return ("Количество лошадинных сил " + self.name + " = " + str(power) + ". Стомость машины = " + str(self.price))

class Kia(Car):
    price = 80000

    def horse_powers(self, power):
        return ("Kia " + self.name + " имеет " + str(power) + " лощадиных сил. Стомость машины = " + str(self.price))

car = Kia("Sorento")
print(car)
print(car.horse_powers(230))