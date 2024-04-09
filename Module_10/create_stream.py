import time
from threading import Thread

def listing(list):
    for i in list:
        print(i)
        time.sleep(1)


var_int = range(0, 11)
var_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#listing(var_int)

thread = Thread(target=listing, args=(var_int,))
thread.start()

listing(var_letter)
thread.join()
