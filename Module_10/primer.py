from queue import Queue
import time, datetime, threading

students= [(99, "Андрей"),
           (76, "Александр"),
           (75, "Никита"),
           (72, "Евгений"),
           (66, "Алексей"),
           (62, "Сергей"),
           (50, "Михаил")]

def student(q):
    while True:
        # Получаем задание из очереди
        check = q.get()
        # Выводим время начала проверки
        print(check[1], 'сдал работу в', datetime.datetime.now().strftime('%H:%M:%S'))
        #Время затраченное на проверку, которое зависит от рейтинга
        time.sleep((100-check[0])/5)
        # Время окончания проверки
        print(check[1], 'забрал работу в', datetime.datetime.now().strftime('%H:%M:%S'))
        # Даём сигнал о том, что задание очереди выполнено
        q.task_done()

# Создаем очередь
q = Queue()
# Загружаем в очередь студентов
for x in students:
    q.put(x)
#создаём и запускаем потоки
thread1 = threading.Thread(target=student, args=(q,), daemon=True)
thread2 = threading.Thread(target=student, args=(q,), daemon=True)
thread1.start()
time.sleep(10)
thread2.start()
# Блокируем выполнение до завершения всех заданий
q.join()
print("Этот текст напечатается после окончания блокировки")