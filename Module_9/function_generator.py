def arifmetic():
    oper = input("Укажите тип операции: ")
    if oper == "+":
        def summ(x, y):
            return x + y
        return summ

    elif oper == "-":
        def difference(x, y):
            return x - y
        return difference

    elif oper == "*":
        def multiply(x, y):
            return x * y
        return multiply

    elif oper == "/":
        def removal(x, y):
            return x / y
        return removal


degree = lambda x, y: x ** y

def degr(x, y):
    return x**y


class Repeater:
   def __init__(self, value):
       self.value = value
   def __call__(self, n):
       return self.value ** (1/n) #вывести из под корня


x = float(input("Укажите параметр х: "))
y = float(input("Укажите параметр y: "))

arif = arifmetic()
print(arif(x, y))
print(degree(x, y))
print(degr(x, y))

repeat_five = Repeater(x)
print(repeat_five(y))