import warnings

class My_Warning():

    def warn_ignore(self):
        try:
            print("Мы его игнорируем. Он нам не подходит!")
        except UserWarning as e:
            print(f"Предупреждение: {e}")

    def warn_error(self):
        try:
            warnings.warn("Это - Должник!", UserWarning)
        except UserWarning as e:
            print(f"Предупреждение: {e}")

    def warn_always(self):
        try:
            warnings.warn("Надо подумать, но возможно!", UserWarning)
        except UserWarning as e:
            print(f"Предупреждение: {e}")

class client(My_Warning):

    def __init__(self, name, status, credit):
        self.name = name
        self.status = status
        self.credit = credit

    def bank(self):
        print(f"Клиент {self.name} хочет взять кредит!")
        if(self.status == 'банкрот'):
            warnings.simplefilter("ignore", UserWarning)
            My_Warning.warn_ignore(self)
        elif (self.status == 'должник'):
            warnings.simplefilter("error", UserWarning)
            My_Warning.warn_error(self)
        else:
            if (self.credit > 100):
                warnings.simplefilter("always", UserWarning)
                My_Warning.warn_always(self)
            elif (50 < self.credit < 100):
                warnings.simplefilter("default", UserWarning)
                My_Warning.warn_always(self)
            elif (self.credit < 50):
                print("Дадим кредит")
            else:
                warnings.simplefilter("always", UserWarning)
                My_Warning.warn_always(self)





CL = client("Tom", "банкрот", 200)
CL.bank()
print()
CL = client("Bob", "должник", 200)
CL.bank()
print()
CL = client("Jo", "хороший", 120)
CL.bank()

