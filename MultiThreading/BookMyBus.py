from threading import *

class BookMyBus:
    
    def __init__(self,availableSeats):
        self.availableSeats=availableSeats
        self.l = Semaphore() #or Lock()
    
    def buy(self,seatsRequested):
        self.l.acquire()
        
        print("Total seats available: ",self.availableSeats)
        if self.availableSeats>=seatsRequested:
            print(current_thread().getName())
            print("Confirming a seat")
            print("Processing the payment")
            print("Printing the ticket")
            self.availableSeats-=seatsRequested
        else:
            print("Sorry, no seats available.")
        
        self.l.release()

obj = BookMyBus(10)

t1 = Thread(target=obj.buy,args=(3,))
t2 = Thread(target=obj.buy,args=(4,))
t3 = Thread(target=obj.buy,args=(4,))

t1.start()
t2.start()
t3.start()