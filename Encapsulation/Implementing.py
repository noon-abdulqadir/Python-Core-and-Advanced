class Student:
    def setID(self,ids): #Imitator methods
        self.ids=ids
    
    def getID(self): #Accessor methods
        return self.ids
    
    def setName(self,name):
        self.name=name
    
    def getName(self):
        return self.name

s = Student()
s.setID(123)
s.setName("John")

print(s.getID())
print(s.getName())