class prime:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def cal(self):
        print("prime nos between ",self.n1," and ",self.n2," is ")
        for i in range(self.n1,self.n2+1):
            p=0
            for j in range(2,i):
                if i%j==0:
                    p=1
                    break
            if p==0:
                print(i," ")

p=prime(2,10)
p.cal()
