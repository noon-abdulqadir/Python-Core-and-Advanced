class Student:
    def __init__(self,ids,name,testscore):
        self.ids=ids
        self.name=name
        self.testscore=testscore
    
    def display(self):
        print(self.ids,self.name,self.testscore)