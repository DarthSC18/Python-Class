#write a python code to perform addition of 2 com plex numbers by passing object as a parameter
#write a python code to perform addition of 2 complex numbers by passing object as a parameter
#self.variable=current objec.variable
#prac7-1:24-02025
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def add(self,other):
        real=self.real+other.real
        img=self.img+other.img
        return complex(real,img)

    def display(self):
        print(f"{self.real}+{self.img}I")

c1=complex(2,3)
c2=complex(4,5)
c3=c1.add(c2)
c1.display()
c2.display()
c3.display()
