#prac 7- 2)
class Bank:
    def __init__(self,accno,bal):
        self.accno=accno
        self.bal=bal
    def deposit(self,amount):
        if amount>0:
            self.bal+=amount
            return True
        return False
    def withdraw(self,amount):
        if amount>0 and amount<self.bal:
            self.bal=self.bal-amount
            return True
        return False
    def fund_transfer(from_acc,to_acc,amount):
        if from_acc.withdraw(amount):
            to_acc.deposit(amount)
            return from_acc,to_acc
        else:
            print("Transaction Failed")
            return from_acc,to_acc
    def display(self):
        print("Available Balance",self.bal)
    
c1=Bank(1001,5000)
c2=Bank(1002,6000)
print("Before Transfer")
c1.display()
c2.display()
c1,c2=Bank.fund_transfer(c1,c2,2000)
print("After Transfer")
c1.display()
c2.display()
