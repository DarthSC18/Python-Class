prac 7-3
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary) #Calling Base class Constructor
        self.dept=dept
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.dept)
        
class Developer(Employee):
    def __init__(self,name,salary,lang):
        super().__init__(name,salary)
        self.lang=lang
        
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.lang)
    
M1=Manager("John",1000,"IT")
D2=Developer("Alice",2000,"C++")
M1.display()
D2.display()
