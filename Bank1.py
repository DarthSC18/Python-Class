class Bank:
    def __init__(self,aid,h,b):
        self.aid=aid
        self.h=h
        self.b=b

    def deposit(self,amt):
        print("The Amount Deposited is: ",amt," and Current Balance: ",self.b)
        self.b=self.b+amt
        print("New Balance: :",self.b)
        
    def withdraw(self,amt):
        print("Amount to be Withdrawn: ",amt) 
        if self.b>amt:
            self.b=self.b-amt
            print("New Balance: ",self.b)
        else:
            print("Insufficient Funds")
    def disbal(self):
        print("Current Balance of: ",self.h," and Account ID: ",self.aid,"is",": ",self.b)

d1=Bank(1234,"Walter",100000)
d1.disbal()
d1.deposit(5000)
d1.withdraw(1000)
s2=Bank(4321,"Jesse",10000)
s2.disbal()
s2.withdraw(1000000)
s2.deposit(100000)
