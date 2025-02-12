class student:
    def __init__(self, n1,n2):
       self.a=n1
       self.b=n2
       self.add=self.a+self.b

    def display(self):
        print("addition",self.add)

s1=student(1,2) #s1 object created
s1.display()
