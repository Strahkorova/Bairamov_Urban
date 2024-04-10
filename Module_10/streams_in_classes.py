import time
import random

from collections import defaultdict

from threading import Thread

SKILL = (90,80,70,60,50,40,30,20,10,0)

class Knight(Thread):
    def __init__(self, name, skills, day, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skills = skills
        self.day = day
        self.catch = defaultdict(int)
    def run(self):
        self.catch = defaultdict(int)
        for skill in reversed(range(self.skills)):
            print(f'{self.name} сражается день (дня) {skill} врагов', flush= True)
            _= 5**random.choice(SKILL)
            if skill is None:
                print(f'{self.name}: никто сегодня не пришел')
            else:
                print(f'{self.name} у меня сегодня {skill} врагов', flush= True)
                self.catch[skill] += 1
        print(f'Итого {self.name} убил:')
        for skill, count in self.catch.items():
            print(f'{skill} - {count}')

Lanselot = Knight(name = 'Lanselot', skills=20, day = 5)
Galahat = Knight(name = 'Galahat', skills=50, day = 3)

print('.'*20, 'Lanselot, на нас напали!')
print('.'*20, 'Galahat, на нас напали!')
Lanselot.start()
Galahat.start()

print('.'*5, 'Еще ждем')
Lanselot.join()
Galahat.join()
print('.'*5, 'Все битвы закончились!')