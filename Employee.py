class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,salary,dept):
        super(). __init__(name,salary)
        self.dept=dept

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.dept)
        
class Developer(Employee):
    def __init__(self,name,salary,lang):
        super(). __init__(name,salary)
        self.lang=lang
        
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Language:",self.lang)
M1=Manager("Michael",50000,"Sales")
M1.display()
M2=Manager("David",500000,"Corporate")
M2.display()
D1=Developer("Dwight",50000,"HTML")
D1.display()
D2=Developer("Jim",50000,"Java")
D2.display()
        
