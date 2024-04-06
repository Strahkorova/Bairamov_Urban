def arifmetic(oper):
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


class Rect:
   def __init__(self, value):
       self.value = value
   def __call__(self, n):
       return self.value ** (1/n) #вывести из под корня


arif = arifmetic("+")
print(arif(16, 2))
print(degree(16, 2))
print(degr(16, 2))

rec = Rect(16)
print(rec(2))
