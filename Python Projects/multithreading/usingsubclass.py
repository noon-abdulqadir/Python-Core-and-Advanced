from threading import Thread

class MyThread(Thread):
    def run(self):
        for i in range(11):
            print(i)
            
t = MyThread()
t.start()
         