import pickle,student

with open("student.dat","wb") as f:
    s = student.Student(123,"John",90)
    pickle.dump(s,f)