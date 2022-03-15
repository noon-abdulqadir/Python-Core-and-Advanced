import threading
from threading import Thread

def DisplayNumbers():
    print(threading.current_thread().getName())
    for i in range(11):
        print(i)

print(threading.current_thread().getName())
t = Thread(target=DisplayNumbers)
t.start()