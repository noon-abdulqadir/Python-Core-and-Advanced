from abc import abstractmethod,ABC#,ABCMeta

class BMW(ABC):
    #__metaclass__ = ABCMeta
    
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def drive(self):
        pass
    
class ThreeSeries(BMW):#inherit
    
    def __init__(self,CruiseControlEnabled,make,model,year):
        #BMW.__init__(self, make, model, year)
        super().__init__(make, model, year)
        self.CruiseControlEnabled=CruiseControlEnabled
    
    def display(self):
        print(self.CruiseControlEnabled)
    
    def start(self):
        super().start()
        print("Button Start.")
    
    def stop(self):
        super().stop()
        print("Button Stop.")
    
    def drive(self):
        print("Three Series is being driven.")
    
class FiveSeries(BMW):#inherit
    
    def __init__(self,ParkingAssistEnabled,make,model,year):
        BMW.__init__(self, make, model, year)
        #super().__init__(make, model, year)
        self.ParkingAssistEnabled=ParkingAssistEnabled
    
    def start(self):
        super().start()
        print("Remote Start.")
    
    def stop(self):
        super().stop()
        print("Remote Stop.")
    
    def drive(self):
        print("Five Series is being driven.")

threeSeries = ThreeSeries(True,"BMW","328i",2018)
print(threeSeries.CruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()

fiveSeries = FiveSeries(True,"BMW","525i",2020)
print(fiveSeries.ParkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)

threeSeries.drive()
fiveSeries.drive()