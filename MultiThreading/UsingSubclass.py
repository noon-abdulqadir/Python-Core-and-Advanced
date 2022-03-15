import threading
from threading import Thread

class MyThread(Thread):
    def run(self):
        print(threading.current_thread().getName())
        for i in range(11):
            print(i)

t = MyThread()
t.start()