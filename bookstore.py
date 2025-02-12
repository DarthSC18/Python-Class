class bookstore:
    def __init__(self,stock,author,price,title):
        self.stock=stock
        self.author=author
        self.price=price
        self.title=title

    def sell_book(self,quantity):
        if self.stock<quantity:
            print("Out of Stock")
        else:
            self.stock=self.stock-quantity
            print("Stock is available: ")
    def add_stock(self, quantity):
        self.stock=self.stock+quantity
        print(quantity," stock quanitty added to: ",self.title)
    def display(self):
        print("Title: ",self.title, "Author: ", self.author, "Stock: ",self.stock)

book1=bookstore(15, "Leo Tolstoy", 600, "War and Peace")
book1.sell_book(5)
book2=bookstore(1, "Fyodor Doestovsky", 599, "Crime and Punishment")
book2.sell_book(5)
