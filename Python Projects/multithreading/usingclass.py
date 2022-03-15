from threading import *
from time import sleep

class MyThread:
    
    def displayNumbers(self):
        print(current_thread().getName())
        sleep(1)
        for i in range(11):
            print(i)

obj = MyThread()
t = Thread(target=obj.displayNumbers)
t.start()

t2 = Thread(target=obj.displayNumbers)
t2.start()

t3 = Thread(target=obj.displayNumbers)
t3.start()
