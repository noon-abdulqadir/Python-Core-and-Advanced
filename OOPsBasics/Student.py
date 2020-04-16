class Student:
    major = "CSE"
    
    def __init__ (self,rollno,name): # parameterized constructor initialize and create fields on class
        self.rollno=rollno
        self.name=name

s1=Student(1,"John")
s2=Student(2,"Bill")

print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)