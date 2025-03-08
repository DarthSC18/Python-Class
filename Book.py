class Books:
    def __init__(self,t,auth,p,q):
        self.t=t
        self.auth=auth
        self.p=p
        self.q=q

    def sell_book(self,qty):
        if self.q>qty:
            print(qty,"Stock of","Book Name:",self.t,"Sold")
            self.q=self.q-qty
    def add_stock(self,qty):
        print(qty,"Stock of","Book Name:",self.t,"Added to the Inventory")
        self.q=self.q+qty
    def display_details(self):
        print("Title:",self.t,"Author:",self.auth,"Price:",self.p,"Items in Stock:",self.q)
b1=Books("War and Peace","Leo Tolstoy",600,10)
b1.display_details()
b1.sell_book(2)
b1.display_details()
b2=Books("Crime and Punishment","Fyodor Doestovsky",600,1)
b2.display_details()
b2.add_stock(10)
b2.display_details()

