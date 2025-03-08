class Number:
    def __init__(self):
        self.x=int(input("Enter number: "))
        
class Square(Number):
    def calc(self):
        return self.x**2

class Cube(Number):
    def calc(self):
        return self.x**3
    
print(f"Square: {Square().calc()}")
print(f"Cube: {Cube().calc()}")

