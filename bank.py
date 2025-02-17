class design:
    def __init__(self,aid,ah,b):#constructor
        self.aid=aid
        self.ah=ah
        self.b=b
    def bal(self):#checking balance
        print("Account ID: ",self.aid," and Name: ",self.ah)
        print("Balance: Rs.",self.b)
    def dep(self,cred):#depositing amount 'cred'
        print("Amount to be deposited: Rs.",cred," in ID: ",self.aid," and Name: ",self.ah," and Balance: ",self.b)
        self.b=self.b+cred
        print("New Balance= Rs.",self.b)
    def deb(self,deb):#debiting amount 'deb
        print("Amount to be withdrawn: Rs.",deb," in ID: ",self.aid," and Name: ",self.ah," and Balance: ",self.b)
        if deb<self.b:#to check if balance is there
            self.b=self.b-deb
            print("New Balance= Rs.",self.b,"\n")
        else:
            print("Insuffiecient Balance\n Current Balance: Rs.",self.b,"\n")
            

d1=design(12345, "Walt", 100000)#id,name,balance in order
d1.bal()
d1.dep(5000)
d1.deb(400)
d2=design(12465, "Jesse", 100000)
d2.bal()
d2.dep(500)
d2.deb(100000000)
                

