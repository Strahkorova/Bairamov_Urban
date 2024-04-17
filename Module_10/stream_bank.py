import threading
import time
from threading import Thread

class banks(Thread):

    def __init__(self, deposit, withdrawal):
        self.deposit = deposit
        self.withdrawal = withdrawal
        self.lock = threading.Lock()

        print(f"В банке открыт счет на сумму {self.deposit} руб!")

    #пополнение счета
    def replenishment(self):
        R = self.deposit+800
        print(f"На банксовком счету {self.deposit} руб!")
        while self.deposit < R:
            with self.lock:
                if self.deposit != 0:
                    self.deposit = self.withdrawal + self.deposit
                    print(f'Накапали проценты на дипозит. Денег на счете - {self.deposit}')
                else:
                    print(f'Ваш счет равен 0 руб.')
                    break
                time.sleep(0.2)

    def Withdrawal(self):
        while self.deposit != 0:
            with self.lock:
                if self.deposit >= self.withdrawal:
                    self.deposit = self.deposit - self.withdrawal
                    print(f'С дипазита сняли деньги! Денег на счете - {self.deposit}')
                else:
                    print('Снимать деньги нельзя! У вас на счете минимальный допустимый остаток')
                    break
                time.sleep(0.2)



bank = banks(1000, 100)


deposito = threading.Thread(target=bank.replenishment)
withdra = threading.Thread(target=bank.Withdrawal)

deposito.start()
withdra.start()

deposito.join()
withdra.join()