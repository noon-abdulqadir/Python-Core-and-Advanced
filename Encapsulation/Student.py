class Student:
    def __init__(self):
        self.__id=123
        self.__name="John"
    
    def display(self):
        print(self.__id) #private fields
        print(self.__name)

s=Student()
#s.display()

print(s._Student__id) #name mangling syntax
print(s._Student__name)