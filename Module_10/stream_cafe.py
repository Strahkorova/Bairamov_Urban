import time
from queue import Empty, Queue
from threading import Thread

class Table():

    table_count = {}
    def __init__(self, number):
        self.number = number
        self.busy = 0

    def Table(self):
        i = 1
        while i != self.number+1:
            Table.table_count[f"Стол № {i}"] = self.busy
            i += 1
        print(Table.table_count)


class Cafe(Thread):
    def __init__(self, queue_count, Table):
        self.queue_1 = 0
        self.table = Table
        self.queue_count = queue_count
        self.queue = Queue()

    #моделирует приход посетителя
    def customer_arrival(self):
        i = 1
        while i != self.queue_count + 1:
            print(f"Посетитель номер - {i} прибыл")
            time.sleep(1)
            self.queue.put(i)
            i += 1

    #моделирует обслуживание посетителя
    def serve_customer(self):
        while True:
            try:
                item = self.queue.get()
            except Empty:
                continue
            else:
                print(f'Обрабатываем элемент {item}')
                time.sleep(2)
                self.queue.task_done()






#class Customer():


c = Cafe(4, Table.table_count)
t = Table(4)
t.Table()

producer_thread = Thread(target=c.customer_arrival)
producer_thread.start()

consumer_thread = Thread(target=c.serve_customer)
consumer_thread.start()

# дожидаемся, пока все задачи добавятся в очередь
producer_thread.join()

# дожидаемся, пока все задачи в очереди будут завершены
consumer_thread.join()
Queue().join()
#c.customer_arrival()
#c.serve_customer()

