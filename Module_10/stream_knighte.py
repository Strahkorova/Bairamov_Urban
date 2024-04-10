import time
from threading import Thread

class knight(Thread):
    def __init__(self, name, skill, enemy):
        Thread.__init__(self)
        self.name = name
        self.skill = skill
        self.enemy = enemy

    def run(self):
        print(f"Рыцарь {self.name} пришел на защиту!")
        i = 1
        while self.enemy != 0:
            self.enemy -= self.skill
            print(f" Сэр {self.name} сражается {i} день(дня). Осталось количество врагов - {self.enemy}", flush = True)
            i += 1
            time.sleep(1)
        print(f"Сэр {self.name} победил врагов за {i-1} дня. Он спас королевтсво!", flush = True)


print(f"Враги напали на королевство Камелот!")

Lancelot = knight("Ланцелот", 20, 100)
Lancelot.start()
time.sleep(0.5)
Galahart = knight("Галахарт", 10, 100)
Galahart.start()

Lancelot.join()
Galahart.join()
print("Все битвы закончились! УРА! УРА! УРА!")