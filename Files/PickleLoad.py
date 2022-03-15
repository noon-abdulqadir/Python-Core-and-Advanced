import pickle

with open("student.dat","rb") as f:
    obj = pickle.load(f)
    obj.display()