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
        print(f"На банксовком счету {self.deposit} руб!")
        while self.deposit < 1500:
            with self.lock:
                if self.deposit != 0:
                    self.deposit = 100 + self.deposit
                    print(f'Накапали проценты на дипозит. Денег на счете - {self.deposit}')
                else:
                    print(f'Ваш счет равен 0 руб.')
                    break
                time.sleep(0.2)

    #снятие наличных
    def Withdrawal(self):
        while self.deposit != 0:
            with self.lock:
                if self.deposit >= 150:
                    self.deposit = self.deposit - self.withdrawal
                    print(f'С дипазита сняли деньги! Денег на счете - {self.deposit}')
                else:
                    print('Снимать деньги нельзя! У вас на счете минимальный допустимый остаток')
                    #break
                time.sleep(0.2)



bank = banks(1000, 200)


deposito = threading.Thread(target=bank.replenishment)
withdra = threading.Thread(target=bank.Withdrawal)

deposito.start()

deposito.join()
withdra.start()


withdra.join()
