#write a python code to calc greatest of 2 numbers using inheritsnce
class Number1:
    def __init__(self,x):
        self.x=x
class Number2(Number1):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def great(self):
        if self.x==self.y:
            print("Numbers are Equal")
        elif self.x==self.y:
            print(f"{self.x} is greater than {self.y}")
        else:
            print(f"{self.y} is greater than {self.x}")

x=int(input("Enter the First Number: "))
y=int(input("Enter the Second Number: "))
z=Number2(x,y)
z.great()
