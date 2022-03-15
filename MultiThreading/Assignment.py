from threading import *    

class Numbers:
    
    def __init__(self):
        self.c = Condition()
    
    def MainThread(self):
        
        print("Current Thread:",current_thread().getName())
        for i in range(1,101):
            print(i)
    
    def EvenNumbersThread(self):
        self.c.acquire()

        print("Current Thread:",current_thread().getName())
        for i in range (1,101):
            if i%2==0:
                print(i)
        self.c.notify()
        self.c.release()
        
    def OddNumbersThread(self):
        self.c.acquire()

        print("Current Thread:",current_thread().getName())
        for i in range (1,101):
            if i%2!=0:
                print(i)
        self.c.wait(timeout=0)
        self.c.release()

numbers = Numbers()

print(numbers.MainThread())
even = Thread(target=numbers.EvenNumbersThread)
odd = Thread(target=numbers.OddNumbersThread)
even.start()
odd.start()