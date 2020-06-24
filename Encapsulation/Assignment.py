class Patient:
    
    def setID(self,id):
        self.__id=id
    
    def getID(self):
        return self.__id
    
    def setName(self,name):
        self.__name=name
    
    def getName(self):
        return self.__name
    
    def setSSN(self,ssn):
        self.__ssn=ssn
    
    def getSSN(self):
        return self.__ssn

p=Patient()
p.setID(123)
p.setName("John")
p.setSSN(456)

print(p.getID())
print(p.getName())
print(p.getSSN())