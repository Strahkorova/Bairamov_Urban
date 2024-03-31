class Except_maoney(Exception):
    def __str__(self):
        return "Недопустимое значение! Количество денег должно быть в заданном диапазоне"


class Except_price(Exception):
    def __str__(self):
        return "У вас не хватает денег для покупки товара"

class Person:
    def __init__(self, name, money, prod, price):
        self.name = name
        min_money, max_money = 100, 500
        if min_money < money < max_money:
            self.money = money
        else:
            raise Except_maoney(min_money, max_money,money)

        if price < money:
            self.prod = prod
            self.price = price
        else:
            raise Except_price()

    def display(self):
        print(f"Имя: {self.name}  количество денег: {self.money}")
        print(f"покупатель {self.name} купил {self.prod} стоимостью {self.price}")


try:
    tom = Person("Tom", 250, "кружка", 300)
    tom.display()

except Except_maoney as e:
    print(e)
except Except_price as q:
    print(q)