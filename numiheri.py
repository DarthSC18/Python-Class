class Number:
    def __init__(self):
        self.num=int(input("Enter a Number:"))
        

class Square(Number):
    
    def display(self):
        sq=self.num*self.num
        print("The Square of the Numeber:",self.num,"is",sq)
class Cube(Number):

    def display(self):
        cube=self.num*self.num*self.num
        print("The Cube of the Numeber:",self.num,"is",cube)
while(True):
    Square().display()
    Cube().display()
    x=int(input("Press 1 to continue, 0 to break"))
    if x==0:
        break
    
