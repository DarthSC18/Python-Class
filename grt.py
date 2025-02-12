class grtr:
    def __init__(self, a,b):
       self.a=a
       self.b=b

    def calc(self):
        if self.a>self.b:
            return 1
        elif self.a<self.b:
            return 0
        else:
            return 2
    def display(self):
        c=self.calc()
        if c==1:
            print(self.a, " Is the largest ")
        elif c==0:
            print(self.b, " Is the largest ")
        else:
            print("Both are Equal")
g1=grtr(5,4)
g1.display()
