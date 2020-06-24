class ObjectCounter:
    
    NumberOfObjects=0
    
    def __init__(self):
        ObjectCounter.NumberOfObjects+=1
    
    @staticmethod
    def DisplayCount():
        print(ObjectCounter.NumberOfObjects)

o1=ObjectCounter()
o2=ObjectCounter()

ObjectCounter.DisplayCount()