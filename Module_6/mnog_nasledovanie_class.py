class Car:
    price = 1000000
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} Марка {}'.format(self.__class__.__name__, self.name)

    def horse_powers(self, power):
        return ("Количество лошадинных сил = " + str(power) + ". Стомость машины = " + str(self.price))

class Vehicle:
    vehicle_type = "none"

    def __init__(self, name):
        self.name = name

    def type(self):
        return '{} Марка {}'.format(self.__class__.__name__, self.name) + ' тип машины = ' + self.vehicle_type


class Nissan(Car, Vehicle):
    price = 50000
    vehicle_type = "Сидан"
    def horse_powers(self, power):
        return ("Количество лошадинных сил " + self.name + " = " + str(power) + ". Стомость машины = " + str(self.price))

car = Nissan("Z350")
print(car)
print(car.type())
print(car.horse_powers(250))