import pickle,Student

with open("student.dat","wb") as f:
    s = Student.Student(123,"John",90)
    pickle.dump(s,f)