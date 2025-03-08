class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model

class Car(Vehicle):
    def __init__(self,make,model,fuel_type):
        super(). __init__(make,model)
        self.fuel_type=fuel_type
    def display(self):
        print("Make: ",self.make)
        print("Model",self.model)
        print("Fuel Type:",self.fuel_type)
class Truck(Vehicle):
    def __init__(self,make,model,cargo_capacity):
        super(). __init__(make,model)
        self.cargo_capacity=cargo_capacity
    def display(self):
        print("Make: ",self.make)
        print("Model",self.model)
        print("Cargo Capacity:",self.cargo_capacity)

C1=Car("Skoda","Kodiaq","Diesel")
C2=Car("BMW","X7","Petrol")
T1=Truck("Ford","F-150",10000)
T2=Truck("Tesla","Cybertruck",100000)
C1.display()
C2.display()
T1.display()
T2.display()
