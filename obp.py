class Prime:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
        
    def isPrime(self,n):
        for i in range(2,n):
            if n%i==0:
                return False
            else:
                return True
    def calc(self):
            for i in range(self.n1,self.n2):
                if self.isPrime(i):
                    print(i)
      

p=Prime(2,10)
p.calc()
