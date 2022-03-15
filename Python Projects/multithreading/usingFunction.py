from threading import *

def displayNumbers():
    print(current_thread().getName())
    for i in range(11):
        print(i)

print(current_thread().getName())
t = Thread(target=displayNumbers)
t.start()