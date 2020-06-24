from abc import abstractmethod,ABC

class TouchScreenLaptop(ABC):
    
    @abstractmethod
    def scroll(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    
    def scroll(self):
        print("Scrolling for HP.")
    
class Dell(TouchScreenLaptop):
    
    def scroll(self):
        print("Scrolling for Dell.")
    
class HPNotebook(HP):
    
    def click(self):
        print("Clicking for HPNotebook.")

class DellNotebook(Dell):
    
    def click(self):
        print("Clicking for DellNotebook.")

a = HPNotebook()

print(a.scroll())
print(a.click())

b = DellNotebook()

print(b.scroll())
print(b.click())